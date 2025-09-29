from typing import Dict, List, Set, Any, Optional, DefaultDict, Tuple
from collections import defaultdict
from collections import Counter
from itertools import combinations, chain
from rapidfuzz.fuzz import token_set_ratio
from fuzzywuzzy import fuzz
import json
import os

categories = ['Int_U', 'Int_D','Con_UU', 'Con_CR', 'LOC_E', 'LOC_IGL', 'LOC_IBU', 'Perm_FC', 'Perm_SU']


def normalize(text: str) -> str:
    """
    Normalize text by stripping whitespace and converting to lowercase.
    Args:
        text: Input string.
    Returns:
        Normalized string.
    """
    return text.strip().lower()

def deduplicate_attribution_entries(
    entries: List[Dict[str, Dict[str, List[Dict[str, Any]]]]],
    preserve_empty_categories: bool = False
) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Deduplicate attribution entries by quoted statement, keeping the longer version when duplicates are found.
    Args:
        entries: List of nested dictionaries with structure: category -> subcategory -> items
        preserve_empty_categories: If True, ensures all category/subcategory combinations from input appear in output (even if empty)
    Returns:
        Deduplicated dictionary with unique quoted statements
    """
    result: DefaultDict[str, DefaultDict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    
    # Collect all possible categories and subcategories for structure preservation
    if preserve_empty_categories:
        all_categories: DefaultDict[str, Set[str]] = defaultdict(set)
        for entry in entries:
            for category, subcats in entry.items():
                for subcat in subcats:
                    all_categories[category].add(subcat)

    # Process entries and deduplicate
    for entry in entries:
        for category, subcats in entry.items():
            for subcat, items in subcats.items():
                for item in items:
                    quote: str = item['quoted_statement']
                    norm_quote: str = normalize(quote)

                    existing_items: List[Dict[str, Any]] = result[category][subcat]
                    replaced: bool = False
                    
                    for i, existing in enumerate(existing_items):
                        existing_norm: str = normalize(existing['quoted_statement'])

                        # Keep longer quote when there's containment
                        if existing_norm in norm_quote:
                            if len(quote) > len(existing['quoted_statement']):
                                existing_items[i] = item
                            replaced = True
                            break
                        elif norm_quote in existing_norm:
                            replaced = True
                            break

                    if not replaced:
                        existing_items.append(item)

    # Ensure all categories/subcategories appear if requested
    if preserve_empty_categories:
        for category, subcats in all_categories.items():
            for subcat in subcats:
                _ = result[category][subcat]  # force creation if missing

    return {cat: dict(subcats) for cat, subcats in result.items()}

def merge_multiple_ai_runs(
    inference_runs: List[Dict[str, Dict[str, List[Dict[str, Any]]]]]
) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Merge multiple AI inference runs into a single deduplicated result.
    Ensures all category/subcategory combinations from any run appear in the final output.
    Args:
        inference_runs: List of AI inference results to merge
    Returns:
        Merged and deduplicated attribution dictionary
    """
    return deduplicate_attribution_entries(inference_runs, preserve_empty_categories=True)

def consolidate_reasoning_chain(
    reasoning_steps: List[Dict[str, Dict[str, List[Dict[str, Any]]]]]
) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Consolidate multiple reasoning steps (e.g., initial + refined analysis) into final result.
    Only preserves structure that actually exists in the reasoning chain.
    Args:
        reasoning_steps: List of reasoning steps to consolidate
    Returns:
        Consolidated attribution dictionary
    """
    return deduplicate_attribution_entries(reasoning_steps, preserve_empty_categories=False)

def map_label(key: str) -> str:
    """
    Map full label key to compact AI label code.
    Args:
        key: Full label key as string.
    Returns:
        Compact AI label code as string.
    """
    mapping: Dict[str, str] = {
        'Locus_External': 'AI_LOC_E',
        'Locus_Internal_Good_Likeable': 'AI_LOC_IGL',
        'Locus_Internal_Bad_Unlikeable': 'AI_LOC_IBU',
        'Stable_Unchangeable': 'AI_Perm_SU',
        'Fluctuate_Changeable': 'AI_Perm_FC',
        'Controllable_Regulated': 'AI_Con_CR',
        'Uncontrollable_Unregulated': 'AI_Con_UU',
        'Deliberate': 'AI_Int_D',
        'Unintentional': 'AI_Int_U',
    }
    return mapping[key]

def comparison_mode(
    inference: Dict[str, Dict[str, List[Dict[str, Any]]]]
) -> Dict[str, List[str]]:
    """
    Transform inference data by mapping labels and extracting quoted statements.
    Args:
        inference: Dictionary with category -> subcategory -> items structure
    Returns:
        Dictionary mapping AI label codes to lists of quoted statements
    """
    out_: Dict[str, List[str]] = {}
    for k, v in inference.items():
        #print(k)
        for kk, vv in v.items():
            #print(map_label(kk))
            out_[map_label(kk)] = [a['quoted_statement'] for a in vv]
    return out_

def matrix(
    GT: List[str],
    INF: List[str],
    threshold: int = 90
) -> Dict[str, int]:
    """
    Perform fuzzy matching between ground truth and inference lists.
    Args:
        GT: Ground truth list of strings
        INF: Inference list of strings
        threshold: Minimum fuzzy match score (default: 90)
    Returns:
        Dictionary with confusion matrix metrics: {'TP': int, 'FN': int, 'FP': int}
    """
    # Preprocess INF: lowercase versions and character counters
    INF_lower: List[str] = [inf.lower() for inf in INF]
    INF_counters: List[Counter] = [Counter(inf) for inf in INF_lower]

    grounded_matches: Set[int] = set()  # Local match candidates for this GT (used for FP tracking)
    inf_matches: Set[int] = set()

    # Iterate over each ground truth string
    for gt_index in range(len(GT)):
        #print("")
        gt: str = GT[gt_index]
        gt_lower: str = gt.lower()  # Normalize case
        matched: bool = False  # Flag to track if GT was matched

        # Try to match against individual INF entries
        for idx, (inf, inf_counter) in enumerate(zip(INF_lower, INF_counters)):
            # Fuzzy match score between GT and INF
            #print(f"Comparing GT: '{gt_lower}' with INF: '{inf}'")
            fuzzy_score: int = fuzz.partial_ratio(gt_lower, inf.replace('...', ""))
            #print(fuzzy_score)
            # Subset match: all characters in GT exist in INF (by frequency)
            subset_match: bool = gt in inf
            #print("subset_match: " + str(subset_match))
            
            # Track INF as a potential candidate if it has some similarity or overlap
            if fuzzy_score >= threshold or subset_match:
                grounded_matches.add(gt_index)
                inf_matches.add(idx)
                matched = True

        # If no single INF matched, try combinations of INF entries
        if not matched:
            #print("!")
            # Only consider INF entries not already used
            inf_indices: List[int] = [i for i in range(len(INF))]

            done: bool = False

            # Try combinations of unused INF entries, starting from size 2
            for r in range(2, len(inf_indices)+1):
                for combo in combinations(inf_indices, r):
                    # Combine text and counters of this combo
                    combined_text: str = " ".join(INF_lower[i] for i in combo)
                    combined_text_: str = "".join(INF_lower[i] for i in combo)

                    # Fuzzy match and subset check against the combined text
                    fuzzy_score: int = token_set_ratio(gt_lower, combined_text)
                    fuzzy_score_: int = token_set_ratio(gt_lower, combined_text_)

                    # If match found, mark all combo indices as used
                    if fuzzy_score >= threshold or fuzzy_score_ >= threshold or gt in combined_text_ or gt in combined_text:
                        done = True
                        grounded_matches.add(gt_index)
                        for a in combo:
                            inf_matches.add(a)

                if done:
                    break

    TP: int = len(grounded_matches)
    FP: int = len(INF) - len(inf_matches)
    FN: int = len(GT) - TP
    return {'TP': TP, 'FN': FN, 'FP': FP}

def calculate_f1_scores(
    confusion_list: List[Dict[str, Dict[str, int]]]
) -> Dict[str, Any]:
    """
    Calculate F1 scores from a list of confusion matrices.
    Args:
        confusion_list: List of confusion matrices, each mapping labels to TP/FP/FN counts
    Returns:
        Dictionary containing per-label F1 scores, macro F1, and micro F1
    """
    from collections import defaultdict

    # Aggregate confusion entries across multiple dictionaries
    aggregated: DefaultDict[str, Dict[str, int]] = defaultdict(lambda: {"TP": 0, "FP": 0, "FN": 0})
    for confusion in confusion_list:
        for label, counts in confusion.items():
            aggregated[label]["TP"] += counts.get("TP", 0)
            aggregated[label]["FP"] += counts.get("FP", 0)
            aggregated[label]["FN"] += counts.get("FN", 0)

    # Per-category F1 scores
    per_label_f1: Dict[str, float] = {}
    total_tp: int = 0
    total_fp: int = 0
    total_fn: int = 0
    
    for label, counts in aggregated.items():
        tp: int = counts["TP"]
        fp: int = counts["FP"]
        fn: int = counts["FN"]

        precision: float = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall: float = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1: float = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        per_label_f1[label] = round(f1, 3)
        total_tp += tp
        total_fp += fp
        total_fn += fn

    # Macro F1: average of all individual F1s
    macro_f1: float = round(sum(per_label_f1.values()) / len(per_label_f1), 3) if per_label_f1 else 0

    # Micro F1: calculated from total TP/FP/FN
    precision_micro: float = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    recall_micro: float = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    micro_f1: float = 2 * precision_micro * recall_micro / (precision_micro + recall_micro) if (precision_micro + recall_micro) > 0 else 0
    micro_f1 = round(micro_f1, 3)

    return {
        "per_label_f1": per_label_f1,
        "macro_f1": macro_f1,
        "micro_f1": micro_f1
    }

def calculate_f1_scores_from_path(
    human_coding_with_transcript: list,
    ai_output_path: str,
    threshold: int = 50
) -> dict:
    """
    Calculate F1 scores from AI output files and human coding data at a given threshold.
    Args:
        human_coding_with_transcript: List of human-coded transcript data
        ai_output_path: Path to directory with AI output JSON files
        threshold: Fuzzy match threshold (default: 50)
    Returns:
        Dictionary with per-label F1, macro F1, and micro F1
    """
    all_matrixes = []
    for oneJson in os.listdir(ai_output_path):
        pathfile = f"{ai_output_path}/{oneJson}"
        if not pathfile.endswith('.json'):
            continue

        try:
            with open(pathfile, "r", encoding="utf-8") as f:
                inference = json.load(f)
            ai_entry = comparison_mode(merge_multiple_ai_runs(inference))
            human_entry = [a for a in human_coding_with_transcript if a["subject_code"] ==oneJson.split(".")[0] ][0]

            one_entry_matrixes = {}

            for acat in categories:
                acat_human = 'Human_'+acat
                acat_ai = 'AI_'+acat
                one_entry_matrixes[acat] = matrix(human_entry[acat_human], ai_entry[acat_ai], threshold = threshold)

            all_matrixes.append(one_entry_matrixes)
        except Exception as e:
            print(f"Error processing {oneJson}: {e}")
        
    return calculate_f1_scores(all_matrixes)
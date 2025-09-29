
inference_instructions_whole = """
You are provided with a Test Case Interview Transcript of a parent discussing their child.

Your task is to systematically extract psychological attributions from the Test Case Interview Transcript using the attribution manuals above provided (Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION). Follow the steps below carefully:

# General Coding Principles:
- Apply strict and conservative thresholds: Only code if the attribution is **clearly stated** and meets the inclusion criteria outlined in the Adapted PASS Manual.
- Avoid inferring meaning across multiple sentences; each sentence must be evaluated **independently** and **stand on its own**.
- Exclude thematic, narrative, or inferential links. Code only **explicit** psychological attributions.
- Code **only** child-referent attributions that are **clearly linked** to **externalizing behavior** or **emotional dysregulation**. Parent-referent statements should be coded only if they are **causal**.
- Do **not** code:
  - Hopes or aspirations
  - Single-instance or anecdotal examples
  - Vague impressions or ambiguous descriptions
  - Contextual or background information without attributional content
  - Statements that do not meet attributional criteria
- When in doubt, **do not code**.

# Unit of Coding – Sentence-Level Attribution:
Each sentence that clearly contains an attribution to a cause of the child’s externalizing behaviour or emotional dysregulation should be coded **independently**, even if multiple sentences across the transcript express the same general idea. Attributional redundancy across sentences is permitted, and each qualifying sentence should be coded **if it strictly meets criteria**.

This approach prioritizes the **frequency and density** of attributional content, not just the presence of unique attributional meanings. Coders must still apply **strict inclusion rules**: only code sentences that meet clear attributional criteria, are child-referent (or parent-referent if causal), and are not merely descriptive or contextual.

Additional Notes for Counting Attributions:
1. **Sentence-Level Counting**: Each sentence that independently meets threshold is counted as one instance.
2. **No Thematic Grouping Across Sentences**: Do not collapse codable sentences expressing similar ideas.
3. **Sentence Independence is Key**: Only count if the sentence stands alone and meets criteria.
4. **Compound Sentences**: If a sentence contains two distinct attributional claims, count each one separately.
5. **Restated or Paraphrased Attributions**: Count each if the restated sentences are independently codable.
6. **Supporting Details Don’t Add Counts**: Do not count elaborations or clarifications as separate attributions.
7. COMMON EXCLUSIONS: Descriptive but non-attributive content, Vague preferences or exaggerated claims without behavioural reference, Dispositional comments without behavioural consequence.
8 Code conservatively: Do not infer attributions or count vague sentiments.
8i. Exclude moment-specific examples or isolated incidents.
8ii. Parent-referent statements only count as Locus (External) when causal.
8iii. Grouped positive traits in one sentence = one code.
8iv. Maintain high reliability by referencing only statements that clearly meet criteria.
8v. Exclude future-oriented hopes (“I hope she gets better”) unless paired with explicit current attribution.
8vi. “Twin contrast” only coded if behavior difference is explicitly attributed to sibling difference.
8vii. Do not infer attributional meaning from emotional tone alone.


# Step-by-Step Instructions:

1. **Evaluate each statement independently and sequentially.**
   - Do not assume connections between statements unless explicitly stated by the parent.

2. **For each statement that contains an attribution**:
   - Identify and label all relevant attribution types, referring strictly to the definitions and criteria in the manuals.
     - Multiple attributions may apply to a single statement — if so, identify each one clearly and separately.
   - Quote the **exact statement** from the transcript.
   - Provide a **clear justification** for each assigned attribution type, explicitly referencing the relevant criteria from the manuals.

3. **Do not infer** or assume intent, emotion, or meaning that is not **explicitly** stated by the parent.
   - Be conservative and rigorous in your judgments — only code what is **clearly supported** by the transcript and **consistent with the manuals**.

4. Use the following attribution categories:
   - **PERMANENCE**: Stable-Unchangeable or Fluctuate-Changeable. (Refer to Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION)
   - **INTENTIONALITY**: Deliberate or Unintentional. (Refer to Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION)
   - **CONTROLLABILITY**: Controllable-Regulated or Uncontrollable-Unregulated. (Refer to Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION)
   - **LOCUS OF CONTROL**: External, Internal (Bad-Unlikeable), Internal (Good-Likeable). (Refer to Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION)

Your final output should be clearly structured, showing:
- The **quoted statement** from the transcript
- All applicable **attribution types** assigned to that statement
- The **justification(s)** for each attribution classification, citing relevant manual definitions

Proceed carefully, analytically, and conservatively. Rely on the manuals for every decision.
"""

def inference_instructions_topic(topic: str) -> str:
   """
   Generate detailed step-by-step instructions for coding a given attribution topic.
   Args:
      topic: The attribution topic (e.g., 'LOCUS_OF_CONTROL', 'PERMANENCE').
   Returns:
      A formatted instruction string for the topic.
   """
   if topic =='LOCUS_OF_CONTROL':
      point_8 = """
8 Code conservatively: Do not infer attributions or count vague sentiments.
8i. Exclude moment-specific examples or isolated incidents.
8ii. Parent-referent statements only count as Locus (External) when causal.
8iii. Grouped positive traits in one sentence = one code.
8iv. Maintain high reliability by referencing only statements that clearly meet criteria.
8v. Exclude future-oriented hopes (“I hope she gets better”) unless paired with explicit current attribution.
8vi. “Twin contrast” only coded if behavior difference is explicitly attributed to sibling difference.
8vii. Do not infer attributional meaning from emotional tone alone.
"""
   else:
      point_8 = """
8 Code conservatively: Do not infer attributions or count vague sentiments.
8i. Exclude moment-specific examples or isolated incidents.
8ii. Grouped positive traits in one sentence = one code.
8iii. Maintain high reliability by referencing only statements that clearly meet criteria.
8iv. Exclude future-oriented hopes (“I hope she gets better”) unless paired with explicit current attribution.
8v. “Twin contrast” only coded if behavior difference is explicitly attributed to sibling difference.
8vi. Do not infer attributional meaning from emotional tone alone.
"""      

   sub_prompt={"LOCUS_OF_CONTROL": 
   "- **LOCUS OF CONTROL**: External, Internal (Bad-Unlikeable), Internal (Good-Likeable). (Refer to Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION)",
   "PERMANENCE": 
   "- **PERMANENCE**: Stable-Unchangeable or Fluctuate-Changeable. (Refer to Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION)",
   "INTENTIONALITY": 
   "- **INTENTIONALITY**: Deliberate or Unintentional. (Refer to Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION)",
   "CONTROLLABILITY": 
   "- **CONTROLLABILITY**: Controllable-Regulated or Uncontrollable-Unregulated. (Refer to Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION)",
   }
   
   prompt = f"""
You are provided with a Test Case Interview Transcript of a parent discussing their child.

Your task is to systematically extract psychological attributions from the Test Case Interview Transcript using the attribution manuals above provided (Adapted PASS MANUAL TO IDENTIFY PERMANENCE ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY INTENTIONALITY ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY CONTROLLABILITY ATTRIBUTION, Adapted PASS MANUAL TO IDENTIFY LOCUS-OF-CONTROL ATTRIBUTION). Follow the steps below carefully:

# General Coding Principles:
- Apply strict and conservative thresholds: Only code if the attribution is **clearly stated** and meets the inclusion criteria outlined in the Adapted PASS Manual.
- Avoid inferring meaning across multiple sentences; each sentence must be evaluated **independently** and **stand on its own**.
- Exclude thematic, narrative, or inferential links. Code only **explicit** psychological attributions.
- Code **only** child-referent attributions that are **clearly linked** to **externalizing behavior** or **emotional dysregulation**. Parent-referent statements should be coded only if they are **causal**.
- Do **not** code:
  - Hopes or aspirations
  - Single-instance or anecdotal examples
  - Vague impressions or ambiguous descriptions
  - Contextual or background information without attributional content
  - Statements that do not meet attributional criteria
- When in doubt, **do not code**.

# Unit of Coding – Sentence-Level Attribution:
Each sentence that clearly contains an attribution to a cause of the child’s externalizing behaviour or emotional dysregulation should be coded **independently**, even if multiple sentences across the transcript express the same general idea. Attributional redundancy across sentences is permitted, and each qualifying sentence should be coded **if it strictly meets criteria**.

This approach prioritizes the **frequency and density** of attributional content, not just the presence of unique attributional meanings. Coders must still apply **strict inclusion rules**: only code sentences that meet clear attributional criteria, are child-referent (or parent-referent if causal), and are not merely descriptive or contextual.

Additional Notes for Counting Attributions:
1. **Sentence-Level Counting**: Each sentence that independently meets threshold is counted as one instance.
2. **No Thematic Grouping Across Sentences**: Do not collapse codable sentences expressing similar ideas.
3. **Sentence Independence is Key**: Only count if the sentence stands alone and meets criteria.
4. **Compound Sentences**: If a sentence contains two distinct attributional claims, count each one separately.
5. **Restated or Paraphrased Attributions**: Count each if the restated sentences are independently codable.
6. **Supporting Details Don’t Add Counts**: Do not count elaborations or clarifications as separate attributions.
7. COMMON EXCLUSIONS: Descriptive but non-attributive content, Vague preferences or exaggerated claims without behavioural reference, Dispositional comments without behavioural consequence.
{point_8}

# Step-by-Step Instructions:

1. **Evaluate each statement independently and sequentially.**
   - Do not assume connections between statements unless explicitly stated by the parent.

2. **For each statement that contains an attribution**:
   - Identify and label all relevant attribution types, referring strictly to the definitions and criteria in the manuals.
     - Multiple attributions may apply to a single statement — if so, identify each one clearly and separately.
   - Quote the **exact statement** from the transcript.
   - Provide a **clear justification** for each assigned attribution type, explicitly referencing the relevant criteria from the manuals.

3. **Do not infer** or assume intent, emotion, or meaning that is not **explicitly** stated by the parent.
   - Be conservative and rigorous in your judgments — only code what is **clearly supported** by the transcript and **consistent with the manuals**.

4. Use the following attribution categories:
   {sub_prompt[topic]}
   
Your final output should be clearly structured, showing:
- The **quoted statement** from the transcript
- All applicable **attribution types** assigned to that statement
- The **justification(s)** for each attribution classification, citing relevant manual definitions

Proceed carefully, analytically, and conservatively. Rely on the manuals for every decision.
"""
   return prompt
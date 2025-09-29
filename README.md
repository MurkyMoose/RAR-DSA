# RAR-DSA

Retrieval-Augmented Reflexion with Dimension-Specific Agents to Code Attributional Dimensions

This project evaluates large language models (LLMs) and multi-agent strategies for automated attribution coding of interview transcripts. It includes baseline, expert-split, reflexion, and retrieval-augmented approaches, with performance compared to human-coded data.

## Structure
- `src/` — Core experiment and utility scripts
- `definitions/` — Coding manuals, instructions, and data models
- `ai_json_output/` — Model outputs for each experimental run
- `data/` — Human-coded and raw data
- `notebook.ipynb` — Main analysis and experiment notebooks

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## Main Scripts
- `src/experts.py`, `src/reflexion.py`, `src/with_retrieval.py` — Run different experimental conditions
- `src/utils.py` — Merging, evaluation, and fuzzy matching utilities

## Outputs
- Please obtain files from author and put into respective subdirectories `ai_json_output/`, `data/`

## Outputs
- Results and figures are saved in `ai_json_output/` and visualized in the notebooks.

## Citation
If you use this code, please cite the associated research paper.

## Third-Party Licenses
This project uses open source packages under the MIT, BSD, and Apache 2.0 licenses, including but not limited to:

- pydantic (MIT)
- fuzzywuzzy (MIT)
- python-Levenshtein (Apache 2.0)
- matplotlib (PSF/BSD)
- numpy (BSD)
- scikit-learn (BSD)
- tqdm (MIT)
- nest_asyncio (MIT)
- jupyter (BSD)
- chromadb (Apache 2.0)
- openai (MIT)

See individual package documentation for full license details. If you redistribute this project with bundled dependencies, ensure to include their respective license files as required by their terms.

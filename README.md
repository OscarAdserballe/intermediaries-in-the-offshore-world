# Bachelor Thesis – Intermediary Network Analysis (Replication Repository)

This repository contains all material needed to reproduce the empirical results presented in my Bachelor thesis. It is nothing serious, but only meant as an attempt at trying to make my work reproducible and trying (keyword: trying!) something that's more professional than it actually is. The code certainly isn't elegant, but I've tried structuring it using Jupyter notebooks. 

The project investigates the global landscape of **intermediary** firms that facilitate offshore incorporations and explores their geographic specialisation using network-science and statistical techniques, and an agentic workflow enriching their individual profiles using LangGraph. This analysis only touches the surface, and man is there still a lot out there.

## Repository layout

| Path | Purpose |
|------|---------|
| `main.ipynb` | End-to-end workflow that loads prepared datasets, recreates every figure/table shown in the thesis. |
| `scrape_intermediaries.ipynb` | Agentic Workflow using LangGraph as a framework and using Tavily to find information on intermediaries. |
| `enrichment_data/` | Light-weight CSV snapshots used by the notebooks (`*_sample_*.csv`). Raw datasets (hundreds of MB) live in `datasets/` and are ignored by Git. |
| `other/dot-graph/` | Network visualisations (DOT + PNG) referenced in the Methods chapter. |
| `writing/` | LaTeX source of the written thesis. Compile with `latexmk -pdf writing/main.tex`. A ready-made PDF (`writing/main.pdf`) is included for convenience. |
| `datasets/` | Large raw datasets (ignored by default); see _Data access_ below. |

## Thesis & analysis overview

### Written thesis (LaTeX)
`writing/main.tex` compiles the full thesis and pulls in the following chapter files:

1. **Introduction** – sets the scene and research questions.
2. **Theory** – situates the work in the tax‐avoidance and network‐science literature.
3. **Data & Methodology** – documents data sources (ICIJ leaks, V-Dem, Historical Tax Haven Database), cleaning, enrichment, and the Generative‐AI classification approach.
4. **Empirical Analysis** – presents descriptive statistics, network measures, and hypothesis tests on specialisation.
5. **Discussion** – interprets findings and contrasts them with existing scholarship and policy debates.
6. **Conclusion** – summarises contributions and limitations.
7. **Appendix** – extra tables, robustness checks, and the full AI prompt template.

Compile with:
```bash
cd writing
latexmk -pdf main.tex
```

### Main analysis notebook
`main.ipynb` mirrors the thesis flow programmatically:

* Loads the prepared CSV snapshots from `enrichment_data/` (or the heavy raw files if present in `datasets/`).
* Reproduces every figure and table in the thesis – geographic heat-maps, power-law fits, degree distributions, network visualisations, etc.
* Saves final outputs to `writing/images/` so they drop straight into the LaTeX build.
* Execution time ≈ 10–15 min on a modern laptop (most of it spent on network calculations and Plotly figure generation).

A smaller helper notebook, `scrape_intermediaries.ipynb`, shows how the enrichment data were scraped and combined.


## Quick start

1. **Clone & install dependencies** (Python ≥ 3.10):

   ```bash
   gh repo clone OscarAdserballe/topologies-of-intermediaries-in-the-offshore-world
   cd <repo>
   poetry install  # or: pip install -r requirements.txt
   ```

2. **Launch the main notebook**:

   ```bash
   poetry run jupyter lab  # or: jupyter notebook
   # open main.ipynb and run all cells
   ```

3. **Re-compile the thesis (optional - src-links hard-coded anyway)**:

   ```bash
   cd writing
   latexmk -pdf main.tex
   ```

## Data access

The full Offshore Leaks & OpenCorporates datasets are **not** included in the repository for size & licensing reasons.  
If you wish to replicate the analysis from scratch, download the raw files into `datasets/` and adjust the paths at the top of `main.ipynb`.

All enrichment data from the agentic workflow is provided in `enrichment_data/`


# Replication package — Access to non-family credit and household enterprise outcomes

Replication code and aggregated results for the manuscript
**"Non-family credit and the survival of household enterprises in Indonesia: double machine learning under spatial confounding"** (submitted to *Journal of Economics and Development*).

This repository is anonymised for peer review.

## What is (and is not) included

| Included | Not included |
|---|---|
| Code that builds the analysis samples from the original IFLS files and produces every table, figure and Monte Carlo result | IFLS microdata and any file derived from them at the household level (RAND terms of use forbid redistribution) |
| Aggregated results (CSV) behind every table and figure | |
| Raw Monte Carlo output (synthetic data, `results/simulation/sim_raw_FULL.csv.gz`) | |
| Supplementary materials 1 and 2 and the script that rebuilds them | |

## Data access

The Indonesian Family Life Survey (IFLS) is distributed free of charge by the RAND Corporation to registered users:
<https://www.rand.org/well-being/social-and-behavioral-policy/data/FLS/IFLS/download.html>.
Download the household and community files of IFLS3 (2000), IFLS4 (2007) and IFLS5 (2014) in Stata format and keep RAND's folder names. The code reads:

* **IFLS4 (2007)**: `b2_nt1`, `b2_nt2`, `b2_bh` (book 2); `bk_ar1`, `bk_sc` (book K); `pce07nom`; community book 1 section G (`bk1_g`).
* **IFLS5 (2014)**: `htrack`; `b2_nt1`, `b2_nt2`, `b2_bh` (book 2).
* **IFLS3 (2000)**, for the placebo sample (notebook `00`): `b2_nt1`, `b2_nt2` (book 2); `b3b_bh1`, `b3b_bh2` (book 3B); `bk_ar1`, `bk_sc` (book K). Notebook `00` also reads IFLS4 `bk_ar1`, `b2_nt1`, `b2_nt2` and IFLS5 `htrack`, `b2_bh`.

District centroid coordinates, used only to build spatial features, are embedded in notebook `01`. They are taken from the open repository ArrayAccess/Indonesia-Postal-And-Area (<https://github.com/ArrayAccess/Indonesia-Postal-And-Area>), which lists BPS administrative codes with coordinates.

Please cite the IFLS field reports (Strauss et al. 2004, 2009, 2016) and send RAND a link to any publication that uses the data (ifls-papers@rand.org).

## Workflow

| Step | Notebook | Input | Output | Runtime (Kaggle CPU, 4 cores) |
|---|---|---|---|---|
| 0 | `notebooks/00_build_placebo_sample_ifls3.ipynb` | IFLS3, IFLS4 | `umkm_ifls3_placebo.csv` | ~10 min |
| 1 | `notebooks/01_main_analysis_and_simulation.ipynb` | IFLS4, IFLS5, output of step 0 | `umkm_ifls_v2.csv`, `tab/`, `fig/`, `sim/`, `draft/angka_untuk_naskah.md` | empirical part ~45 min; Monte Carlo 2 × ~11 h (sharded) |
| 2 | `notebooks/02_closing_experiments.ipynb` | `umkm_ifls_v2.csv`, `umkm_ifls3_placebo.csv` | `X*_*.csv`, `X_ringkasan.md` | ~1–2 h |
| 3 | `notebooks/03_timing_and_attrition.ipynb` | `umkm_ifls_v2.csv`, `umkm_ifls3_placebo.csv`, IFLS4/IFLS5 `.dta` | `X7_timing.csv`, `X8_attrition_*.csv` | ~1 h |
| 4 | `docs/make_additional_files.py` | `results/` | Supplementary materials 1–2 | < 1 min |

Notebook `01` is controlled by a configuration cell:

* `MODE = "FULL"` reproduces the paper (`"FAST"` is a quick check).
* `MAIN_SCHEME = "random"` is the main specification (random five-fold cross-fitting, covariate set C, district-clustered SE).
* Monte Carlo: set `RUN_SIMULATION = True` and run `SHARD = (0, 2)` and `SHARD = (1, 2)` in two sessions; then run once with `RUN_SIMULATION = False` and both outputs as input. The notebook merges every `sim_raw_FULL_shard*.csv` it finds. To skip the simulation entirely, use `results/simulation/sim_raw_FULL.csv.gz` (unzipped) as input.

All randomness is seeded (`SEED = 2026`); notebook `02` checks that its first cross-fitting split reproduces Table 3 of notebook `01` exactly (−0.0816 for business closure, single split).

The notebooks were written for Kaggle (paths under `/kaggle/input` and `/kaggle/working`) and fall back to `./output` elsewhere. Code comments are partly in Indonesian.

## Where each result comes from

See [`docs/table_map.md`](docs/table_map.md).

## Software

Python ≥ 3.10; see `requirements.txt`. Results in the paper were produced with LightGBM nuisance learners; without LightGBM the code falls back to scikit-learn's HistGradientBoosting and estimates will differ slightly. The causal-forest robustness check needs `econml`.

## Licence

Code: MIT (see `LICENSE`). Aggregated results and supplementary files: CC BY 4.0.

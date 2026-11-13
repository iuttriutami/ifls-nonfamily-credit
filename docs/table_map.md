# Manuscript results → code and files

| Manuscript | Notebook (section) | File in `results/` |
|---|---|---|
| Table 1 Balance | 01 (B, before B4) | `tables/T1_descriptives.csv` |
| Table 2 Monte Carlo, baseline | 01 (A.2) | `simulation/sim_summary_FULL.csv` (block = baseline, rho = 2) |
| Table 3 Average effects (20-split medians) | 02 (X1) | `experiments/X1_repeated.csv` (check = main); OLS: `tables/T2_ols_fe.csv` |
| Table 4 Profit margins | 01 (B6b) | `tables/T4_margins_scale.csv` |
| Table 5 Subgroups | 02 (X4) | `experiments/X4_subgroups.csv` |
| Table 6 Robustness | 02 (X1, X2); 01 (B6) | `experiments/X1_repeated.csv`, `experiments/X2_overlap.csv`, `tables/T5_robustness_usaha_tutup.csv`, `tables/T5b_lopo_usaha_tutup.csv` |
| Table 7A Pre-trend placebo | 00 → 02 (X3) | `experiments/X3_pretrend.csv` |
| Table 7B History-augmented | 01 (E) | `tables/T7_history_augmented.csv` |
| Sect. 6.3 BLP/GATES | 02 (X6) | `experiments/X6_blp_repeated.csv`, `experiments/X6_blp_splits.csv` |
| Sect. 6.4 Sensitivity | 02 (X5) | `experiments/X5_sensitivity.csv` |
| Sect. 7 Targeting | 01 (B7) | `tables/T7b_policy.csv`, `tables/T7_targeting_curve_*.csv` |
| Additional file 1, Tables A1–A7, Figures A1–A2 (closure placebo: 00 → 01, D; CLAN: 01, B5) | `docs/make_additional_files.py` | as above, plus `tables/T3_dml_ate.csv`, `tables/T6c_clan_*.csv`, `tables/T6_placebo.csv` |
| Additional file 2, Table B1, Figures B1–B4 | `docs/make_additional_files.py` | `simulation/sim_summary_FULL.csv` |

Variable names in the CSV files are Indonesian: `usaha_tutup` = business closed, `ihs_laba` = IHS profit, `tenaga_kerja` = workers, `kredit` = non-family credit.
| Table VII Panel C (timing of credit), Table A8 | 03 (X7) | `experiments/X7_timing.csv` |
| Section 6.4 attrition, Table A9 | 03 (X8) | `experiments/X8_attrition_estimates.csv`, `experiments/X8_attrition_balance.csv` |

Table numbers in this map refer to the Journal of Economics and Development version (Roman numerals I–VII; supplementary tables A1–A9, B1).

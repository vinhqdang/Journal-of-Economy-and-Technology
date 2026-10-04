# Blind double extraction: agreement with the original extraction

A separate model run extracted key fields from 16 randomly chosen included studies without seeing the original extraction (seed 20261004). Agreement is the share of studies on which the two extractions give the same value. This measures consistency of reading, not truth; where the two disagree the paper's text decides.

| Field | Agreeing | Share |
|---|---|---|
| n_economies | 13 of 16 | 81% |
| year_first | 15 of 16 | 94% |
| year_last | 15 of 16 | 94% |
| estimator_class | 12 of 16 | 75% |
| gmm_vs_not | 13 of 16 | 81% |
| identification_none_vs_some | 14 of 16 | 88% |
| outcome_families_exact | 16 of 16 | 100% |
| headline_direction | 14 of 16 | 88% |
| income_group_comparison | 12 of 16 | 75% |
| low_income_listed | 5 of 5 | 100% |
| overall_risk_of_bias | 11 of 16 | 69% |

Mean overlap (Jaccard) of the outcome-family sets: 1.00.

## Disagreements

| Study | Field | Original | Blind |
|---|---|---|---|
| 88 | n_economies | 94 | 99 |
| 88 | overall_risk_of_bias | serious | moderate |
| 1372 | estimator_class | FE_RE_OLS | accounting_DEA_other |
| 269 | identification_none_vs_some | other (Granger-type predictive causality only; no instrument or exogenous variation) | none |
| 442 | year_last | (2000, 2022) | (2000, 2021) |
| 442 | overall_risk_of_bias | critical | serious |
| 952 | estimator_class | GMM | FE_RE_OLS |
| 952 | identification_none_vs_some | threshold model | none |
| 952 | overall_risk_of_bias | serious | moderate |
| 126 | estimator_class | GMM | FE_RE_OLS |
| 408 | headline_direction | negative | mixed |
| 408 | overall_risk_of_bias | serious | moderate |
| 138 | n_economies | 193 | 152 |
| 138 | estimator_class | GMM | FE_RE_OLS |
| 138 | overall_risk_of_bias | serious | moderate |
| 341 | n_economies | 110 | 102 |
| 341 | year_first | (1995, 2019) | (2000, 2019) |
| 1713 | headline_direction | positive | mixed |

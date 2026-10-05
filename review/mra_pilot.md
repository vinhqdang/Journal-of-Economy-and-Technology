# Pilot meta-regression: ICT-type adoption and output or productivity

**Status: exploratory pilot, not a result.** The inputs were extracted by machine and every printed number was checked against the source text twice (an automatic proximity check and a second, independent reading of the tables by a separate model run), and the author has since checked a random sample of the extracted data by hand against the source papers (see `data/human_check.md`; the scope of that check is recorded there). Effect sizes are partial correlation coefficients (PCC) computed from the printed coefficient and its standard error or t-statistic, with degrees of freedom approximated as observations minus 10 regressors. The sample is small, comes only from papers with a free or supplied full text, and the underlying studies mostly treat adoption as exogenous, so pooled numbers describe conditional association and not a causal effect.

- Estimates extracted: 318 from 38 papers.
- Usable estimates: 148 from 24 papers. Excluded: uncertainty not convertible to t (p-value or interval) (71); interaction term, not a main effect (49); no usable number of observations (28); technology not ICT-type (crypto or AI) (17); judged not poolable on second-pass check (5).

## 1. One headline estimate per paper, random-effects pooling

- Papers: 22. Pooled PCC = 0.161 (95% CI 0.093 to 0.228). Between-paper variance tau² = 0.0230, I² = 93%. 95% prediction interval -0.144 to 0.465.

- Reading the numbers (rough Doucouliagos convention for partial correlations: 0.07 small, 0.17 medium, 0.33 large): a pooled value in the small-to-medium range with very high I² means papers disagree a lot about size, even if most signs are positive.

- Share of headline estimates that are positive: 86%. Positive and statistically significant: 68%.


## 2. Moderator meta-regression (all main estimates, standard errors clustered by paper)

Estimates: 148; papers (clusters): 24. With fewer than about 30 clusters the clustered standard errors are optimistic, so treat p-values as indicative only.

| Moderator | Coefficient | Clustered SE | p |
|---|---|---|---|
| const | 0.075 | 0.048 | 0.12 |
| lowmid | 0.079 | 0.073 | 0.28 |
| gmm | 0.069 | 0.077 | 0.37 |
| mobile | 0.047 | 0.043 | 0.27 |
| internet | -0.082 | 0.056 | 0.15 |

`lowmid` = the estimate comes from a low- or middle-income, developing or emerging sample (0 otherwise); `gmm` = system or difference GMM; `mobile`, `internet` = technology type relative to general ICT.


Unweighted summary by income setting:

| Setting | Estimates | Papers | Mean PCC |
|---|---|---|---|
| high-income, mixed or not stated | 115 | 21 | 0.114 |
| low/middle-income or developing | 33 | 10 | 0.146 |

## 3. Publication-bias checks

- FAT-PET: PCC = 0.036 + 1.60 x SE. A slope on SE that is clearly different from zero (here p = 0.11) suggests small-study or selective-reporting bias; the intercept (0.036, p = 0.47) is the bias-corrected effect.

- PEESE intercept (bias-corrected effect when a true effect exists): 0.086 (p = 0.03).

- Funnel plot: `figures/funnel.png`.


## 4. Sensitivity of the pooled headline estimate to the degrees-of-freedom assumption

Assumed number of regressors k = 0: 0.158; k = 5: 0.159; k = 20: 0.163. A stable value means the result does not hinge on this approximation.


## What this pilot can and cannot support

- It can show whether there is enough comparable material to run a meta-regression at all, and which moderators are worth pursuing.
- It cannot support a causal statement, a claim about AI (too few estimates), or a firm statement about income groups until the author's hand check is fully documented and the sample is widened beyond the studies found so far (the search had low recall; see google_scholar_results.md).


# Amendment 1 to the macro-panel plan: a valid event study (3 October 2026, written before the new code was run)

**Why.** The stacked event study in `spec.md` (A4, A5) failed its own checks: almost every economy crosses the takeoff threshold inside the window, so clean "never or much later treated" controls were scarce (7 in the low and lower-middle group), and that group showed a pre-trend of 12 log points. The results were reported and marked not interpretable (`summary.md`). This amendment replaces the design. The earlier results stay in the repository as the failed first attempt.

**A4b. Staggered event study with not-yet-treated controls and covariate adjustment** (after Callaway and Sant'Anna, 2021, regression-adjustment version).
- Takeoff year g = first year the mobile measure reaches 10 subscriptions per 100 among economies below 10 in 1995 (main). Robustness: thresholds of 25 and 50 per 100.
- For each cohort g (1996 to 2014) and horizon e from -5 to +10, e not equal to -1, the effect ATT(g, g+e) compares the change in log GDP per capita (times 100) from year g-1 to year g+e for economies with takeoff year g against economies **not yet treated** at year g+e (takeoff later than g+e, or never by 2019). A comparison is estimated only with at least 3 treated and 8 control economies.
- Covariates for the comparison, by outcome regression on controls: log GDP per capita in 1995 and average annual growth from 1995 to g-1 (set to 0 when g = 1996). This removes the part of the pre-trend explained by initial income and earlier growth.
- Aggregation to event time e: average of ATT(g, g+e) over cohorts, weighted by the number of treated economies.
- Subgroups (low and lower-middle, upper-middle, high income): treated economies are restricted to the group and controls are drawn from all groups, with the same covariates.
- Inference: bootstrap over economies (400 draws, whole procedure re-estimated); 95% percentile intervals.
- Pre-trend rule: effects for e from -5 to -2 are placebo effects. A subgroup is interpreted only if the 95% interval of their mean includes zero. Otherwise the result is reported and labelled not interpretable.
- The same estimator is applied to the secondary outcomes (A5) only for samples that pass the pre-trend rule.

**A7. Local projections on the annual panel** (a design without a binary treatment). Shock: change in mobile subscriptions per 100 over the previous three years, in units of 10. Outcome: cumulative growth of GDP per capita from year t to t+h (100 times log difference), h = 0 to 8. Controls: growth over the previous three years, log GDP per capita in year t, country and year fixed effects, standard errors clustered by country; coefficients are separate for the four income groups. Placebo: the shock in the following three years against growth in the preceding three years. This estimates a dynamic association, not a causal effect.

All other statements in `spec.md` stand. No result is dropped.

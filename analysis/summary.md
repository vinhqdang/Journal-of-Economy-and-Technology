# Summary of the macro-panel analysis (what it can and cannot say)

Full tables: `results.md` (1995 to 2019, main) and `results_end2023.md` (sensitivity). Plan: `spec.md`. Data: `data/wdi_panel.csv` (World Bank WDI, downloaded 3 October 2026; CO2 emissions could not be retrieved).

These are fixed-effects associations. None of them identifies a causal effect.

## What the data support
1. **Mobile adoption and growth, by income group (A1).** Over 5-year periods, a 10-subscription increase per 100 people goes with higher annual growth in every income group: 0.36 pp in low-income (95% CI -0.05 to 0.76), 0.47 pp in lower-middle income (0.16 to 0.77), 0.16 pp in upper-middle (0.04 to 0.28) and 0.16 pp in high income (0.05 to 0.26). The association is largest in lower-middle income economies, and about two to three times the upper-middle and high-income figures. With country fixed effects the lower-middle association stays (0.36, p = 0.03) and the others shrink toward 0.13 to 0.20. Ending the sample in 2023 gives the same pattern (lower-middle 0.34, p < 0.01; upper-middle 0.05, not significant).
2. **Dose-response (A3).** Across all economies the association is largest where mobile adoption was below 10 per 100 at the start of a period (0.41) and smaller at 40 to 80 per 100 (0.18); it does not vanish at high adoption (0.27 above 80). It is not monotone, and for low and lower-middle income economies the point estimate above 80 per 100 is the largest (1.37) but imprecise (95% CI -0.01 to 2.74), based on 35 observations.
3. **Within low and lower-middle income economies (A6).** None of secondary enrolment, electricity access, private credit or initial income significantly changes the mobile association (all p > 0.19). The data do not support, or rule out, the claim that these conditions matter inside this group; the confidence intervals are wide (a standard-deviation change in a moderator could change the association by about 0.3 pp in either direction).

## What the data do not support
- **A predetermined version (A2) does not reproduce the pattern.** When the regressor is the previous period's change in mobile adoption, the association is positive only in lower-middle income economies (0.26, p = 0.02), near zero in upper-middle, and negative in low-income (-0.38, p = 0.13) and high-income (-0.16, p = 0.01) economies. For internet use the predetermined association is negative in every income group (largest in low-income economies, -3.9 pp per +10 points of users, p = 0.06). The contemporaneous association in A1 therefore partly reflects growth driving adoption or common shocks, and it should not be read as a payoff to adoption.
- **The first event study (A4, A5, stacked cohorts) was not interpretable and has been replaced** by the design in `spec_amendment.md` (A4b); see the section below and `results_event.md`.
- **Fixed broadband (A1, A2) is not interpretable.** Subscriptions per 100 changed by small amounts over most periods, so a "10-unit" change lies far outside the data for low-income economies, and the estimates (for example -21 pp in low-income economies) reflect extrapolation from very few observations (34 for low-income).
- **Cost-effectiveness** was not attempted; WDI has no price or investment series for these technologies.

## Departures from `spec.md`
- Income groups use only the current World Bank classification; the planned sensitivity check with initial GDP per capita was not run.
- CO2 emissions per capita were not retrieved (the indicator did not download), so that A5 row is empty.
- For the event study, controls came from the same income group when at least 8 clean controls existed, and from all groups otherwise (upper-middle and high-income samples), as flagged in the tables.
- The two broadband specifications and the 2023 sensitivity are reported in full but not interpreted beyond what is stated above.

## Event study with not-yet-treated controls (A4b) and local projections (A7)
Full tables: `results_event.md`. Plan: `spec_amendment.md`. Figures: `figures/event_study_cs.png`, `figures/lp.png`.

- **Pre-trends.** With the takeoff at 10 mobile subscriptions per 100, the pre-trend rule is passed in all four samples. With a threshold of 50 the pooled and upper-middle samples fail it and are not interpreted.
- **Event study.** Five years after takeoff, log GDP per capita is about 14 log points higher than in not-yet-treated economies (95% CI 0.6 to 36.5). The gain is distinguishable from zero only in high-income economies (19, CI 6.2 to 36.7). For low and lower-middle income economies the estimate is -5.9 (CI -18.6 to 31.9), too wide to rule out an effect of the high-income size, and no estimate is possible at ten years (too few not-yet-treated controls). The ten-year estimate for all economies (48 log points) is implausibly large for a causal effect and mostly reflects different growth paths of early and late adopters.
- **Outcomes beyond income.** Life expectancy is about 0.9 years higher at five years (CI 0.1 to 1.7); under-5 mortality is 15 log points lower in low and lower-middle income economies (CI -26.0 to 1.0). Unemployment and agriculture share fail the pre-trend rule in most samples. These are descriptive.
- **Local projections.** For lower-middle income economies, cumulative growth is 0.4 pp higher after one year and 2.0 pp higher after six years per +10 subscriptions (CI 0.8 to 3.2). The profile is flat for upper-middle and high-income economies. For low-income economies it turns negative at long horizons (-4.3 pp at eight years, CI -9.2 to 0.6).
- **Across designs.** No income group has a significantly positive association under all four designs (same-period, previous-period, event study, local projections). Lower-middle income is positive under three, high income under two, upper-middle under one, low income under none. The designs do not agree on which group gains more.

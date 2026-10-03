# Summary of the macro-panel analysis (what it can and cannot say)

Full tables: `results.md` (1995 to 2019, main) and `results_end2023.md` (sensitivity). Plan: `spec.md`. Data: `data/wdi_panel.csv` (World Bank WDI, downloaded 3 October 2026; CO2 emissions could not be retrieved).

These are fixed-effects associations. None of them identifies a causal effect.

## What the data support
1. **Mobile adoption and growth, by income group (A1).** Over 5-year periods, a 10-subscription increase per 100 people goes with higher annual growth in every income group: 0.36 pp in low-income (95% CI -0.05 to 0.76), 0.47 pp in lower-middle income (0.16 to 0.77), 0.16 pp in upper-middle (0.04 to 0.28) and 0.16 pp in high income (0.05 to 0.26). The association is largest in lower-middle income economies, and about two to three times the upper-middle and high-income figures. With country fixed effects the lower-middle association stays (0.36, p = 0.03) and the others shrink toward 0.13 to 0.20. Ending the sample in 2023 gives the same pattern (lower-middle 0.34, p < 0.01; upper-middle 0.05, not significant).
2. **Dose-response (A3).** Across all economies the association is largest where mobile adoption was below 10 per 100 at the start of a period (0.41) and smaller at 40 to 80 per 100 (0.18); it does not vanish at high adoption (0.27 above 80). It is not monotone, and for low and lower-middle income economies the point estimate above 80 per 100 is the largest (1.37) but imprecise (95% CI -0.01 to 2.74), based on 35 observations.
3. **Within low and lower-middle income economies (A6).** None of secondary enrolment, electricity access, private credit or initial income significantly changes the mobile association (all p > 0.19). The data do not support, or rule out, the claim that these conditions matter inside this group; the confidence intervals are wide (a standard-deviation change in a moderator could change the association by about 0.3 pp in either direction).

## What the data do not support
- **A predetermined version (A2) does not reproduce the pattern.** When the regressor is the previous period's change in mobile adoption, the association is positive only in lower-middle income economies (0.26, p = 0.02), near zero in upper-middle, and negative in low-income (-0.38, p = 0.13) and high-income (-0.16, p = 0.01) economies. Internet use shows the same sign reversals. The contemporaneous association in A1 therefore partly reflects growth driving adoption or common shocks, and it should not be read as a payoff to adoption.
- **The event study around mobile takeoff (A4 and A5) is not interpretable.** Nearly every economy crosses 10 subscriptions per 100 during the window (189 of 190 below 10 in 1995), so clean never-treated controls are scarce (7 in the low and lower-middle group, 30 overall). The low and lower-middle group shows a clear pre-trend (mean +12 log points before takeoff), so its post-takeoff estimates (a fall of 16 to 18 log points, with confidence intervals spanning zero) are driven by differential pre-trends. The same design applied to life expectancy, mortality, unemployment and agriculture share is unreliable for the same reason, so we do not interpret those rows. Timing around technology arrival remains an open question.
- **Fixed broadband (A1, A2) is not interpretable.** Subscriptions per 100 changed by small amounts over most periods, so a "10-unit" change lies far outside the data for low-income economies, and the estimates (for example -21 pp in low-income economies) reflect extrapolation from very few observations (34 for low-income).
- **Cost-effectiveness** was not attempted; WDI has no price or investment series for these technologies.

## Departures from `spec.md`
- Income groups use only the current World Bank classification; the planned sensitivity check with initial GDP per capita was not run.
- CO2 emissions per capita were not retrieved (the indicator did not download), so that A5 row is empty.
- For the event study, controls came from the same income group when at least 8 clean controls existed, and from all groups otherwise (upper-middle and high-income samples), as flagged in the tables.
- The two broadband specifications and the 2023 sensitivity are reported in full but not interpreted beyond what is stated above.

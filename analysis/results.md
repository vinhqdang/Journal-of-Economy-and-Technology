# Results of the macro-panel analysis (spec: `spec.md`)

Data: World Bank WDI, 1995 to 2019. Exploratory associations, not causal effects. Income groups are the current World Bank classification. Coefficients are in percentage points of annual GDP-per-capita growth per 10-unit change in the technology measure, with 95% confidence intervals from standard errors clustered by country. Cells with fewer than 15 economies are marked and not interpreted.

## A1 contemporaneous, mobile subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 20 | 65 | 0.355 [-0.046, 0.757] (p=0.08) |
| Lower-middle | 42 | 168 | 0.465 [0.163, 0.766] (p=0.00) |
| Upper-middle | 51 | 190 | 0.156 [0.037, 0.275] (p=0.01) |
| High | 64 | 232 | 0.155 [0.046, 0.264] (p=0.01) |

With country fixed effects added: Low 0.196 (p=0.35); Lower-middle 0.357 (p=0.03); Upper-middle 0.136 (p=0.05); High 0.129 (p=0.03)

## A3 dose-response by baseline mobile level (per 100 people at start of period)

| Sample | Baseline bin | Obs | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| All economies | <10 | 186 | 0.405 [0.249, 0.561] (p=0.00) |
| All economies | 10-40 | 97 | 0.281 [0.167, 0.395] (p=0.00) |
| All economies | 40-80 | 123 | 0.179 [0.059, 0.298] (p=0.00) |
| All economies | >80 | 249 | 0.271 [0.119, 0.423] (p=0.00) |
| Low and lower-middle income | <10 | 109 | 0.509 [0.171, 0.846] (p=0.00) |
| Low and lower-middle income | 10-40 | 36 | 0.359 [0.106, 0.612] (p=0.01) |
| Low and lower-middle income | 40-80 | 53 | 0.453 [0.080, 0.826] (p=0.02) |
| Low and lower-middle income | >80 | 35 | 1.367 [-0.005, 2.739] (p=0.05) |
| Upper-middle and high income | <10 | 77 | 0.234 [0.013, 0.455] (p=0.04) |
| Upper-middle and high income | 10-40 | 61 | 0.233 [0.093, 0.372] (p=0.00) |
| Upper-middle and high income | 40-80 | 70 | 0.120 [-0.008, 0.247] (p=0.07) |
| Upper-middle and high income | >80 | 214 | 0.159 [0.052, 0.266] (p=0.00) |

## A6 differences inside low and lower-middle income economies (mobile)

Sample: 62 economies, 233 observations. Each moderator is standardised and added to the mobile effect one at a time.

| Moderator (at start of period) | Interaction with +10 mobile (pp growth per SD) | Obs |
|---|---|---|
| secondary enrolment | 0.136 [-0.205, 0.478] (p=0.43) | 233 |
| electricity access | 0.024 [-0.301, 0.348] (p=0.89) | 224 |
| private credit | -0.074 [-0.295, 0.147] (p=0.51) | 204 |
| log GDP per capita | 0.237 [-0.128, 0.602] (p=0.20) | 233 |

## A2 predetermined (previous-period change), mobile subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 19 | 55 | -0.376 [-0.861, 0.109] (p=0.13) |
| Lower-middle | 42 | 143 | 0.260 [0.034, 0.486] (p=0.02) |
| Upper-middle | 51 | 160 | 0.005 [-0.147, 0.158] (p=0.95) |
| High | 64 | 219 | -0.156 [-0.281, -0.032] (p=0.01) |

With country fixed effects added: Low -0.509 (p=0.17); Lower-middle 0.369 (p=0.03); Upper-middle 0.067 (p=0.39); High -0.098 (p=0.15)

## A1 contemporaneous, internet users, % of population

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 18 | 53 | -0.916 [-3.241, 1.409] (p=0.44) |
| Lower-middle | 42 | 158 | 1.185 [0.348, 2.023] (p=0.01) |
| Upper-middle | 51 | 184 | 0.370 [-0.040, 0.779] (p=0.08) |
| High | 60 | 223 | -0.089 [-0.340, 0.162] (p=0.49) |

With country fixed effects added: Low -1.537 (p=0.13); Lower-middle 1.089 (p=0.12); Upper-middle 0.405 (p=0.12); High 0.032 (p=0.83)

## A2 predetermined (previous-period change), internet users, % of population

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 19 | 43 | -3.861 [-7.810, 0.088] (p=0.06) |
| Lower-middle | 41 | 127 | -0.399 [-1.202, 0.405] (p=0.33) |
| Upper-middle | 49 | 150 | -0.209 [-0.582, 0.165] (p=0.27) |
| High | 60 | 210 | -0.306 [-0.509, -0.102] (p=0.00) |

With country fixed effects added: Low -5.308 (p=0.08); Lower-middle -0.209 (p=0.71); Upper-middle 0.009 (p=0.97); High -0.205 (p=0.13)

## A1 contemporaneous, fixed broadband subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 17 | 34 | -21.426 [-27.860, -14.993] (p=0.00) |
| Lower-middle | 40 | 99 | 5.846 [2.454, 9.237] (p=0.00) |
| Upper-middle | 47 | 122 | 1.830 [0.623, 3.036] (p=0.00) |
| High | 62 | 192 | -0.057 [-0.589, 0.474] (p=0.83) |

With country fixed effects added: Low -34.200 (p=0.00); Lower-middle 6.767 (p=0.32); Upper-middle 1.330 (p=0.08); High -0.283 (p=0.56)

## A2 predetermined (previous-period change), fixed broadband subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 14 | 20 | 6.588 [-3.566, 16.742] (p=0.20) (fewer than 15 economies, not interpreted) |
| Lower-middle | 38 | 62 | -5.478 [-12.136, 1.179] (p=0.11) |
| Upper-middle | 42 | 83 | -0.928 [-1.826, -0.030] (p=0.04) |
| High | 60 | 138 | -0.094 [-0.767, 0.579] (p=0.78) |

With country fixed effects added: Low 11.040 (p=0.23); Lower-middle -2.148 (p=0.51); Upper-middle -0.590 (p=0.63); High -0.377 (p=0.57)

## A4 event study around the mobile takeoff (first year with at least 10 subscriptions per 100)

Economies below 10 per 100 in 1995: 190; of these 189 reach 10 by 2019. Window: 5 years before to 10 years after; reference year -1; stacked cohorts with clean controls (control economies reach 10 more than 10 years after the cohort year, or never by 2019); cohort-by-country and cohort-by-year fixed effects. Controls are drawn from the same income-group set as the treated economies (clarification of the spec). Outcome: log GDP per capita times 100, so a coefficient of 5 means GDP per capita about 5% higher than in the reference year, relative to controls.

| Sample | Treated economies | Control economies | Pre-trend (mean of -5 to -2) | Effect at +5 | Effect at +10 |
|---|---|---|---|---|---|
| All economies | 189 | 30 | -1.8 | 8.6 [-4.0, 21.2] | 8.9 [-13.4, 31.3] |
| Low and lower-middle income | 69 | 7 | 12.2 | -15.8 [-46.8, 15.3] | -18.2 [-69.0, 32.7] |
| Upper-middle income (controls from all income groups) | 56 | 10 | 0.1 | 6.3 [-14.3, 26.8] | 7.6 [-26.1, 41.2] |
| High income (controls from all income groups) | 64 | 30 | 2.3 | 6.3 [-7.4, 20.0] | 5.1 [-18.0, 28.2] |

Figure: `figures/event_study.png`. Panels with fewer than 15 treated economies are left empty.

## A5 secondary outcomes around the mobile takeoff (effect at +5 and +10 years)

| Outcome | Sample | Treated | Effect at +5 | Effect at +10 |
|---|---|---|---|---|
| Life expectancy (years) | All economies | 189 | -0.60 [-2.18, 0.98] | -0.89 [-3.21, 1.44] |
| Life expectancy (years) | Low and lower-middle income | 69 | -3.04 [-5.96, -0.12] | -3.58 [-6.99, -0.17] |
| Life expectancy (years) | Upper-middle income (controls from all groups) | 56 | -1.41 [-3.90, 1.08] | -1.21 [-4.29, 1.86] |
| Life expectancy (years) | High income (controls from all groups) | 64 | -0.98 [-2.25, 0.30] | -1.54 [-3.45, 0.37] |
| Under-5 mortality (log x 100) | All economies | 178 | 2.03 [-17.49, 21.55] | 0.45 [-24.32, 25.23] |
| Under-5 mortality (log x 100) | Low and lower-middle income | 69 | 26.79 [-18.84, 72.42] | 23.53 [-27.46, 74.52] |
| Under-5 mortality (log x 100) | Upper-middle income (controls from all groups) | 56 | 14.21 [-23.83, 52.25] | 9.78 [-32.49, 52.05] |
| Under-5 mortality (log x 100) | High income (controls from all groups) | 53 | -0.83 [-15.22, 13.57] | -1.76 [-21.96, 18.44] |
| Unemployment (pp) | All economies | 171 | -0.22 [-1.18, 0.73] | -0.34 [-1.39, 0.70] |
| Unemployment (pp) | Low and lower-middle income | 68 | -0.10 [-2.04, 1.84] | -2.28 [-3.84, -0.72] |
| Unemployment (pp) | Upper-middle income (controls from all groups) | 51 | 0.79 [-0.46, 2.03] | 0.40 [-1.18, 1.98] |
| Unemployment (pp) | High income (controls from all groups) | 52 | -0.49 [-1.55, 0.57] | -0.32 [-1.47, 0.83] |
| Agriculture share of value added (pp) | All economies | 178 | 2.28 [-0.31, 4.88] | 3.65 [-1.73, 9.03] |
| Agriculture share of value added (pp) | Low and lower-middle income | 66 | 5.81 [0.86, 10.77] | 11.48 [2.34, 20.61] |
| Agriculture share of value added (pp) | Upper-middle income (controls from all groups) | 55 | 1.38 [-3.04, 5.80] | 2.07 [-9.29, 13.44] |
| Agriculture share of value added (pp) | High income (controls from all groups) | 57 | 2.64 [0.19, 5.10] | 4.21 [-0.33, 8.75] |
| CO2 per capita (log x 100) | not available from the API | | | |
| Electric power use per capita (log x 100) | All economies | 136 | 4.39 [-2.16, 10.94] | 0.92 [-15.90, 17.75] |
| Electric power use per capita (log x 100) | Low and lower-middle income | 48 | 5.49 [-6.40, 17.37] | 4.12 [-24.14, 32.39] |
| Electric power use per capita (log x 100) | Upper-middle income (controls from all groups) | 43 | 1.64 [-5.47, 8.74] | -1.65 [-28.03, 24.72] |
| Electric power use per capita (log x 100) | High income (controls from all groups) | 45 | 4.48 [-2.68, 11.64] | 0.25 [-15.59, 16.09] |


# Results of the macro-panel analysis (spec: `spec.md`)

Data: World Bank WDI, 1995 to 2023. Exploratory associations, not causal effects. Income groups are the current World Bank classification. Coefficients are in percentage points of annual GDP-per-capita growth per 10-unit change in the technology measure, with 95% confidence intervals from standard errors clustered by country. Cells with fewer than 15 economies are marked and not interpreted.

## A1 contemporaneous, mobile subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 20 | 60 | 0.329 [-0.123, 0.782] (p=0.15) |
| Lower-middle | 42 | 166 | 0.344 [0.168, 0.521] (p=0.00) |
| Upper-middle | 51 | 186 | 0.053 [-0.048, 0.154] (p=0.31) |
| High | 61 | 227 | 0.134 [0.031, 0.238] (p=0.01) |

With country fixed effects added: Low 0.057 (p=0.82); Lower-middle 0.270 (p=0.01); Upper-middle 0.074 (p=0.16); High 0.152 (p=0.00)

## A3 dose-response by baseline mobile level (per 100 people at start of period)

| Sample | Baseline bin | Obs | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| All economies | <10 | 186 | 0.368 [0.211, 0.525] (p=0.00) |
| All economies | 10-40 | 95 | 0.243 [0.127, 0.359] (p=0.00) |
| All economies | 40-80 | 116 | 0.142 [0.028, 0.256] (p=0.01) |
| All economies | >80 | 242 | 0.145 [0.025, 0.266] (p=0.02) |
| Low and lower-middle income | <10 | 109 | 0.432 [0.108, 0.757] (p=0.01) |
| Low and lower-middle income | 10-40 | 35 | 0.272 [0.050, 0.493] (p=0.02) |
| Low and lower-middle income | 40-80 | 50 | 0.332 [0.048, 0.616] (p=0.02) |
| Low and lower-middle income | >80 | 32 | 0.546 [0.123, 0.969] (p=0.01) |
| Upper-middle and high income | <10 | 77 | 0.209 [-0.017, 0.435] (p=0.07) |
| Upper-middle and high income | 10-40 | 60 | 0.201 [0.059, 0.344] (p=0.01) |
| Upper-middle and high income | 40-80 | 66 | 0.089 [-0.042, 0.220] (p=0.18) |
| Upper-middle and high income | >80 | 210 | 0.077 [-0.033, 0.188] (p=0.17) |

## A6 differences inside low and lower-middle income economies (mobile)

Sample: 62 economies, 226 observations. Each moderator is standardised and added to the mobile effect one at a time.

| Moderator (at start of period) | Interaction with +10 mobile (pp growth per SD) | Obs |
|---|---|---|
| secondary enrolment | 0.055 [-0.156, 0.265] (p=0.61) | 226 |
| electricity access | -0.035 [-0.250, 0.180] (p=0.75) | 217 |
| private credit | -0.037 [-0.233, 0.159] (p=0.71) | 198 |
| log GDP per capita | 0.164 [-0.068, 0.397] (p=0.17) | 226 |

## A2 predetermined (previous-period change), mobile subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 19 | 54 | -0.408 [-0.870, 0.054] (p=0.08) |
| Lower-middle | 42 | 143 | 0.164 [-0.016, 0.344] (p=0.07) |
| Upper-middle | 51 | 160 | -0.047 [-0.195, 0.101] (p=0.53) |
| High | 62 | 217 | -0.187 [-0.302, -0.072] (p=0.00) |

With country fixed effects added: Low -0.517 (p=0.14); Lower-middle 0.281 (p=0.02); Upper-middle 0.022 (p=0.77); High -0.102 (p=0.15)

## A1 contemporaneous, internet users, % of population

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 18 | 53 | -0.343 [-1.571, 0.885] (p=0.58) |
| Lower-middle | 42 | 155 | 0.377 [0.126, 0.628] (p=0.00) |
| Upper-middle | 51 | 184 | 0.168 [-0.127, 0.463] (p=0.26) |
| High | 60 | 222 | -0.016 [-0.232, 0.201] (p=0.89) |

With country fixed effects added: Low -0.609 (p=0.27); Lower-middle 0.347 (p=0.04); Upper-middle 0.317 (p=0.08); High 0.088 (p=0.50)

## A2 predetermined (previous-period change), internet users, % of population

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 19 | 42 | -4.413 [-8.859, 0.032] (p=0.05) |
| Lower-middle | 41 | 127 | -0.443 [-1.139, 0.253] (p=0.21) |
| Upper-middle | 49 | 150 | -0.195 [-0.549, 0.160] (p=0.28) |
| High | 59 | 209 | -0.304 [-0.497, -0.110] (p=0.00) |

With country fixed effects added: Low -5.319 (p=0.07); Lower-middle -0.249 (p=0.66); Upper-middle 0.030 (p=0.91); High -0.162 (p=0.20)

## A1 contemporaneous, fixed broadband subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 16 | 30 | -34.577 [-44.946, -24.209] (p=0.00) |
| Lower-middle | 40 | 97 | 1.604 [0.630, 2.578] (p=0.00) |
| Upper-middle | 46 | 118 | 1.530 [0.713, 2.346] (p=0.00) |
| High | 59 | 189 | -0.129 [-0.754, 0.495] (p=0.68) |

With country fixed effects added: Low -45.135 (p=0.00); Lower-middle 0.583 (p=0.25); Upper-middle 1.530 (p=0.02); High -0.090 (p=0.80)

## A2 predetermined (previous-period change), fixed broadband subscriptions per 100

| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |
|---|---|---|---|
| Low | 14 | 19 | -116.272 [-321.204, 88.659] (p=0.27) (fewer than 15 economies, not interpreted) |
| Lower-middle | 38 | 62 | -4.147 [-9.249, 0.954] (p=0.11) |
| Upper-middle | 42 | 83 | -0.445 [-1.371, 0.481] (p=0.35) |
| High | 59 | 137 | -0.199 [-0.889, 0.491] (p=0.57) |

With country fixed effects added: Low 15.391 (p=0.50); Lower-middle -1.392 (p=0.72); Upper-middle 0.100 (p=0.93); High -0.289 (p=0.57)

## A4 event study around the mobile takeoff (first year with at least 10 subscriptions per 100)

Economies below 10 per 100 in 1995: 190; of these 189 reach 10 by 2023. Window: 5 years before to 10 years after; reference year -1; stacked cohorts with clean controls (control economies reach 10 more than 10 years after the cohort year, or never by 2023); cohort-by-country and cohort-by-year fixed effects. Controls are drawn from the same income-group set as the treated economies (clarification of the spec). Outcome: log GDP per capita times 100, so a coefficient of 5 means GDP per capita about 5% higher than in the reference year, relative to controls.

| Sample | Treated economies | Control economies | Pre-trend (mean of -5 to -2) | Effect at +5 | Effect at +10 |
|---|---|---|---|---|---|
| All economies | 189 | 30 | -1.8 | 8.6 [-4.0, 21.2] | 9.0 [-12.8, 30.8] |
| Low and lower-middle income | 69 | 7 | 12.2 | -15.8 [-46.8, 15.3] | -18.2 [-69.0, 32.7] |
| Upper-middle income (controls from all income groups) | 56 | 10 | 0.0 | 6.3 [-14.2, 26.8] | 7.5 [-25.3, 40.3] |
| High income (controls from all income groups) | 64 | 30 | 2.3 | 6.3 [-7.4, 20.0] | 5.1 [-18.0, 28.2] |

Figure: `figures/event_study.png`. Panels with fewer than 15 treated economies are left empty.

## A5 secondary outcomes around the mobile takeoff (effect at +5 and +10 years)

| Outcome | Sample | Treated | Effect at +5 | Effect at +10 |
|---|---|---|---|---|
| Life expectancy (years) | All economies | 189 | -0.60 [-2.18, 0.98] | -0.81 [-3.08, 1.47] |
| Life expectancy (years) | Low and lower-middle income | 69 | -3.04 [-5.96, -0.12] | -3.58 [-6.99, -0.17] |
| Life expectancy (years) | Upper-middle income (controls from all groups) | 56 | -1.41 [-3.90, 1.08] | -1.32 [-4.29, 1.65] |
| Life expectancy (years) | High income (controls from all groups) | 64 | -0.98 [-2.25, 0.30] | -1.54 [-3.45, 0.37] |
| Under-5 mortality (log x 100) | All economies | 178 | 2.03 [-17.49, 21.55] | 0.45 [-24.32, 25.23] |
| Under-5 mortality (log x 100) | Low and lower-middle income | 69 | 26.79 [-18.83, 72.42] | 23.53 [-27.46, 74.52] |
| Under-5 mortality (log x 100) | Upper-middle income (controls from all groups) | 56 | 14.21 [-23.83, 52.25] | 9.78 [-32.49, 52.05] |
| Under-5 mortality (log x 100) | High income (controls from all groups) | 53 | -0.83 [-15.22, 13.57] | -1.76 [-21.96, 18.44] |
| Unemployment (pp) | All economies | 171 | -0.22 [-1.18, 0.73] | -0.34 [-1.39, 0.70] |
| Unemployment (pp) | Low and lower-middle income | 68 | -0.10 [-2.03, 1.84] | -2.28 [-3.84, -0.72] |
| Unemployment (pp) | Upper-middle income (controls from all groups) | 51 | 0.79 [-0.46, 2.03] | 0.40 [-1.18, 1.98] |
| Unemployment (pp) | High income (controls from all groups) | 52 | -0.49 [-1.55, 0.57] | -0.32 [-1.47, 0.83] |
| Agriculture share of value added (pp) | All economies | 180 | 2.28 [-0.31, 4.88] | 3.65 [-1.73, 9.03] |
| Agriculture share of value added (pp) | Low and lower-middle income | 67 | 5.81 [0.86, 10.77] | 11.48 [2.35, 20.61] |
| Agriculture share of value added (pp) | Upper-middle income (controls from all groups) | 56 | 1.38 [-3.04, 5.80] | 2.07 [-9.29, 13.44] |
| Agriculture share of value added (pp) | High income (controls from all groups) | 57 | 2.64 [0.19, 5.10] | 4.21 [-0.33, 8.75] |
| CO2 per capita (log x 100) | not available from the API | | | |
| Electric power use per capita (log x 100) | All economies | 136 | 4.39 [-2.16, 10.94] | 0.92 [-15.90, 17.75] |
| Electric power use per capita (log x 100) | Low and lower-middle income | 48 | 5.49 [-6.39, 17.37] | 4.12 [-24.14, 32.39] |
| Electric power use per capita (log x 100) | Upper-middle income (controls from all groups) | 43 | 1.64 [-5.47, 8.74] | -1.65 [-28.03, 24.72] |
| Electric power use per capita (log x 100) | High income (controls from all groups) | 45 | 4.48 [-2.68, 11.64] | 0.25 [-15.59, 16.09] |


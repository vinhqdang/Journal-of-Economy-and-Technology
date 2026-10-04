# Additional research questions: results (exploratory)

Specified in `extra_questions_spec.md` before the analyses were run. Exploratory: no multiplicity correction, machine-extracted inputs (a random sample checked by the author by hand; see `data/human_check.md`). A single p-value below 0.10 among these tests is a hypothesis, not a finding.

## RQ2 to RQ4: extra moderators in the meta-regression

Same weighted regression as the pilot (147 estimates, 23 papers, standard errors clustered by paper), adding one variable at a time to `lowmid`, `gmm`, `mobile` and `internet`.

| Question | Added variable | Share of estimates with variable = 1 (or mean) | Coefficient | Clustered SE | p | Papers with variation |
|---|---|---|---|---|---|---|
| RQ2 measurement | composite index as exposure | 0.11 | 0.0570 | 0.0910 | 0.53 | 1 of 23 |
| RQ3 outcome form | growth-rate outcome | 0.38 | -0.0426 | 0.0894 | 0.63 | 1 of 23 |
| RQ4 time | sample midyear, centred (per year) | -0.00 | -0.0152 | 0.0071 | 0.03 | 22 of 22 |

A coefficient on `composite` or `growth` is the average difference in partial correlation relative to single-indicator or level estimates. Several papers contribute estimates with the same value of the added variable, so these tests rest on between-paper contrasts and are weak.

## RQ5: are weaker designs more common where low-income economies are sampled?

| Outcome | Studies listing a low-income economy | Studies not listing one | Odds ratio | Fisher p |
|---|---|---|---|---|
| No identification strategy (versus any) | 9 of 26 (35%) | 31 of 58 (53%) | 0.46 | 0.16 |
| Moderate risk of bias (versus serious or critical) | 3 of 26 (12%) | 7 of 58 (12%) | 0.95 | 1.00 |

26 of 84 studies list at least one low-income economy; studies that report no income coverage are counted as not listing one, which biases the comparison toward the second column.

## RQ6: does study quality go with the reported direction for output?

- all family-1 results positive: moderate-risk studies 1 of 3; serious or critical 10 of 46; odds ratio 1.80, Fisher p = 0.54.
- at least one negative or null family-1 result: moderate-risk studies 1 of 3; serious or critical 26 of 46; odds ratio 0.38, Fisher p = 0.58.

Base: 49 studies with at least one output or productivity result. Most studies report several results, so "all positive" is a demanding criterion.

## RQ7: which enabling conditions are tested, and in which direction?

| Moderator | Studies | Entries | Amplifies | Dampens | Mixed | Null | Unclear | Formally tested entries |
|---|---|---|---|---|---|---|---|---|
| other_country_characteristic | 32 | 39 | 4 | 8 | 19 | 2 | 6 | 18 |
| income_group | 27 | 30 | 8 | 7 | 8 | 5 | 2 | 6 |
| human_capital | 15 | 16 | 9 | 3 | 4 | 0 | 0 | 9 |
| infrastructure_connectivity | 10 | 10 | 5 | 2 | 2 | 0 | 1 | 6 |
| institutions_governance | 8 | 9 | 3 | 2 | 4 | 0 | 0 | 6 |
| trade_openness | 8 | 8 | 4 | 2 | 2 | 0 | 0 | 8 |
| sector_structure | 8 | 8 | 0 | 1 | 6 | 0 | 1 | 3 |
| financial_development | 6 | 6 | 2 | 1 | 2 | 0 | 1 | 4 |
| time_period | 5 | 5 | 0 | 1 | 3 | 1 | 0 | 0 |

165 heterogeneity entries from 84 studies; 34 are not moderation tests (robustness, control sensitivity or descriptive remarks) and are left out of the table. Classification by one model reader; a second reader classified a random 20% sample (n = 28) and agreed on the moderator type in 86% of entries (kappa 0.83), on the direction in 71% (kappa 0.64) and on whether the test was formal in 96% (kappa 0.93). Direction counts are therefore indicative only.

## RQ8: thresholds stated by the studies

| Study | Moderator | Stated threshold |
|---|---|---|
| 45 | other | 71.87 (DFI index in percent) |
| 126 | other | median (P50) split; no estimated threshold |
| 126 | human capital | median (P50) split of high-skilled share; no estimated threshold |
| 126 | other | split at 2009/2010 |
| 174 | other | LNTRADE = 4.737 (about 114% trade/GDP in levels if natural log; only about 4.5% of country-years above it by 2 |
| 174 | other | LNGVCP = -1.0710 (56 countries) |
| 174 | institutions | LNGOV = 2.9072 (about 50% of country-years above) |
| 174 | institutions | LNIT = -0.2166 (p < 0.10 only; about 85% of sample above) |
| 174 | other | AI quantiles Q50 and Q75 (values not reported) |
| 217 | other | 60% (median bank concentration) |
| 245 | other | about 0.6 (DE index) |
| 408 | human capital | HC index 2.352 (composite); 2.3 mobile; 2.4 internet users; 2.6 broadband |
| 408 | infrastructure | DE 81.3%; mobile 119.85%; internet users 52.34%; broadband 2.83% |
| 755 | other | c = 0.442 (Model 1, MTCO2PC), 0.441 (Model 2, CARIN), 0.358 (Model 3, GHG) in log FDIIF; slope gamma = 7.930,  |
| 755 | income group | see above |
| 879 | other | FDI 73.6% of GDP (sign change); GFCF none (-52.2, outside range) |
| 891 | other | 21.4 (Model B2); 43.3 as printed for Model A2 |
| 952 | infrastructure | 47.5% internet penetration |
| 957 | institutions | 88% private credit to GDP (fixed telephone, MENA); computed ratio is about 86.8 |
| 1372 | other | 3.5224 (virtual social network index); 2.4394 (internet in schools index) |
| 1419 | other | Mobile.Pay 15 (QGI Q90); Mobile.SR 40 (QGI Q10), 50 (QGI Q75); Gini Mobile.SR 32.18 (Q75); poverty Mobile.SR 1 |
| 1469 | other | 100 mobile subs per 100; internet 50% (primary), 65% (secondary) |
| 1494 | other | DIG = 0.48 (Gini), about 0.50 (Theil) |
| 1798 | institutions | 0.300 (voice and accountability), 0.300 (government effectiveness), 0.250 (rule of law); 2.500 (economic gover |
| 9106 | infrastructure | below-median baseline fixed telephone penetration |
| 9304 | other | 100 (mobile, TFP); 101.214-101.419 (mobile, welfare TFP); 15 (internet, welfare real TFP) |

Thresholds are in different units and rest on one study each. They are listed, not pooled. Where two studies state a threshold for the same variable they do not agree in an obvious way (human capital: composite index of 2.35 in Africa, median splits elsewhere).

## RQ9: evidence gap map (studies per outcome family and income-group coverage)

A study counts in every income group its sample lists. Studies that report no income coverage appear only in the last column.

| Outcome family | Low | Lower-middle | Upper-middle | High | Coverage not reported | Studies |
|---|---|---|---|---|---|---|
| Output and productivity | 16 | 16 | 15 | 30 | 13 | 49 |
| Structural change | 4 | 4 | 4 | 4 | 1 | 6 |
| Labour market | 3 | 5 | 6 | 11 | 2 | 14 |
| Poverty and distribution | 2 | 1 | 3 | 8 | 4 | 12 |
| Living standards | 5 | 5 | 5 | 9 | 5 | 16 |
| Resource cost | 2 | 1 | 2 | 6 | 0 | 6 |

## RQ10: AI stream versus historical-wave stream

| Measure | Historical waves (H) | AI (AI or both) |
|---|---|---|
| Moderate risk of bias | 8 of 69 (12%) | 2 of 15 (13%) |
| Critical risk of bias | 6 of 69 (9%) | 4 of 15 (27%) |
| No identification strategy | 31 of 69 (45%) | 9 of 15 (60%) |
| Compares income groups or regions | 30 of 69 (43%) | 6 of 15 (40%) |
| Lists a low-income economy | 24 of 69 (35%) | 2 of 15 (13%) |
| Median number of economies | 32 (n = 69) | 16 (n = 15) |
| Median first sample year | 2000 (n = 69) | 2012 (n = 15) |

Low-income coverage, AI against historical: Fisher p = 0.13. Counts are small (AI n = 15).


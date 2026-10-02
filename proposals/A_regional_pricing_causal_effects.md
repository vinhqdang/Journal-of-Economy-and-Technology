# Proposal A: Causal effects of regional pricing and free promotions on generative AI adoption

**Target journal:** Journal of Economy and Technology (JET), Research Article
**Author:** Quang-Vinh Dang, British University Vietnam, Hung Yen, Vietnam (vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024)
**Status:** idea stage, literature check done on 2 October 2026 (see section 3 for what was and was not read)

**Working title:** Price cuts into new markets: what localized low-price tiers and free promotions do to generative AI adoption in lower-income countries

**Keywords:** generative AI; regional pricing; price discrimination; difference-in-differences; technology adoption; digital divide

---

## 1. Why the earlier version was not enough

A first draft proposed a cross-country "hours of work needed to buy AI access" index. That is a descriptive purchasing-power exercise in the style of the Big Mac or iPhone index, and a referee would call it descriptive. The affordability index stays in this proposal only as a measurement section (section 6, step 1). The contribution is now a causal question with a theory-based welfare counterfactual.

## 2. Research questions

- **RQ1 (adoption effect).** How much does the launch of a localized low-price tier raise generative AI adoption in the countries that receive it, relative to countries that do not yet have it?
- **RQ2 (price response).** What is the implied response to price when a plan goes from a low price to zero (the free 12-month promotion in India)?
- **RQ3 (persistence).** Does usage persist after a promotion ends, or does it fall back? A 12-month promotion that began on 4 November 2025 ends in November 2026, so this can be observed.
- **RQ4 (heterogeneity).** Are effects larger in poorer countries, in countries with lower card penetration, or where local-currency payment was enabled?
- **RQ5 (welfare).** Under a simple third-degree price discrimination model, when does regional pricing raise both provider profit and total welfare?

## 3. Positioning and what was checked

| Source | What it shows | Read in detail? |
|---|---|---|
| [CNBC, 9 Oct 2025](https://www.cnbc.com/2025/10/09/openai-expands-its-cheapest-chatgpt-plan-to-16-more-countries-in-asia.html) | ChatGPT Go expanded from India and Indonesia to 16 more Asian countries, with local-currency payment in some. | Search snippet only |
| [TechCrunch, 27 Oct 2025](https://techcrunch.com/2025/10/27/openai-offers-free-chatgpt-go-for-one-year-to-all-users-in-india) and [Medianama](https://www.medianama.com/2025/10/223-openai-chatgpt-go-free-indian-users/) | Free ChatGPT Go for 12 months to all users in India, claimable from 4 Nov 2025. | Search snippet only |
| [Rest of World, 2026](https://restofworld.org/2026/countries-generative-ai-adoption/) and the Microsoft Global AI Adoption report | Cross-country adoption statistics, candidate validation data. | Not read |
| "The Price of Intelligence" (arXiv 2608.29843) | Quality-adjusted price indices for API services, list prices, no country dimension. | Read |
| "LLeMpower" (arXiv 2404.09356) | Cross-sectional access disparities. | Abstract only |

No peer-reviewed event study of regional pricing for generative AI turned up in the searches. That is weak evidence of a gap. The search must be repeated in Google Scholar, SSRN and NBER before the project starts. Facts taken from news items must be re-confirmed from primary sources (provider announcements and help-centre pages), including the claim that the plan went global at USD 8 on 15 January 2026, which so far comes only from a third-party price guide.

## 4. Identification strategy

Treatment events (to be confirmed from primary sources):

| Date | Event | Treated units |
|---|---|---|
| Aug 2025 | Low-price tier launched | India |
| Sep 2025 | Same tier | Indonesia |
| 9 Oct 2025 | Expansion | 16 further Asian countries, including Vietnam |
| 4 Nov 2025 | Free 12-month promotion | India (second treatment, price to zero) |
| Jan 2026 | Global rollout (to be verified) | Remaining countries, which ends the clean not-yet-treated window |
| Nov 2026 | Promotion expires | India (persistence test) |

Design: staggered adoption with not-yet-treated and never-treated countries as controls. Estimators that are robust to heterogeneous timing: Callaway and Sant'Anna, Sun and Abraham, and synthetic difference-in-differences. Pre-trend tests plus HonestDiD sensitivity bounds.

Cross-provider triple difference: competing services that did not change price in the treated countries act as a placebo and as a substitution check. A rise in the treated provider's outcome with no change for rivals points to the price channel. A rise for all providers points to a general demand shock.

Threats and responses:

- **Few, clustered treated units (mostly Asia).** Wild cluster bootstrap and randomization inference. Report the number of effective clusters.
- **Concurrent shocks** (model releases, school calendars, telecom bundles, rival promotions). Date-by-date event windows, rival-service placebos, a log of known concurrent events kept from the start.
- **Proxy outcomes, not paid conversions.** Stated openly. See section 5.
- **One provider only.** Extend to other providers' regional launches if dates can be documented. Present external validity as a limitation.

## 5. Data

Outcomes are proxies for adoption, because subscriber counts by country are not public.

1. Google Trends, within-country relative interest in the service and in rivals, weekly. Each series is normalised within country and compared only in changes.
2. Web traffic estimates by country from public traffic-estimation tools, and app-store ranking snapshots from archived pages.
3. If budget allows, commercial app-download estimates by country.
4. Survey-based adoption data (Microsoft report, other cross-country surveys) as validation of the proxy, not as the main outcome.
5. Covariates: GNI per capita (PPP), internet and mobile penetration, card penetration, English proficiency, exchange rates.

A company statement that paid subscribers in India doubled after launch is a company-reported figure and is not used as an outcome.

Timing matters. The promotion in India ends in November 2026. Weekly data collection and archiving of pricing pages should start now and be pre-registered, so the persistence test has a clean pre-specified design.

## 6. Method

1. **Measurement (context section).** Capability-adjusted affordability burden by country and date, using published quality-adjusted price indices as inputs. This section is descriptive and kept short.
2. **Event studies and staggered DiD** for RQ1, RQ3 and RQ4.
3. **Price response.** Compare the move from the paid tier to zero in India with the earlier low-price launch, using the proxy outcomes. Report it as a bounded range, not a point elasticity.
4. **Price discrimination model.** Two-market monopoly with a global price versus separate prices. State the Varian and Schmalensee conditions: total welfare rises only if total output rises. Calibrate with the estimated adoption effect and test sensitivity.
5. **Welfare counterfactual.** Compare consumer surplus and profit under uniform global pricing, regional pricing and free promotion.

## 7. Expected contributions

- First quasi-experimental evidence on regional pricing for generative AI services, with a persistence test around a promotion's end.
- A transparent, replicable pipeline that others can extend as more providers localise prices.
- A welfare statement tied to estimated effects instead of assumed ones.

## 8. Main risks

| Risk | Consequence | Mitigation |
|---|---|---|
| Proxy outcomes are noisy | Wide confidence intervals | Several independent proxies, report agreement across them, state limits |
| Treated countries are not comparable to controls | Biased estimates | Synthetic DiD, covariate-conditional parallel trends, rival-service placebo |
| Promotion in India overlaps other offers | Cannot isolate the price effect | Log concurrent offers, use event windows, treat India as a case study |
| Another group publishes first | Loses novelty | Pre-register and post a working paper early |

## 9. Plan (about 6 months)

| Month | Work |
|---|---|
| 0 | Start weekly data collection and archiving, pre-register the design |
| 1 | Confirm event dates from primary sources, finish literature search |
| 2 | Build the country-week panel |
| 3 | Event-study and DiD estimates, placebo and robustness checks |
| 4 | Persistence analysis after the November 2026 expiry |
| 5 | Price discrimination model and welfare counterfactual |
| 6 | Writing, replication package, JET submission |

## 10. JET submission notes

Structured abstract of about 300 words, no more than 6 keywords, author-date references, data availability statement with a public replication package, competing-interest declaration and a generative-AI disclosure if any tool is used for language editing. Check the current article processing charge. The guide for authors lists USD 500 with a waiver for submissions before 31 December 2025, a date that has passed.

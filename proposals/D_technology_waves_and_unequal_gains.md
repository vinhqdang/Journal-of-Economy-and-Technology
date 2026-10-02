# Proposal D: Is AI another internet? Technology waves, adoption gradients and the distribution of gains across 150+ economies

**Target journal:** Journal of Economy and Technology (JET), Research Article
**Author:** Quang-Vinh Dang, British University Vietnam, Hung Yen, Vietnam (vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024)
**Status:** question framing and literature scan, 2 October 2026. The research questions below come from the author's own question and are open for confirmation.

**Working title:** Is AI another internet? Adoption gradients, payoffs and who gains from successive technology waves, 1975–2026

**Keywords:** general-purpose technology; technology diffusion; generative AI; economic growth; income divergence; cross-country panel; machine learning

---

## 1. The question as the author posed it

How have economies operated over the last 50 years as technology changed? Is AI like the internet, like Bitcoin, like deep learning? Does the effect differ between economies, and if so why? Will a rich economy such as the United States, a developing one such as Vietnam, or a poor one such as Cambodia gain more from AI?

Design decisions taken so far:

- **Scale:** as many economies as data allow, in the hundreds if possible, not three case studies. Realistically about 150–190 economies for the main variables.
- **Mechanisms:** all plausible factors are put in together (human capital, digital and electric infrastructure, compute access, sector structure, institutions and regulation, trade integration, language), and the data decide which matter.
- **Outcomes:** not yet fixed. Proposed default: output per capita growth and total factor productivity as primary, poverty and inequality as secondary. Open to change.

## 2. Research questions

- **RQ1 (similarity of waves).** How does the relationship between income and technology penetration evolve in the years after each wave starts? Is AI's adoption gradient closer to mobile phones, to the internet and broadband, or to crypto-assets?
- **RQ2 (payoffs).** Historically, for a given amount of adoption, were growth, productivity, poverty and inequality outcomes better in high-, middle- or low-income economies?
- **RQ3 (mechanisms).** Which country characteristics explain the differences in RQ1 and RQ2, and how stable is that ranking across methods and periods?
- **RQ4 (AI).** Applying the estimated patterns, which types of economies are predicted to gain most from generative AI, and do the early adoption data (2023–2026) agree? Present United States, Vietnam and Cambodia as worked examples, not as the basis of the claim.

## 3. Positioning and what was checked

| Source | What it shows | Gap this paper addresses | Read in detail? |
|---|---|---|---|
| Comin and Hobijn, "An Exploration of Technology Diffusion" | 15 technologies, 166 countries, 1820–2003. Average adoption lag of 47 years. Technology adoption differences account for at least 25% of cross-country income differences. | Older technologies. Does not cover generative AI, crypto or deep learning. | Search snippet only |
| Comin and Mestieri, "If Technology Has Arrived Everywhere, Why Has Income Diverged?" | Adoption lags have converged, but penetration gaps between rich and poor countries have widened. Average adoption intensity in non-Western countries about 47% of the Western level. | The key reference to test against AI: does the intensity gap repeat, shrink, or grow faster? Data end before the AI era. | Search snippet only |
| IMF, "Gen-AI: Artificial Intelligence and the Future of Work" (SDN/2024/001) and the AI Preparedness Index | Exposure about 60% of jobs in advanced economies, 40% in emerging markets, 26% in low-income countries. Preparedness index covers 174 economies across four areas. | Exposure and preparedness today, no historical comparison and no estimated payoffs. Indices usable as mechanism inputs. | Snippets only |
| Microsoft, "Global AI Adoption in 2025: A Widening Digital Divide" | Adoption in the Global North roughly twice that of the Global South, with the gap widening below about USD 20,000 income per capita. | One source, one measurement method. Needs validation against other sources. | Snippet only |
| Statements that AI spreads faster than earlier technologies, with paid subscriptions more evenly spread across income groups than the internet at a similar stage | Early adoption looks faster and, within some countries, flatter by income. | Needs checking at source. The origin of this comparison was not clear in the search results. | Snippets only |
| World Bank, World Development Report 2026 on AI for development; Brookings, "The Next Great Divergence"; OECD, "Emerging divides in the transition to AI" | Policy and descriptive treatments of a possible new divergence. | Descriptive. No common cross-wave method and no estimated heterogeneity. | Titles and snippets only |

Not yet looked for, and needed before submission: the general-purpose technology literature (for example work on electricity and ICT productivity lags and on whether machine learning is a general-purpose technology), the leapfrogging literature (for example mobile phones in low-income countries), and cross-country evidence on internet and broadband effects on growth. The current claim of novelty is therefore provisional.

What looks open from this scan: a single method applied to several waves (mobile, internet and broadband, smartphones, crypto, AI) including post-2003 waves, outcomes beyond income, mechanism ranking with many candidates, a back-tested forecast, and a test against early AI data.

## 4. Technology waves and how each is measured

| Wave | Penetration measure | Years | Caveat |
|---|---|---|---|
| Mobile phones | Subscriptions per 100 people (ITU, World Bank WDI) | 1985– | Long, good coverage |
| Internet and broadband | Users per 100, fixed and mobile broadband (ITU, WDI) | 1990– | Long, good coverage |
| Smartphones and mobile data | Mobile broadband subscriptions, smartphone share | about 2008– | Coverage thinner for poor countries |
| Crypto-assets | Published adoption indices and exchange-flow measures | about 2015–, coverage mainly from 2019 | Short, partly proprietary, adoption can be speculative and not productive |
| Deep learning | Not a consumer product. Proxy by research output, patents and industrial robot density by country | 2012– | A proxy for capability and diffusion, not a penetration rate. Treated separately |
| Generative AI | Country-level usage measures from published reports and independent sources, population-normalised | 2022– | Short, few sources, measurement differs by source. Cross-validate before use |

Crypto and deep learning are included as contrasts on purpose. They test whether the pattern in the results is about technologies that raise productivity throughout the economy, or about any new technology.

## 5. Data

1. **Diffusion:** ITU and WDI for mobile, internet and broadband. The Comin–Hobijn cross-country adoption dataset for long histories, after checking which recent technologies it covers. Published AI-usage data and independent proxies such as Google Trends interest by country.
2. **Outcomes:** Penn World Table (output, productivity, human capital), WDI, World Bank Poverty and Inequality Platform, WIID, and sector data (GGDC and UNIDO) for the subset of countries that have them.
3. **Mechanisms:** IMF AI Preparedness Index components, electricity access, schooling attainment, governance indicators, trade openness, economic complexity, English proficiency, mobile and broadband prices, compute access measures if available.
4. **Sample:** all economies with usable data for at least a core set of variables, reporting the number of countries per analysis. Missingness is patterned (poorer countries have less data), so results are reported on the full unbalanced sample and on a balanced subsample.

## 6. Method

1. **Adoption gradients (RQ1).** For each wave and each year since launch, estimate the cross-country slope of log penetration on log income, and a dispersion measure. Plot the gradient against years since launch for all waves on one axis. Compare AI's early path with the early paths of the others.
2. **Payoffs (RQ2).** Country-year panel of growth, productivity, poverty and inequality on adoption intensity, with country and year fixed effects, and interactions between adoption and income group and between adoption and each mechanism. For identification, use instruments that predate the adoption decision, such as distance to submarine-cable landing points and pre-existing fixed-line stock interacted with the global fall in technology prices. A sector-level design of the Rajan–Zingales type (sectors that depend more on the technology, in countries with better enabling conditions) wherever sector data exist.
3. **Mechanism ranking (RQ3).** With many candidate factors and limited waves, use several methods and report agreement: Bayesian model averaging (posterior inclusion probabilities), post-double-selection LASSO, causal forests for heterogeneous effects, and stability selection. These rank candidate mechanisms. They do not establish causation on their own.
4. **Forecast and back-test (RQ4).** Estimate on the early waves, predict the heterogeneity in a later wave (for example the smartphone and broadband era) and score the forecast. Only a method that passes the back-test is applied to AI. Report prediction intervals, not point forecasts. Compare with early AI adoption and exposure data.
5. **Falsification.** Check that crypto adoption does not show productivity payoffs similar to the productivity-enhancing waves. If it did, something is wrong with the design.

## 7. Expected contributions

- A common-metric comparison of successive technology waves, extended to the AI era and to non-productive contrasts.
- Evidence on whether the historical pattern, where arrival converges but intensity diverges, repeats with AI.
- A ranked and stress-tested list of country characteristics behind unequal gains, from many candidates, not a few assumed ones.
- A back-tested, uncertainty-aware statement about which kinds of economy are positioned to gain from AI, with Vietnam, Cambodia and the United States as examples.

## 8. Risks and limits

| Risk | Mitigation |
|---|---|
| Cross-country growth regressions are fragile and endogenous | Fixed effects, pre-determined instruments, sector designs where possible, many robustness specifications, report fragility openly |
| AI outcomes are not observable yet (2022 onward) | RQ4 is a conditional forecast, labelled as such. Causal claims limited to earlier waves |
| Only a handful of technology waves | Treat waves as the unit for RQ1 and avoid strong generalisation. Use country-level variation for RQ2–RQ3 |
| AI adoption data come from few sources with different methods | Use several sources, check agreement, report results by source |
| Missing data for the poorest countries | Report coverage, balanced and unbalanced results, bounds for selection |
| Machine-learning rankings can be unstable | Stability selection, agreement across methods, back-testing |
| Crypto and deep learning are not like the others | Used as contrasts with their own measures, not forced into one metric |

## 9. Plan (about 8 months)

| Month | Work |
|---|---|
| 1 | Complete the literature search, read all snippet-only sources, confirm outcome measures with the author |
| 2 | Assemble diffusion, outcome and mechanism data, check coverage |
| 3 | Adoption-gradient analysis across waves (RQ1) |
| 4–5 | Payoff and heterogeneity estimation (RQ2) |
| 6 | Mechanism ranking and robustness (RQ3) |
| 7 | Back-test and AI forecast, country examples (RQ4) |
| 8 | Writing, replication package, JET submission |

## 10. Relation to the other proposals

Proposal A (regional pricing) zooms in on one price lever for access to generative AI. This proposal sets the wider historical and cross-country frame. A could be a later paper or a case within D's mechanism section. B and C are archived.

## 11. JET submission notes

Structured abstract of about 300 words, at most 6 keywords, author-date references, data and code availability statement (all inputs public, replication package in a public repository), competing-interest declaration, and a generative-AI disclosure if any tool is used for language editing. Confirm the current article processing charge, since the waiver in the guide for authors ended on 31 December 2025.

# Manuscript Proposal for the Journal of Economy and Technology (JET)

**Working title:** Cheaper intelligence, unequal access? A capability-adjusted, PPP-based affordability index of generative AI services across countries, 2023–2026

**Proposed author:** Quang-Vinh Dang, British University Vietnam, Hung Yen, Vietnam
(vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024)

**Proposed article type:** Research Article (structured abstract of about 300 words, up to 6 keywords)

**Keywords:** generative AI; affordability; purchasing power parity; price discrimination; digital divide; technology diffusion

---

## 1. One-paragraph pitch

Posted prices of large language model (LLM) services have fallen sharply, and recent work shows that quality-adjusted prices fall faster still. A falling world price does not mean that access is becoming more equal. What a household or firm can actually buy depends on local income, local pricing practice (regional discounts, free tiers, taxes, payment frictions) and the quality gap between free and paid tiers. This paper builds the first time-varying *affordability index* for generative AI that combines (i) a capability-adjusted price of AI services, (ii) purchasing-power-parity (PPP) and wage data, and (iii) country-specific consumer and API price schedules. It asks whether the cross-country affordability gap is converging or diverging, and which mechanisms (regional pricing, open-weight models, free tiers) close it.

## 2. Why this fits JET

JET's scope covers "the economic, managerial and policy implications of technology development" and "computer and information technologies with strong applications in economics and management." This idea sits on both sides of that line.

- It applies standard price-measurement economics (hedonic and matched-model indices, PPP conversion, price discrimination theory) to a new technology good.
- It needs data engineering and statistical modelling (price-history scraping, benchmark-based capability estimation).
- It speaks to policymakers, which is one of JET's stated audiences.

Recent JET papers cover AI regulation, algorithmic bias, sentiment models for economic decisions and technology adoption in developing economies. This one adds a measurement-and-welfare view of AI access.

## 3. Novelty check and positioning

A short literature search was done on 2 October 2026. It must be repeated in full before submission.

| Related work | What it does | What it leaves open (this paper's contribution) |
|---|---|---|
| "The Price of Intelligence: A Quality-Adjusted Price Index for AI Services" (arXiv 2608.29843) | Builds quality-adjusted API price indices from about 21,000 price observations (Feb 2024–Aug 2026). Finds that quality-adjusted prices fall about 0.73 log points a year, against about 0.10 for unadjusted token prices. | Covers list prices of API providers in one market. Does not address cross-country affordability, PPP, consumer subscription tiers, or regional pricing. |
| Bajari et al., "Hedonic prices and quality adjusted price indices powered by AI" (J. Econometrics, 2025; arXiv 2305.00044) | Uses AI (transformers) to estimate hedonic prices for ordinary goods. | Concerns AI as a *tool* for price measurement, not AI services as the *good* being priced. |
| "LLeMpower: Understanding Disparities in the Control and Access of Large Language Models" (arXiv 2404.09356) | Documents concentration of LLM ownership and economic capacity across nations. | Cross-sectional and capacity-focused. It is not a time-varying, capability-adjusted measure of end-user affordability. |

An earlier idea, a pure quality-adjusted price index for LLM APIs, was dropped. The first source above already occupies that space. The PPP and affordability dimension is the open niche.

## 4. Research questions and hypotheses

- **RQ1 (level).** In 2026, how many hours of local median labour income buy a fixed bundle of AI capability (for example, a fixed volume of tasks at a fixed quality level) in each country?
- **RQ2 (trend).** Between 2023 and 2026, did cross-country dispersion in that affordability burden narrow (sigma-convergence) or widen?
- **RQ3 (mechanisms).** How much of the gap is closed by (a) regional or PPP-linked pricing, (b) free tiers, (c) open-weight models served by cheap third-party providers, and (d) local-currency and payment frictions?
- **RQ4 (welfare).** What is the implied consumer-surplus or access loss if low-income countries can only use models a fixed number of capability steps behind the frontier?

Hypotheses:

- **H1.** Capability-adjusted world prices fall fast, but the affordability burden of *frontier* access falls much more slowly in lower-middle-income countries because consumer subscription prices are sticky and mostly USD-denominated.
- **H2.** The free-tier and open-weight capability gap, not the price gap, is the binding constraint for low-income users.
- **H3.** Regional pricing narrows the burden only where firms have adopted it. Adoption is predicted by market size and piracy or substitution risk, as in standard third-degree price-discrimination models.

## 5. Data (all public or reproducible)

1. **Price histories.** Provider pricing pages via Internet Archive snapshots, public pricing JSON repositories with git history, and aggregator price tables. Consumer subscription prices by country, collected from app-store and web pricing pages (including taxes) at several dates.
2. **Capability measures.** Public benchmark scores and arena-style ratings, combined into a latent capability score (item response theory or a factor model), with robustness to benchmark choice.
3. **Macro and labour data.** World Bank ICP PPP conversion factors, GNI per capita (Atlas and PPP), IMF exchange rates, ILO median or mean wages, ITU data on internet affordability.
4. **Token-consumption per task.** A small benchmark task set run through a sample of models to measure tokens used, including hidden reasoning tokens. This converts per-token prices into per-task prices.

## 6. Methods

1. **Capability-adjusted price.** Hedonic regression and a chained matched-model index, following the standard price-index literature. The paper builds on published indices and does not claim to invent the index.
2. **Affordability burden.** For country *c* and date *t*, the burden is *B_ct* = (local price of the reference bundle at capability level *k*) / (local median income per hour), reported both at market exchange rates and PPP.
3. **Convergence analysis.** Sigma- and beta-convergence of log *B_ct* across countries. Panel regressions with country and time fixed effects. Event-study design around documented regional-pricing launches, for example staggered rollout of local pricing in specific countries.
4. **Mechanism decomposition.** Oaxaca–Blinder or Shapley-style decomposition of the burden gap into price, income, tier-availability and capability-ceiling components.
5. **Welfare bounds.** Compare consumer surplus under frontier access with surplus under lagged-capability access. Use a simple CES or logit-demand model with parameters taken from the literature, with sensitivity analysis.
6. **Vietnam case study.** Vietnam is the home setting of the author. It also gives a concrete lower-middle-income to upper-middle-income example, covering local-currency prices, payment methods and wage levels. A comparison with a handful of peer economies is added.

## 7. Expected contributions

- A reproducible, open dataset and code for a cross-country AI affordability index, updated as new data arrive.
- Evidence on whether falling AI prices are reducing or reinforcing the global digital divide.
- A policy-relevant decomposition: which levers (regional pricing, open-weight availability, connectivity subsidies) move access most.
- A methodological bridge between the AI-price-index and digital-divide literatures.

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Consumer price data by country are patchy. | Use a fixed set of 25–40 countries, record collection dates, report coverage, run robustness checks on subsets. |
| Capability is multidimensional and benchmarks are contaminated. | Report indices under several benchmark sets and exclude benchmarks flagged as problematic. |
| Prices change faster than review cycles. | Fix a data cut-off date, archive all raw snapshots, give a replication package. |
| Overlap with the preprint above. | Cite and build on it. Frame the contribution as affordability and distribution, not price-index construction. |
| Welfare section relies on assumed elasticities. | Present it as bounds with transparent sensitivity analysis. |

## 9. Work plan (about 6 months)

| Month | Milestone |
|---|---|
| 1 | Full literature review; pre-register definitions of the reference bundle and burden metric; set up data collection |
| 2 | Collect price and capability data; build the capability score |
| 3 | Construct the index; run the token-per-task experiment |
| 4 | Convergence and event-study analysis |
| 5 | Mechanism decomposition, welfare bounds, Vietnam case study |
| 6 | Writing, replication package, submission to JET |

## 10. Submission checklist for JET

- Structured abstract of about 300 words and no more than 6 keywords.
- Author-date references, sorted alphabetically and then chronologically.
- Data availability statement with the replication package deposited in a public repository.
- Declaration of competing interests, plus a disclosure of any generative-AI use for language editing, as the journal policy requires.
- Check the current article processing charge. The guide for authors lists USD 500, with a waiver for submissions before 31 December 2025. That date has passed, so confirm the current terms.

## 11. Alternative ideas, if this one is not chosen

1. **Reproducibility audit for ML in economics.** Re-run a sample of recent "ML applied to socioeconomic data" papers with released data and measure how often the reported gains survive simple baselines and leakage-free validation.
2. **Hidden-cost economics of reasoning models.** Per-task cost of reasoning models versus non-reasoning models, and what it means for firm-level adoption decisions.
3. **Strategic pricing among AI providers.** Test for tacit coordination or competitive responses in API price changes using event-study methods on price-change histories.

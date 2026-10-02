# Proposal C: When does AI pay? Task-level cost-effectiveness of generative AI, wage levels, and the distribution of growth and living-standard gains across countries

**Target journal:** Journal of Economy and Technology (JET), Research Article
**Author:** Quang-Vinh Dang, British University Vietnam, Hung Yen, Vietnam (vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024)
**Status:** idea stage, literature scan done on 2 October 2026 (see section 3 for what was and was not read)

**Working title:** When does AI pay? Cost-effectiveness thresholds, wage levels, and who gains from generative AI

**Keywords:** generative AI; task-based growth; cost-effectiveness; wages; productivity; living standards; cross-country evidence

---

## 1. The question

Two quantities are said to drive what AI does to growth and to ordinary people: how *good* AI is (efficiency, reliability) and how *much it costs* per unit of work. Most macro work on this assumes a task-level cost saving and then aggregates it. This paper puts the cost side at the centre. A task is worth giving to AI only if the cost of an AI-produced unit, including the human review that is still needed, is below the cost of the human-produced unit. Human cost depends on the local wage. AI cost is roughly the same everywhere. So the *same* global fall in AI prices makes different tasks, occupations and countries cross the threshold at different dates, and the gains in growth and living standards are spread unevenly as a result.

## 2. Research questions

- **RQ1 (threshold).** For each country and year in 2023–2026, what share of the wage bill sits in tasks where AI is cost-effective, and how does that share vary with the wage level?
- **RQ2 (price versus reliability).** Which matters more for the cost-effective share and for the implied growth gain: falling prices per token, or rising reliability that cuts the human review needed per task?
- **RQ3 (prediction).** Does the cost-effective share predict *realised* AI adoption and early productivity changes better than exposure alone does?
- **RQ4 (distribution).** Under explicit price and reliability scenarios to 2032, how are the gains in real wages and output per worker distributed across countries and across wage groups within a country?

## 3. Positioning and what was checked

| Source | What it does | Gap | Read in detail? |
|---|---|---|---|
| Acemoglu, "The Simple Macroeconomics of AI" (NBER w32487) | Task-based aggregation. Reported upper bound of about 0.66% total factor productivity gain over ten years. | Takes the task-level cost saving as given. No cost threshold that varies with wages. | Search snippet only |
| Svanberg, Li, Fleming, Goehring and Thompson, "Beyond AI Exposure: Which Tasks are Cost-Effective to Automate with Computer Vision?" | Static cost-effectiveness model for computer vision in the US. Reports that about 23% of vision-task wages are attractive to automate at then-current costs. | Computer vision, one country, one date. Not language models, not a falling price, not cross-country. | Search snippet only |
| "Economic Evaluations of Language Models" (arXiv 2607.19375) | Builds task-level time-saving measures for US occupations. | Does not compare AI cost with wages by country or occupation and does not link to growth or living standards. Stated as such in its own scope. | Read |
| "The Price of Intelligence" (arXiv 2608.29843) | Quality-adjusted price indices for AI services. | Prices only. No wage comparison, no growth link. | Read |
| "Mind the Gap: AI Adoption in Europe and the U.S." (NBER w34995) | Industries with higher AI adoption show faster productivity growth, in Europe and the US. | Associations with adoption. Covers Europe and the US. No cost threshold. | Snippet only; the file was too large to fetch |
| EIB Working Paper 2026/02, "AI adoption, productivity and employment: Evidence from European firms" | Firm-level study of about 12,000 European firms, productivity gain of about 4%. | Europe, adoption-based. | Snippet only |
| ILO WP 140 (2025), "Generative AI and jobs: a refined global index of occupational exposure" | Exposure scores for ISCO-08 four-digit occupations. | Exposure only, not cost-effectiveness. Usable as an input. | Snippet only |
| Epoch AI, "The plunging price of thought", and "The Price of Progress" (arXiv 2511.23455) | Price per unit of benchmark performance falling roughly 5 to 10 times a year. | Price trend only. | Snippets only |
| EPRI and arXiv 2606.19777, "Have Data Centers Raised Your Electric Bill?" | Finds lower average residential rates on average in the US, with regional heterogeneity. | A possible input for the resource-cost extension in section 6. | Snippet only |

No paper that combines the three elements (language-model cost per task, wage-based thresholds, and a cross-country time path) turned up. That is weak evidence of a gap. Repeat the search in Google Scholar, SSRN, NBER and RePEc before starting. Every snippet-only row must be read in full before it is cited in a manuscript.

## 4. Model sketch

For task bundle *k* in occupation *o*, country *c* and year *t*:

- Human cost per unit: H = w(o,c,t) × h(k), where h is human time per unit and w is the fully loaded wage.
- AI cost per unit: A = [p(t) × n(k) + ρ(k,t) × w(o,c,t) × h(k) + F(k) / V(k)] / q(k,t), where
  - p(t) is the capability-adjusted price per token,
  - n(k) is tokens per attempt, including hidden reasoning tokens,
  - ρ is the share of human time still needed for review and correction,
  - F / V is fixed integration cost spread over task volume,
  - q is the success probability per attempt.
- A task is cost-effective if A ≤ (1 − δ) H, where δ is a switching margin.
- The per-task saving is s = 1 − A / H when cost-effective and 0 otherwise.
- Aggregate gain for country *c* follows the Hulten-style sum of wage-bill shares × exposure × saving, as in the task-based macro literature.

Implications to be derived formally, not assumed:

1. The cost-effective share of the wage bill rises with the wage and with the fall of p(t). Low-wage economies cross the threshold later.
2. Because ρ scales with the wage, there is a floor on the saving: once AI tokens are cheap, the unautomated review step dominates, and further price falls have a shrinking effect (a Baumol-type bottleneck). Reliability gains, not price falls, then drive the remaining gains.
3. Within a country the first tasks to cross the threshold are high-wage cognitive tasks, which differs from the routine-task pattern of earlier automation. The distributional prediction follows.

## 5. Data

1. **Exposure and tasks.** ILO four-digit ISCO-08 exposure scores, and task descriptions mapped to ISCO.
2. **Wages by occupation and country.** ILOSTAT earnings by occupation (usually at one- or two-digit ISCO), national statistics where available, and PPP conversion factors. Resolution is coarser than the exposure data. Imputation and its error are reported.
3. **AI prices.** Published quality-adjusted price series, plus provider price histories archived from public pages.
4. **Tokens and success per task.** A small task benchmark, built by the author and mapped to ISCO tasks, run on several models. It measures tokens per attempt (hidden reasoning tokens included), success rates and review time assumptions. The benchmark and prompts are released.
5. **Realised adoption.** Cross-country worker and firm AI-use surveys, such as those cited in the studies above, and any public national surveys. Country coverage will be uneven.
6. **Productivity.** EU KLEMS and OECD industry-level data for the countries that have them, up to the latest release.

## 6. Method

1. **Build the threshold panel** for 40–60 countries and 2023–2026. Report the share of the wage bill that is cost-effective under a base case and under a grid of δ, ρ, F and q.
2. **Decompose** changes in the cost-effective share into price, reliability, wage growth and exchange-rate or PPP components (RQ2).
3. **Horse race for prediction (RQ3).** Regress realised adoption on exposure alone, on cost-effective share alone and on both, with income, internet penetration and sector mix as controls. Use occupation-level variation within countries where data allow. For productivity, use an industry-by-country panel, with the within-industry change in the predicted gain as regressor. The time window is short, so this part is described as exploratory and its specification is pre-registered.
4. **Scenarios for RQ4.** Combine the threshold model with a standard task-based aggregation. Scenarios: price keeps falling at the recent pace, price decline slows, reliability improves faster or slower. Report ranges, not point forecasts.
5. **Resource-cost extension.** Add a shadow cost of electricity and compute to p(t), using published estimates, to show how sensitive the thresholds are to costs that today's prices may not reflect.
6. **Vietnam and peer economies** as a worked example, since Vietnam is the author's setting and sits in a wage range where the threshold dates matter.

## 7. Expected contributions

- A measurement of *when AI becomes economically worth using* by country, not only whether tasks are technically exposed.
- A clean statement of whether price or reliability is the binding margin, which is directly useful for policy on compute subsidies versus evaluation and assurance.
- A distributional account of who gains first, from the wage side.
- A released benchmark and panel that others can extend.

## 8. Risks and limits

| Risk | Mitigation |
|---|---|
| Time window of 2023–2026 is too short for strong growth effects | State it. Treat the productivity test as exploratory. Lean on the threshold measurement and scenarios, not on a headline growth coefficient |
| Occupation wages are coarse in many countries | Use two-digit ISCO, report imputation error, show results for countries with finer data separately |
| Exposure scores come from model-based scoring and may be biased | Report results under alternative exposure measures and with exposure held out |
| Task benchmark may not represent real work | Document construction, publish it, run with several models and report dispersion |
| Many assumptions drive scenarios | Show full sensitivity grids, publish code, avoid point predictions |
| Crowded topic | Keep the contribution tight: the cost threshold across wage levels, price versus reliability, and the cross-country time path |

## 9. Plan (about 7 months)

| Month | Work |
|---|---|
| 1 | Full literature search, read all snippet-only sources, fix model and notation |
| 2 | Build exposure, wage and price inputs, design the task benchmark |
| 3 | Run the benchmark, estimate tokens and success rates |
| 4 | Construct the threshold panel, decomposition |
| 5 | Adoption and productivity tests |
| 6 | Scenarios, resource-cost extension, Vietnam example |
| 7 | Writing, replication package, JET submission |

## 10. Relation to the other proposals

Proposal A (regional pricing) studies *consumer access* and prices. This proposal studies *enterprise and labour substitution* and the growth consequences. They share the price series and country panel, so they can be run as one research programme. The earlier proposal on verifiable billing (B) has been archived.

## 11. JET submission notes

Structured abstract of about 300 words, at most 6 keywords, author-date references, data and code availability statement, competing-interest declaration, and a generative-AI disclosure if a tool is used for language editing. Confirm the current article processing charge, since the waiver in the guide for authors ended on 31 December 2025.

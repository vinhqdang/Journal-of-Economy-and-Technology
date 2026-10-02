# Proposal B: Who pays for proof? Certification, reputation and regulation in markets for opaque LLM inference

**Target journal:** Journal of Economy and Technology (JET), Research Article (theory with calibration)
**Author:** Quang-Vinh Dang, British University Vietnam, Hung Yen, Vietnam (vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024)
**Status:** idea stage, literature check done on 2 October 2026

**Working title:** Who pays for proof? Certification, reputation and regulation in markets for opaque LLM inference

**Keywords:** LLM pricing; hidden reasoning tokens; verifiable inference; certification; mechanism design; market structure

---

## 1. Honest status of the idea

The first version of this idea was "moral hazard in per-token billing of hidden reasoning tokens". That version is largely taken. The literature check found:

- A formal principal-agent analysis of token misreporting, with results on incentive-compatible pricing.
- A contract-design model where an agent chooses both a model and a token budget.
- Security-style papers that propose and attack auditing schemes for hidden tokens.

What is left is the market and institutional level. The two formal papers listed below say explicitly that they stay at the micro level, with one buyer and one provider, and leave out competition, reputation, regulation and welfare comparisons of remedies. This proposal targets that gap. It is narrower than the original idea, it is theory-heavy, and its novelty margin depends on proving results that the micro-level papers do not contain.

## 2. Research questions

- **RQ1 (voluntary certification).** If providers can adopt costly verifiable-inference technology (for example hardware attestation or proofs of inference) and signal it to users, does certification unravel, so that all honest providers certify and non-certification signals opportunism? How does the answer depend on the verification cost?
- **RQ2 (market structure).** Verification has a fixed cost. Do small providers, such as local hosts of open-weight models, exit or get locked out, and does the market concentrate?
- **RQ3 (remedies compared).** Compare the welfare of: opaque per-token pricing, mandated certification, pay-per-character or other incentive-compatible pricing, per-task fixed prices with a warranty, and regulatory audits with penalties.
- **RQ4 (reputation).** When can repeated interaction and reputation replace verification, and when does it fail, for example when users cannot judge quality or cost per task?

## 3. Positioning

| Source | What it does | Gap it leaves | Read in detail? |
|---|---|---|---|
| "Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives" (arXiv 2505.21627) | Principal-agent model of token misreporting. Shows only pay-per-character is incentive-compatible among additive schemes. | Micro level only. No competition, reputation, regulation or welfare comparison. Verification infrastructure left open. | Yes |
| "Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice" (arXiv 2608.18232) | Linear contract with hidden model choice and token budget. | One principal and one agent. Verification cost only as a constant in an appendix. No market or regulation. | Yes |
| "Token Inflation: How Dishonest Providers Can Overcharge for Large Language Model Usage" (arXiv 2605.30040) | Attacks three auditing schemes. Hidden reasoning usage can be inflated heavily without detection. | Security analysis, no economic model. | Yes |
| CoIn (arXiv 2505.13778), PALACE (arXiv 2508.00912), "Invisible Tokens, Visible Bills" (arXiv 2505.18471) | Auditing methods and a call to audit. | Technical, not economic. | Search snippets only |
| "Menu Pricing of Large Language Models" and "Token Allocation, Fine-Tuning and Optimal Pricing" (Cowles Foundation discussion papers) | Pricing theory for LLM services. | Whether they address verification and certification must be checked. | Titles only, not read |

Unread items must be read before any claim of novelty is written into a manuscript.

## 4. Model sketch

- **Players.** A continuum of users and several providers. Providers have a private type: honest or opportunistic (willing to inflate billed usage if undetected). The fraction of each type is common knowledge.
- **Technology.** Verification costs a fixed amount F and a variable amount v per unit of usage. It makes billed usage verifiable. Heterogeneous F captures that small providers face a higher relative cost.
- **Users.** Observe the certification status and the price. They cannot observe true usage without verification. They choose a provider, or exit.
- **Provider moves.** Choose price, whether to certify, and (if opportunistic and not certified) an inflation level with a detection probability that rises with inflation.
- **Regulator (RQ3).** Can mandate certification, impose audits with a penalty, or mandate a pricing format.

Targeted results (to be proved, not assumed):

1. A threshold on F and v below which full certification is an equilibrium, and a region with partial certification.
2. Conditions under which mandated certification lowers welfare because it removes small providers.
3. Conditions under which per-task pricing with a warranty substitutes for verification.
4. The comparison of remedies in welfare terms and in market concentration.

## 5. Calibration and checks

Public inputs: posted API prices, the number of independent providers hosting the same open-weight model on public aggregators, reported shares of reasoning tokens from published studies, and published estimates of inflation under the attacks above. These calibrate the simulations. The paper does not claim any provider overcharges. It analyses incentives and institutions, and states this plainly.

No new access to proprietary APIs is needed. If some empirical test is added later (for example price dispersion for the same model across providers), it is a secondary exhibit.

## 6. Contribution

- Moves the discussion from "can providers cheat" to "which institutions make honest billing an equilibrium, and who bears the cost".
- Gives policy-relevant comparisons for regulators and standard setters, which is a JET audience.
- Links to Proposal A: both concern who gets access to AI and on what terms. Small and local providers are the ones most exposed to verification fixed costs.

## 7. Risks

| Risk | Mitigation |
|---|---|
| Novelty margin is thin if the micro-level authors extend their own work | Post a working paper early, focus on market-level theorems that the micro models cannot deliver |
| Pure theory may be harder to place | Keep the calibration and a clear policy table. JET has published game-theoretic work on contract design |
| Results depend on modelling choices | State assumptions, show robustness to alternative detection functions and cost structures |
| Could be read as accusing providers | Frame it as an incentive analysis. Report the honest-provider case and the benchmark with no inflation |

## 8. Plan (about 6 months)

| Month | Work |
|---|---|
| 1 | Read the unread items, full literature search, fix the model |
| 2 | Solve the baseline equilibrium and the certification threshold |
| 3 | Market structure and entry results |
| 4 | Remedy comparison and welfare |
| 5 | Calibration and robustness |
| 6 | Writing, code release, JET submission |

## 9. JET submission notes

Same checklist as Proposal A: structured abstract of about 300 words, at most 6 keywords, author-date references, data and code availability statement, competing-interest declaration and a generative-AI disclosure if a tool is used for language editing. Confirm the current article processing charge.

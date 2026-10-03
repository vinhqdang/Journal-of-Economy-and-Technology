# Systematic review protocol (PRISMA-P 2015 structure)

**Title:** Do the gains from digital and general-purpose technology waves differ by a country's income level and enabling conditions? A systematic review of cross-country evidence on mobile, internet, ICT, crypto-assets and artificial intelligence, 1995–2026

**Registration:** to be registered on OSF before the search is run. PROSPERO is restricted to health-related reviews, so OSF is the intended venue. Registration needs the author's own account.
**Version:** 1.0 draft, 2 October 2026
**Linked proposal:** [proposals/D_technology_waves_and_unequal_gains.md](../proposals/D_technology_waves_and_unequal_gains.md). This review is the evidence-synthesis stage of that project.

## Administrative information

| # | Name | Affiliation | Role | Contact |
|---|---|---|---|---|
| 1 | Quang-Vinh Dang | British University Vietnam, Hung Yen, Vietnam | Guarantor and lead reviewer | vinh.dq4@buv.edu.vn, ORCID 0000-0002-3877-8024 |
| 2 | To be recruited | | Second reviewer (strongly recommended, see section "Study records") | |

**Amendments** (each logged with date, section and reason):

| # | Date | Section | Change | Reason |
|---|---|---|---|---|
| 1 | 2026-10-02 | Search strategy | Boolean query written with explicit phrase variants (OpenAlex does not allow wildcards inside quoted phrases) and restricted to the Economics, Econometrics and Finance field | Unrestricted query returned about 7,600 records, too many for one screener. Content of the four blocks is unchanged |
| 2 | 2026-10-02 | Study records | Four holding categories added at abstract stage: context (diffusion, adoption determinants, models; supports RQ1), environmental-outcome-only (low priority), review (for backward citation search), supplementary micro evidence | Many relevant records are not eligible payoff studies but are needed for RQ1 and for citation chasing |
| 3 | 2026-10-02 | Information sources | arXiv attempted but not completed. Scopus, Web of Science and EconLit not yet searched | Service time-out; institutional access needed |
| 4 | 2026-10-02 | Study records | Automated stage-1 rules added before manual reading. Single assisted screener, verification sample of 90 for the author | No second screener available |
| 5 | 2026-10-02 | Full-text stage | Included records ranked into tier A (80) and tier B (167) to decide which paywalled papers to request first | Ranking by income-level, threshold, convergence and AI cues plus citation count; used only to prioritise the request list |
| 6 | 2026-10-02 | Full-text stage | Records with no free full text and not on the short request list are kept as an abstract-level evidence map: study characteristics and the headline direction are recorded from the abstract and flagged, but they are excluded from pooled estimates and from risk-of-bias ratings, and certainty for them is rated very low | About 160 papers are paywalled; asking the author to retrieve all of them is not workable |
| 7 | 2026-10-03 | Full-text stage | Papers whose only available venue the author judged unreliable after visiting the journal site are not read at full text and are not used as evidence (idx 153 and 892). Source quality is checked at this point for every paper, not only at the venue-flag stage | The venue-quality screen is a stated criterion; a manual look at the journal is more reliable than the automated flag |
**Support:** no external funding declared. **Role of funder:** none.
**Use of AI tools:** screening and extraction are planned with automated assistance. The exact wording of the disclosure, required by the journal's policy on generative AI, is to be completed by the author before submission.

## Rationale

Existing work gives pieces of the answer. Long-run studies of technology adoption find that the *arrival* of technologies converged across rich and poor countries while the *intensity* of use diverged. Policy reports describe adoption gaps and exposure for AI. What is missing is a structured synthesis of the empirical cross-country evidence on whether the *payoffs* of successive digital waves differed by income level and by enabling conditions, across more than growth, and with the AI evidence placed beside the evidence from earlier waves. A systematic review is justified because the primary studies use different technology measures, outcomes, samples and identification strategies, and a transparent, reproducible search and appraisal is needed before any conclusion about AI is drawn from them.

An earlier literature scan (2 October 2026) found no systematic review with this scope, but that scan used web searches only and has to be repeated in the full search below, including a search for existing systematic reviews and meta-analyses on ICT and growth.

## Objectives (PICOS, adapted to macro-economic evidence)

- **P (Population):** national economies (all income levels), or groups of economies within multi-country samples.
- **I/E (Exposure):** adoption or diffusion of one of: ICT in general, mobile telephony, internet and broadband, smartphones and mobile data, crypto-assets, artificial intelligence (including machine learning, deep learning and generative AI).
- **C (Comparator):** lower versus higher adoption, or one income group or enabling-condition group versus another.
- **O (Outcomes):** six families, one primary indicator each (see below).
- **S (Study design):** quantitative empirical studies with a stated identification or estimation strategy: panel regressions, instrumental variables, difference-in-differences and event studies, structural estimation, growth accounting, and meta-analyses.

**Review question:** In empirical cross-country studies of digital and general-purpose technology waves, do the effects on output, structural change, labour markets, distribution, living standards and resource use differ by income level and by country characteristics, how large are the differences, and how does the evidence on AI compare with that on earlier waves?

Two evidence streams are kept apart in every table:

- **Stream H (historical waves):** ICT, mobile, internet and broadband, smartphones, crypto-assets.
- **Stream AI:** AI, machine learning, deep learning, generative AI. AI evidence is young and mostly not cross-country, so this stream has relaxed eligibility (below).

## Eligibility criteria

| Criterion | Include | Exclude |
|---|---|---|
| Study design | Quantitative empirical studies and meta-analyses with a stated estimation strategy | Opinion pieces, editorials, purely conceptual papers, case descriptions without estimation, simulation-only studies with no empirical calibration |
| Sample (Stream H) | At least 10 economies, or an explicit comparison of income groups | Single-country and few-country studies |
| Sample (Stream AI) | At least 3 economies, or an explicit comparison across income levels | Single-country firm or worker studies are not synthesised. Those in low- and middle-income settings are listed separately as supplementary evidence |
| Publication date | 1 January 1995 to the search date | Before 1995 (before the internet became a mass technology). Older technology history is covered by the prior long-run studies cited in the rationale |
| Language | English | Other languages (a limitation, see below) |
| Publication status | Peer-reviewed articles, and working papers from named series (NBER, IMF, World Bank, CEPR, OECD, UNCTAD, ITU). Preprints from repositories flagged as lower tier | Conference abstracts, blog posts, press articles, consultancy reports without methods |
| Exposure | One of the technologies above, measured as adoption, diffusion, investment or capability | Technology as a control only, or digitisation of a single sector with no adoption measure |
| Outcome | At least one outcome from the six families | None of the six |

### Outcomes

| Family | Primary indicator (fixed in advance) | Examples of secondary indicators |
|---|---|---|
| 1. Output and productivity | GDP per capita growth | Total factor productivity, labour productivity |
| 2. Structural change | Employment share of services | Manufacturing share, digitally delivered services exports |
| 3. Labour market | Employment rate | Informality, youth unemployment, labour share, skill premium |
| 4. Poverty and distribution | Gini coefficient | Poverty headcount, top 10% and bottom 40% income shares |
| 5. Living standards beyond income | Household consumption per capita | Life expectancy, schooling, financial inclusion |
| 6. Resource cost | Electricity use per capita | Carbon intensity of output, external balance |

Time points: the horizon at which the effect is reported (contemporaneous, medium run, long run) is recorded for each estimate.

## Information sources

| Source | Access | Role |
|---|---|---|
| Scopus | Institutional access (author exports results) | Main multidisciplinary database |
| Web of Science Core Collection | Institutional access (author exports results) | Second main database, citation tracking |
| RePEc / IDEAS and EconLit | Open (RePEc), institutional (EconLit) | Economics-specific coverage and working papers |
| OpenAlex | Open, needs a free personal API key because the shared quota is exhausted | Open database, reproducible counts, links to open-access full text |
| NBER, IMF, World Bank, CEPR, OECD, UNCTAD, ITU working-paper series | Open | Grey literature, reduces publication bias |
| Backward and forward citation search of all included studies and of the benchmark set | Open and institutional | Finds studies missed by keywords |
| Search for existing systematic reviews and meta-analyses | Same databases | Checks whether the review question has been answered |

At least two databases are searched, as the method requires. Search date and the number of records from each source are recorded for the PRISMA 2020 flow diagram.

## Search strategy (draft, to be calibrated on a pilot)

Four concept blocks, combined with AND, searched in title, abstract and keywords.

```
Block A (technology):
  "information and communication technolog*" OR ICT OR internet OR broadband
  OR "mobile phone*" OR "mobile telephon*" OR smartphone* OR "digital technolog*"
  OR "digital economy" OR "artificial intelligence" OR "machine learning"
  OR "deep learning" OR "generative AI" OR "large language model*"
  OR "general purpose technolog*" OR "general-purpose technolog*"
  OR cryptocurrenc* OR bitcoin OR "crypto-asset*" OR blockchain

Block B (economy level):
  countr* OR "cross-country" OR "cross country" OR nation* OR "developing econom*"
  OR "emerging econom*" OR "low-income" OR "middle-income" OR "high-income"
  OR "income group*" OR "developed econom*" OR "advanced econom*"

Block C (outcomes):
  growth OR productivity OR GDP OR poverty OR inequality OR employment OR wage*
  OR "labor share" OR "labour share" OR "structural transformation"
  OR "financial inclusion" OR welfare OR "living standard*" OR "human development"

Block D (heterogeneity):
  heterogene* OR "absorptive capacity" OR complementar* OR threshold
  OR "human capital" OR "digital divide" OR convergence OR divergence
  OR "technology diffusion" OR "technology adoption" OR leapfrog*

Combined: A AND B AND C AND D
Filters: 1995 to search date; English; articles, reviews, working papers
```

Database syntax (field tags for Scopus `TITLE-ABS-KEY(...)` and Web of Science `TS=(...)`) is generated from the same blocks. If the first run returns far too many records, Block D is made stricter and subject-area filters are added, with each change logged. The strategy is reviewed against the PRESS checklist before the final run.

**Recall check.** A benchmark set of known relevant papers is used to test that the search finds what it should. Items confirmed to exist so far: Comin and Hobijn, "An Exploration of Technology Diffusion"; Comin and Mestieri, "If Technology Has Arrived Everywhere, Why Has Income Diverged?"; the IMF staff discussion note "Gen-AI: Artificial Intelligence and the Future of Work". Further candidates, to be confirmed before use: studies of broadband and growth in OECD countries, of fast internet arrival in African countries, and of mobile phones and markets in low-income settings. If the search misses a benchmark paper, the strategy is revised.

## Study records

- **Management:** a spreadsheet or reference manager with record IDs. Deduplication by DOI, then by normalised title and year, followed by a manual check.
- **Screening:** title and abstract first, then full text. The screening decisions are made with automated assistance by applying the eligibility table. **The author verifies every included record and every uncertain record, and a random 10% sample of the excluded records at title and abstract stage.** Agreement between the assisted decisions and the author's decisions is reported (Cohen's kappa). A second human reviewer is strongly recommended for the full-text stage. Where none is available, this is declared as a limitation.
- **Pilot:** 50 records screened first to calibrate the criteria, then the criteria are frozen.
- **Documentation:** every exclusion at full text has a coded reason. Counts feed a PRISMA 2020 flow diagram.
- **Full-text access:** papers that cannot be opened are listed with links so that the author can download them through institutional access. Studies without full text are not assessed from the abstract.

## Data collection and data items

An extraction form is piloted on 3–5 studies, then frozen.

| Category | Items |
|---|---|
| Study | Authors, year, outlet and tier (peer-reviewed, working paper, preprint), funding, conflicts |
| Technology | Which wave, how adoption was measured, level of measurement |
| Sample | Number and names of economies, years, income-group definition, panel structure |
| Design | Estimator, identification strategy (instrument, event timing, none), controls, fixed effects |
| Outcome | Family, indicator, horizon |
| Result | Coefficient or elasticity, standard error or interval, sample size, sign, significance |
| Heterogeneity | Interaction terms and subgroup results by income, human capital, infrastructure, institutions, sector structure, language, other |
| Thresholds | Reported cut-off values for enabling conditions |
| Robustness | Number of specifications reported, whether the headline result is the preferred one |

Missing or unclear items are marked as such and not imputed. Authors are not contacted unless an estimate cannot be interpreted without it.

## Risk of bias assessment

RoB 2 and ROBINS-I were built for trials and for non-randomised studies of interventions. They fit cross-country macro studies poorly. This protocol therefore uses a **ROBINS-I-style tool adapted to cross-country observational studies**, and says so as a deviation from the standard tools. Domains:

1. Confounding and reverse causation (is adoption treated as exogenous, and is there a credible instrument or timing design?).
2. Measurement of exposure (does the adoption measure capture use or only access or investment?).
3. Selection of countries and years (missing data patterns, survivorship).
4. Measurement of outcomes (quality of the national statistics used).
5. Model specification and researcher degrees of freedom (number of specifications, sensitivity).
6. Selective reporting.

Each domain is rated low, moderate, serious or critical, with a short justification. Results appear as a traffic-light table. They feed a sensitivity analysis that drops studies at serious or critical risk.

## Data synthesis

- **Feasibility.** Estimates are pooled only when at least 10 estimates share a comparable exposure and outcome definition and can be put on a common scale (for example an elasticity). Otherwise the synthesis is narrative, following the SWiM guideline, with effect-direction plots.
- **Model.** Random-effects meta-regression. Estimates are nested within studies, so standard errors are clustered by study (robust variance estimation) or a multilevel model is used.
- **Heterogeneity.** Q, I-squared, tau-squared and a prediction interval.
- **Pre-specified subgroups and moderators:** income group, technology wave, identification strategy, period, publication tier.
- **Sensitivity analyses:** leave-one-study-out, exclude serious or critical risk of bias, exclude working papers, alternative income classification.
- **Software:** R (metafor and related packages).
- **Publication bias.** Funnel plots and precision-effect tests (PET and PEESE) where at least 10 estimates exist. Selective reporting is checked by comparing working-paper and published versions where both exist.

## Confidence in the evidence

GRADE adapted to observational macro evidence. Evidence starts low for non-randomised designs and is moved up for large effects or consistent dose-response patterns, and down for risk of bias, inconsistency, indirectness (especially for extrapolating earlier waves to AI), imprecision and publication bias. Certainty is rated separately for the Stream H and Stream AI findings.

## Known limitations of this design (internal check, not an independent review)

| Issue | Handling |
|---|---|
| Question is broad, with many technologies and outcomes | Two streams, six outcome families, one primary indicator each, pre-specified subgroups. If the pilot shows the corpus is unmanageable, narrow by technology and log it as an amendment |
| Technologies differ in kind (crypto and deep learning are not consumer goods) | Exposure measure recorded per study. Pooling only within comparable definitions |
| No second human screener yet | Declared. Verification sample and agreement statistics. Second reviewer recommended |
| Standard bias tools do not fit macro studies | Adapted tool, declared as a deviation |
| AI evidence is thin and recent | Separate stream, narrative synthesis expected, certainty rated separately, no extrapolation without a stated link to earlier waves |
| English only | Declared limitation, risk of missing regional literature |
| Cross-country growth regressions are fragile | Fragility is a finding to report, with specification counts and bias ratings |
| Meta-analysis may not be feasible | Narrative synthesis is a planned fallback and not a failure |

## Plan

| Step | Output |
|---|---|
| Author confirms this protocol | Confirmed version 1.0 |
| Register on OSF | Registration ID, added to this file |
| Pilot search and recall check | Calibrated strategy, amendment log |
| Run searches in at least two databases | Records per source and the exported files |
| Deduplicate and screen titles and abstracts | Screening log, kappa |
| Full-text list and access links | List of papers the author needs to download |
| Full-text screening, extraction, bias assessment | Extraction sheet, traffic-light table |
| Synthesis and GRADE | Tables, plots, certainty ratings |
| Write the PRISMA 2020 report | Manuscript section and appendices |

## Revision log

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-10-02 | Quang-Vinh Dang | Initial draft |

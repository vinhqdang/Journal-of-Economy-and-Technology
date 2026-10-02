# PRISMA 2020 flow (pilot run, 2 October 2026)

Status: **no study has been included yet.** The counts below stop at the full-text request stage. Nothing has been assessed at full text, and no data have been extracted.

| Stage | n | Note |
|---|---|---|
| Records identified, OpenAlex | 1,840 distinct (1,841 rows) | Protocol Boolean query, restricted to the Economics, Econometrics and Finance field (amendment 1) |
| Records identified, Crossref | 1,285 distinct (2,880 rows) | 96 technology-by-context queries, journal articles from 1995 |
| Records identified, NBER working papers | 579 distinct (2,671 rows) | Same 96 queries, from 1995 |
| Records identified, arXiv | 0 | **Attempted, not completed.** The service did not respond in a usable time and the job was stopped |
| Records identified, Scopus, Web of Science, EconLit | 0 | **Not yet run.** Needs institutional access |
| Distinct records before cross-source deduplication | 3,704 | |
| Duplicates removed across sources | 92 | DOI, then normalised title and year |
| Records after deduplication | 3,612 | |
| Excluded by automated rules (stage 1) | 1,545 | No eligible technology term 897, no outcome term 474, no multi-economy or heterogeneity cue 174 |
| Records read at title level | 2,067 | 365 of them had no abstract and were judged on title only |
| Excluded at title level | 1,611 | Includes 374 removed by a title rule (single-country name or clearly off-topic word, with no multi-economy cue) |
| Records assessed at abstract level | 456 | 71 had no abstract |
| Excluded at abstract level | 121 | Reasons coded: E1 single or fewer than 10 economies, E2/E3 exposure or outcome not eligible, E4 conceptual, review or theory without own estimation |
| Duplicates found at abstract level (preprint and published versions) | 8 | |
| Set aside as context (diffusion, adoption determinants, models) | 46 | New category, amendment 2 |
| Set aside, environmental outcome only (low priority) | 22 | New category, amendment 2 |
| Set aside as reviews, for backward citation search | 9 | New category, amendment 2 |
| Set aside as supplementary micro evidence (field experiments, firm studies) | 3 | New category, amendment 2 |
| **Sent to full-text assessment** | **247** | 80 in tier A (priority), 167 in tier B. 44 of the 247 were judged on title only |
| Full texts retrieved automatically | 29 of 256 (included plus reviews) | Open-access links only |
| Full texts still needed from the author | 227 | See the request lists |

## Screening method and its limits

- One assisted screener (automated rules plus a single reader). **No independent second screener, so no agreement statistic yet.** A random verification sample of 90 decisions is in `data/verification_sample.csv` for the author to check. Agreement will be reported once it is returned.
- Title screening was generous (the aim was not to lose relevant records). Abstract screening applied the eligibility table in the protocol.
- Source tiers: a few open-access links point to journals that have not been checked against predatory-journal lists. That check belongs to the full-text stage.

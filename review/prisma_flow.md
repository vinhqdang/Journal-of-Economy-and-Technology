# PRISMA 2020 flow (updated 4 October 2026)

Status: counts for the main search (OpenAlex, Crossref, NBER) are in the first table and the full-text stage is at the end; records from the supplementary Google Scholar search are listed in a separate table because they entered outside the main flow.

| Stage | n | Note |
|---|---|---|
| Records identified, OpenAlex | 1,840 distinct (1,841 rows) | Protocol Boolean query, restricted to the Economics, Econometrics and Finance field (amendment 1) |
| Records identified, Crossref | 1,285 distinct (2,880 rows) | 96 technology-by-context queries, journal articles from 1995 |
| Records identified, NBER working papers | 579 distinct (2,671 rows) | Same 96 queries, from 1995 |
| Records identified, arXiv | 0 | **Attempted, not completed.** The service did not respond in a usable time and the job was stopped |
| Records identified, Scopus, Web of Science, EconLit | 0 | **Not run.** Needs institutional access |
| Records identified, Google Scholar | Supplementary, reported separately below | Added on 4 October after a first-page check showed that the main search had missed relevant studies |
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
| **Sent to full-text assessment** | **247** | 80 ranked as tier A for priority, 167 as tier B. 44 of the 247 were judged on title only |
| Full texts retrieved automatically and verified against title | 72 of 256 (included plus reviews) | Open-access links, repository copies, preprints, publisher pages |
| Full texts requested from the author | 25 | Short list in `fulltext_requests.md` |
| Without full text, kept at abstract level only | 151 | Flagged, not pooled, no bias rating (amendment 6) |

## Supplementary Google Scholar search (not part of the counts above)

| Stage | n | Note |
|---|---|---|
| Queries run, first page each (pasted by the author) | 4 queries (G1, G2, G4, G7), 40 results | The other eleven queries (`google_scholar_queries.md`) have not been run |
| Results not among the 3,612 records | 29 | `data/scholar_g1_page1.csv`, `scholar_g2_page1.csv`, `scholar_g4_page1.csv`, `scholar_g7_page1.csv` |
| Results already among the 3,612 records but removed by the stage-1 rule or never read | 2 | Yin and Choi 2023 (stage-1 rule); Gonzales 2023 (no free full text at the time) |
| Obtained and read at full text | 20 | 9101 to 9106, 9201 to 9204, 9301 to 9305, 9401 to 9404 and 1580; free full texts supplied by the author |
| Not obtained (G1) | 3 | Chavula 2013, Torero et al. 2006, Omer and Ghanim 2026 (a preprint; the published version was read) |
| Included | 17 | 9202 (five countries), 9301 (a mathematical model) and 9403 (simulated panel only) were excluded at full text; study 9401 is kept on its generic ICT index because it never measures AI; all verified by the second pass |

The twenty read studies are counted in the full-text stage below. The first pages of four queries are not a search: they show that the main search had low recall, and they suggest that the remaining queries would add more. The author and the reviewer agreed to stop requesting from Google Scholar after G7.

## Screening method and its limits

- One assisted screener (automated rules plus a single reader). **No human second screener.** A blind model re-screening of a random sample of 340 records gave 79% agreement at the abstract stage (kappa 0.59) and suggests that screening missed records (see `rescreening.md`). A random verification sample of 90 decisions is in `data/verification_sample.csv` for the author to check. Agreement will be reported once it is returned.
- Title screening was generous (the aim was not to lose relevant records). Abstract screening applied the eligibility table in the protocol.
- Source tiers: a few open-access links point to journals that have not been checked against predatory-journal lists. That check belongs to the full-text stage.

## Full-text stage (updated)

| Stage | n | Note |
|---|---|---|
| Full texts read | 132 | 132 files received; 0 was the wrong document (idx 242) and needs re-retrieval |
| Excluded at full text | 43 | E1 14, E2 5, E3 1, E4 23 |
| Context only (no payoff outcome estimated) | 1 | |
| **Included, preliminary** | **88** | Machine-extracted, quotes partly verified, see `extraction_summary.md`. 40 are flagged for human check |


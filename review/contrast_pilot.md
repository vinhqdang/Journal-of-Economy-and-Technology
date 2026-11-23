# Within-study income contrasts: pilot results (23 Nov 2026)

Data: `data/contrasts_all.json` (coded contrasts), `data/new_studies.json` (new records), `data/contrast_verification.json` (second check against full texts). Analysis: `scripts/contrast_meta.py`; output in `contrast_pilot_output.txt`. Screening of the new searches: `data/round2_screening.csv`. Full texts still needed: `fulltext_needed_round2.md`.

## Searches added
- Backward and forward citation search in OpenAlex from 32 studies with income comparisons and Stanley et al. (2018): 3,595 new records, 667 after rules, screened.
- OpenAlex query for income-group comparisons without a field restriction: 2,472 hits, 2,280 new; screened after rules together with the extra citation records (1,092).
- 181 new records are includable or possible and report income-group comparisons; 65 had an open-access PDF, 64 were coded (55 eligible).
- Semantic Scholar was not reachable (rate limit); RePEc and Google Scholar remain to be run by hand.

## Results
- 71 studies with at least one richer-vs-poorer contrast (27 from the included studies, 44 new); 216 contrasts.
- Headline directions: richer larger 29, poorer larger 24, opposite signs 10, no clear difference 3, unclear 5 (sign test p = 0.58).
- 33 headline contrasts have t/SE and N. Second check: 26 confirmed, 0 corrected, 6 without full text, 1 unverifiable; 8 flagged as implausible.
- Difference in partial correlations, richer minus poorer (random effects, HKSJ interval):
  - all outcomes: +0.018 [-0.116, 0.152], I2 99%; excluding flagged: -0.007 [-0.062, 0.048], k = 25
  - output and productivity: -0.040 [-0.072, -0.007], k = 20; excluding flagged: -0.036 [-0.069, -0.003], k = 16
  - verified and not flagged, all outcomes: -0.016 [-0.084, 0.053], k = 19
- Reading: no evidence that richer economies gain more. For output, the association is, if anything, slightly larger in poorer economies, but the difference is small (about a fifth of the average association of 0.16) and rests on 16 to 20 studies coded with model assistance.

## Open
- Full texts for 18 included and 116 new studies (SE/N and more contrasts).
- Independent second human coder for the analysed contrasts.
- Risk of bias of the new studies was rated by the coding model and is more lenient than the original ratings; it must be re-rated on the original scale.

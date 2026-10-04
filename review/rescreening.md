# Independent re-screening of a random sample (blind second screener)

A separate model run, given only the review criteria and each record's title and abstract (no earlier decision), screened 340 randomly chosen records. This is a second screener of the same model family as the first, so it checks consistency and recall, not truth. Disagreements about exclusions were then adjudicated by a third blind reading of the abstract. Sample size per stage is small, so intervals are wide.

## Abstract stage (S3, n = 120 of 456)

| Second screener's UNSURE counted as | Agreement | Cohen's kappa |
|---|---|---|
| include | 79% | 0.59 |
| not include | 78% | 0.54 |

Of the 8 sampled records the first screener had set aside as "environmental outcome only, low priority" (protocol amendment 2), the second screener would have sent 7 to full text. Carbon and electricity outcomes are in the protocol's outcome family 6, so these records meet the eligibility criteria; setting them aside was a prioritisation choice, and it is why only 4 included studies report resource-cost outcomes.

## Recall: records excluded by the first screener that a second reader would include

| Stage excluded | Sample | Second screener: include or unsure | After adjudication: meets or probably meets | Share (95% CI) | Implied number among all excluded at this stage |
|---|---|---|---|---|---|
| Automated stage-1 rules | 100 | 7 | 2 | 2.0% (0.6 to 7.0) | about 31 of 1545 (range 9 to 108) |
| Title level | 120 | 15 | 10 | 8.3% (4.6 to 14.7) | about 134 of 1611 (range 74 to 236) |
| Abstract level (coded exclusions only) | 120 | 8 | 4 | 3.3% (1.3 to 8.3) | about 15 of 456 (range 6 to 38) |

Taken together, the screening may have excluded on the order of 180 records (range about 88 to 382) that a careful reader would have sent to full text, in addition to the 22 records set aside on purpose as environmental-outcome-only. 9 of the 30 adjudicated records could not be judged because no abstract was available. The estimate rests on small samples and on model readers; it is a warning about recall, not a count.

Adjudicated records judged to meet or probably meet the criteria are listed in `data/rescreen_adjudication.json`. Typical cases: artificial-intelligence or digital-economy panels with carbon or energy outcomes, small panels of fewer than 10 economies judged eligible under the AI rule, and financial-inclusion studies in Africa and the Arab world.


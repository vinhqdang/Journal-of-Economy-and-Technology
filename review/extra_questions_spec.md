# Additional research questions (specified before the analyses were run, 3 October 2026)

Main question (RQ1, already answered in `synthesis.md` and `mra_pilot.md`): do the gains from digital technology waves differ by income level and enabling conditions?

The questions below use only data already collected. They are **exploratory**. Each has a fixed analysis, so the result does not depend on choices made after seeing the data. All are reported, including null results. No multiplicity correction is applied; with 8 tests, one or two p-values below 0.10 are expected by chance, so a single significant result is a hypothesis, not a finding. Inputs are machine-extracted and not human-verified.

| # | Question | Data | Analysis | Why it matters |
|---|---|---|---|---|
| RQ2 | Does the size of the ICT-output association depend on how the technology is measured (composite index versus a single indicator)? | MRA estimates (`mra_estimates.csv`) | Add a `composite` indicator (exposure variable is an index, PCA score or composite) to the clustered moderator regression | Index-based studies dominate recent work, and an index can mix inputs and outcomes |
| RQ3 | Does it depend on the outcome form (growth rate versus log level)? | MRA estimates | Add a `growth` indicator (outcome transform is a growth rate) | Level regressions with trending variables overstate associations |
| RQ4 | Is the association weaker in later samples (diminishing returns)? | MRA estimates, sample midyear parsed from the years field | Add centred midyear to the same regression | Tests whether ICT returns faded as adoption spread |
| RQ5 | Are weaker designs more common where low-income economies are sampled? | 67 included studies | Fisher exact tests: low-income economy present versus (a) identification strategy none versus any, (b) overall risk of bias moderate versus serious or critical | If designs are weaker exactly where the question matters, the income-gap question is least answerable there |
| RQ6 | Does study quality go with the reported direction for output? | Included studies reporting family 1 | Fisher exact tests: share of studies whose family-1 results are all positive, by overall risk of bias (moderate versus serious or critical) | Shows whether the positive consensus depends on weaker studies |
| RQ7 | Which enabling conditions do authors test, and does the condition amplify or dampen the technology's effect? | Heterogeneity entries in the 67 records | Count studies by moderator type; classify each entry as amplifies, dampens, mixed or not a moderation test, by one reader with a 20% second-reader check | Tests the claim that returns are conditional |
| RQ8 | Where do thresholds appear, and do they agree across studies? | Threshold values in the 67 records | Tabulate stated thresholds by variable, without pooling | Thresholds are cited in policy, but each rests on one study |
| RQ9 | Where are the evidence gaps? | 67 records | Map outcome family by income-group coverage and by stream; count studies per cell | Shows which questions the literature cannot yet answer |
| RQ10 | Does the AI stream differ from the historical-wave stream in design and coverage? | 67 records | Compare streams on risk of bias, identification, income-group comparison, low-income coverage, and sample size | Tests whether AI evidence is comparable to earlier waves |

**Not answerable with the current data** (need new studies, not new analysis): effects by adoption level (dose-response) within a single design; causal effects by income group; time-varying effects around specific technology arrivals; cost-effectiveness; heterogeneity inside low-income economies.

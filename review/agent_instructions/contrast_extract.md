# Coding within-study income contrasts

Goal: for each study, record every comparison of the technology-outcome association between a richer and a poorer group of economies that the study itself estimates, so that the difference can be analysed with the study's own design held constant.

Inputs
- `contrast_input.json`: the verified extraction record of each candidate study (results, heterogeneity, income_group_results, sample, design).
- `txt/<idx>.txt`: full text, where available. Use it to fill coefficients, standard errors, t statistics, p values and numbers of observations that the extraction record lacks. Do not guess numbers that are in neither source.

What counts as a contrast
- Split-sample: the same specification estimated separately for a richer and a poorer group (World Bank income groups, developed vs developing, OECD vs non-OECD, high vs low income by the authors' rule).
- Interaction: technology x (richer-group dummy or income level) in one regression.
- Regions are a contrast only if the study itself labels them as richer/poorer (for example "advanced" vs "emerging"). Otherwise record design = "region" and they will be analysed separately.
- Not a contrast: groups that are not ordered by income, single-group samples, descriptive trends.

Record one object per contrast:
```
{"idx": "...", "study": "...", "family": 1-6, "outcome": "...", "technology": "...", "estimator": "...",
 "comparison": "WB income groups | developed-developing | OECD-nonOECD | income level (continuous) | region",
 "design": "split-sample | interaction | region",
 "richer_group": "...", "poorer_group": "...",
 "b_rich": num|null, "se_rich": num|null, "t_rich": num|null, "p_rich": "text"|null, "n_obs_rich": int|null, "n_econ_rich": int|null,
 "b_poor": ..., "se_poor": ..., "t_poor": ..., "p_poor": ..., "n_obs_poor": ..., "n_econ_poor": ...,
 "b_inter": num|null, "se_inter": num|null, "t_inter": num|null, "p_inter": "text"|null, "n_obs_inter": int|null,
 "same_units": true|false,          # are b_rich and b_poor on the same scale (same specification and variables)?
 "diff_test_reported": true|false,  # does the study formally test the difference (interaction, Chow, Wald, z test)?
 "direction": "richer larger | poorer larger | no clear difference | opposite signs | unclear",
 "headline": true|false,            # exactly one per study, see rule
 "evidence": "page/table locator and short quote",
 "needs_fulltext": true|false,      # true if t/SE/N are missing and the full text is not available
 "notes": "..."}
```

Direction: compare the point estimates on the same scale (richer larger means b_rich > b_poor for a beneficial outcome; for outcomes where lower is better, such as Gini, poverty, emissions, CO2 intensity or mortality, state in notes that the sign is reversed and code direction in terms of the benefit). If the difference test is reported, follow it; if the intervals overlap heavily and no test is reported, still code the point-estimate direction but set diff_test_reported false.

Headline rule (one per study): output and productivity family first, otherwise the family the study is mainly about; the study's main technology measure; its preferred or main specification; the richest vs poorest groups available (high vs low, else high vs lower/middle, else developed vs developing).

When the group with more than two categories is reported (high, upper-middle, lower-middle, low), record the headline as richest vs poorest and also add the other adjacent pairs as non-headline contrasts.

Output: a JSON list written to the file named in the task. Then a short report: number of studies, contrasts, headline contrasts with both t (or SE) and N available, studies needing the full text.

## New records (full text only)

For records found by the supplementary searches there is no extraction record. First decide full-text eligibility using the criteria in `agent_instructions/screen_chase.md` (include, or exclude with code E1 to E5). For included records also record: stream ("H" or "AI"), technology, outcome families, n_economies, years, estimator, and overall risk of bias (low, moderate, serious, critical) using: low = credible design for the claim; moderate = standard panel design with reasonable controls but exogeneity not established; serious = causal language with no strategy for reverse causation, or a mismatched exposure index; critical = severe problems (implausible magnitudes, very few observations, no controls). Then code the contrasts as above, using the OpenAlex id as idx.
Output per record: {"idx", "title", "eligibility": "include|exclude", "code", "stream", "technology", "families", "n_economies", "years", "estimator", "risk_of_bias", "contrasts": [ ... objects as above ... ]}.

# Risk-of-bias rating (adapted ROBINS-I), same scale as the original included studies

Rate six domains, each low / moderate / serious / critical, then an overall rating:
1. confounding_reverse_causation: is adoption treated as exogenous? Is there a credible strategy (external instrument with argued exclusion, timing design, natural experiment)? Internal-lag GMM alone, with causal language, is serious; with many instruments or Hansen/Sargan p near 1, serious.
2. exposure_measurement: does the measure capture the technology (penetration rates are moderate; composite indices whose scope does not match the technology, or proxies such as ICT imports, are serious).
3. selection_of_countries_years: selection by data availability, short windows, unbalanced panels, tiny subsamples.
4. outcome_measurement: quality of the national statistics; constructed indices.
5. specification_researcher_df: many specifications with no preferred one, unexplained sign flips, inconsistent tables (stars that do not match SEs, impossible t values).
6. selective_reporting: only significant results shown, missing tables, "available on request".

Overall: the worst domain usually sets it, but one serious domain among otherwise moderate ones gives serious.
- low = credible design for the claim (rare);
- moderate = standard panel design with reasonable controls but exogeneity not established, and no serious problem elsewhere;
- serious = causal language with no strategy for reverse causation, or a measure that does not capture the exposure, or a serious problem in any domain;
- critical = the conclusions cannot be trusted from this design (implausible magnitudes, internally inconsistent tables, very few observations, no controls).
In the original set of 97 studies the overall ratings were moderate 11%, serious 77%, critical 11%, none low. Most single-equation panel or GMM studies with causal language are serious. Calibration examples with domain reasons: rob_calibration.json.

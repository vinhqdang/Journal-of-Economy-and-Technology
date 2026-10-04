# Narrative synthesis: who gains from technology waves, and under what conditions

**Status: working draft for the review team. Based on 67 included studies read in full (of 247 sent to full-text assessment). Extractions are machine-made. 64 were re-checked once against the texts by a separate model run (`second_pass_verification.md`); the last three (71, 278, 341) had only a first pass plus a check of their printed numbers by search. The author has also checked the extracted data by hand (scope recorded in `data/human_check.md`). Read the limits in section 9 before quoting anything.**

Method: structured narrative synthesis (SWiM). Studies are grouped by outcome family and by technology; direction of association, size where comparable, and the moderators the authors tested are tabulated. No studies are pooled here except in the pilot meta-regression (`mra_pilot.md`), which covers only ICT-type adoption and output. Because every included study has a moderate, serious or critical risk of bias and no study rates "low", the direction of an association is reported, not a causal effect.

## 1. What the evidence base looks like

| Item | Count |
|---|---|
| Included studies | 67 (54 on ICT, mobile, internet, broadband and similar; 11 on AI; 2 on both) |
| Risk of bias, overall (first-pass ratings) | moderate 8, serious 50, critical 9, low 0. The second-pass check would move nine ratings (six down, three up); it is not applied |
| Studies with no identification strategy beyond controls and fixed effects | 36 of 67 |
| Studies with a formal or descriptive income-group or regional comparison of the effect | 26 of 67 |
| Studies that list a low-income economy (negated mentions such as "no low-income country" not counted) | 20 of 67 |
| Studies where the headline estimate is the preferred specification | yes 24, no 7, unclear 36 |

Studies per outcome family (a study can contribute to several): output and productivity 37; labour market 14; poverty and distribution 11; living standards beyond income 12; structural change 5; resource cost 4. AI evidence by family: output 4, labour 5, poverty and distribution 2, living standards 3, resource cost 2, structural change 0.

The evidence is thick for one question (ICT and output in rich or mixed samples) and thin for the rest. Almost all the evidence is on ICT, mobile and internet. The 13 AI studies are mostly short panels (2015 to 2023) of 3 to 78 economies, and several use a national readiness index or a count of robots as the AI measure.

## 2. Output and productivity (37 studies; 4 on AI)

**Direction.** Most studies report a positive association between ICT-type adoption and growth or productivity, but not all. Of the 16 studies whose headline estimate could be converted to a partial correlation, 88% are positive and 75% positive and significant. The pooled value is 0.19 (95% CI 0.10 to 0.27) with I² of 93%, so studies disagree strongly on size. After correcting for small-study bias the effect shrinks to between 0.005 (FAT-PET) and 0.06 (PEESE). See `mra_pilot.md`.

**Effects can run the other way or cancel out.** Mobile subscriptions: current-year effect +0.209 and lag -0.247 in a 41-economy system GMM (10). Country-by-country estimates for ten Asian economies are positive in four, negative in two, and insignificant in four (57). Ten high-income countries show no significant effect of any ICT indicator (1448). In 27 EU states the DESI digitalisation coefficient loses significance once economic freedom is added (988). In 11 MENA economies, CS-ARDL estimates of an ICT index on GDP per capita are 0.05 (long run) and 0.06 (short run), both significant only at 10%, while the dynamic common correlated effects estimate is 0.30; the paper's own causality tests show feedback in both directions (71). A digital economy index lowers green total factor productivity across 40 Belt and Road economies (245), although that outcome sits closer to resource cost.

**Estimator matters.** In the meta-regression, estimates from system or difference GMM are on average 0.16 lower in partial correlation than OLS or fixed-effects estimates (p < 0.01 with clustered errors, 18 papers). This is consistent with reverse causation inflating simpler estimates, though it cannot prove it.

**Complementarities are the most repeated finding.** ICT pays more where human capital is higher: tertiary-enrolment interactions are positive in two Asian system-GMM studies (302, 323) and in a developing-country productivity study (422); in Africa the marginal effect of the digital economy is negative below a human capital index of about 2.35 and positive above it, and the average African country is below the threshold (408). Financial development, trade openness, governance, electricity and ICT's own diffusion level also appear as moderators (957, 422, 988, 302). Most of these are interaction terms in single-equation panels, so they show conditional association, not that raising the moderator would change the return.

**Time pattern.** A non-parametric study of 24 OECD economies finds no contemporaneous effect of ICT capital change on the frontier but a positive effect five years later (321). A 27-country EU study finds similar ICT elasticities (about 0.09) in 1996 to 2004 and 2005 to 2016 (285). Studies that look only at the contemporaneous coefficient can miss this.

**AI and output.** Four studies. Developed economies show about twice the productivity effect of emerging economies (0.24 against 0.11) in a 10-economy comparison rated at critical risk of bias (535). In 63 low and lower-middle income economies, AI-related imports are associated with higher labour productivity, more so where connectivity, electricity and financial inclusion are better, and no different between low and lower-middle income (879). A sub-Saharan firm-level study (913) and a three-country generative-AI survey (1596) are both rated critical and cannot be relied on.

## 3. Structural change (5 studies; none on AI)

Internet penetration is associated with faster structural change, and the association is larger in low and lower-middle income and agrarian economies than in upper-middle and high-income ones (707, 51 economies). It is also larger where forward value-chain linkages are higher. The same study finds that manufacturing employment falls in South Asia and is unchanged in sub-Saharan Africa. A 3G coverage study in 14 developing countries finds jobs created in services and non-farm self-employment but no shift of labour away from agriculture (1679). ICT is positive for industry and services value added but not for agriculture in a 26-economy PMG study (1031), although columns 2 to 4 of its Tables 10 and 11 are identical across industry and services, so that paper needs a human check. Information and communication technology is associated with lower export concentration and a more diversified export structure in about 100 developing economies, and the effect is larger in the low and lower-middle income group (−0.155 on the concentration index) than in the high and upper-middle group (−0.020), with no formal test of the difference (341, system GMM, rated moderate; the paper is inconsistent on years and country counts). The evidence base here is still small.

## 4. Labour market (14 studies; 5 on AI)

**ICT and routine work.** Studies of advanced economies agree that ICT is linked to polarisation and a shift of employment away from routine tasks (239, 802, 126). In 27 European countries ICT capital creates more jobs where the share of high-skilled jobs is lower (126). Capital-skill complementarity raises skill premia in 14 OECD economies (1759) and narrows gender wage gaps in 11 (803). Every one of these studies is on high-income economies. No included study measures routinisation in low-income economies.

**Mobile internet in developing countries.** 3G coverage raises women's labour-force participation but not men's, with effects in services wages and unpaid or non-farm self-employment, in 14 low and middle income countries (1679, rated moderate). It is one of the few studies in the set that uses an instrument for developing-country labour outcomes.

**AI and employment.** Studies find AI exposure positively associated with employment growth, concentrated in high-education occupations and younger workers: 16 European countries (108) and 23 mostly high-income countries (1526, with gains only in the high computer-use tercile). In Southeast Asia, Singapore is the only complementarity case, and Indonesia and Thailand show displacement (750; the country-level results sit in a figure that could not be checked). Across 29 countries the AI index effect on employment declines with labour productivity level (1564). A 78-economy readiness index study (441) is rated critical. The pattern across studies is that AI complements skills and displaces the rest; the evidence on low-income economies is nil.

## 5. Poverty and distribution (11 studies; 2 on AI)

Results split. In 45 developing countries a threshold model finds ICT raises the Gini below a digital maturity score of 0.48 and lowers it above, an inverted U (1494); the mean score of 0.458 is close to the threshold. A study of poverty and inequality finds the inequality effect on poverty reverses above a technology threshold (1372). In 48 sub-Saharan African economies ICT is positively associated with a composite inclusive growth index (0.03 to 0.15 across specifications), with trade openness negative on its own and offset by ICT in the interaction, though the paper is inconsistent about its estimator (278). Mobile banking is mostly null or weakly negative on average inclusive growth, with effects at the tails of the distribution (1419). Robots raise inter-country carbon inequality, less so in open and well-connected economies (174, threshold on trade openness). Wage distribution results in OECD countries are those above under labour market.

The consistent message is that effects depend on how far a country has gone: below some level digitalisation widens the gap, above it narrows it. The thresholds are estimated in single studies with large uncertainty and have not been replicated.

## 6. Living standards beyond income (12 studies; 3 on AI) and resource cost (4 studies; 2 on AI)

**Living standards.** Mobile subscriptions are positively associated with the Human Development Index in high-income and lower-middle-income groups, and not in low-income countries (138, 193 stated economies). ICT slopes on HDI are positive in South Asia, sub-Saharan Africa and Latin America (68, 79 developing economies). In low and lower-middle income countries ICT narrows gender education gaps up to about 100 mobile subscriptions per 100 people, after which the gap widens again (1469). Internet raises financial inclusion more where governance is better (1798, sub-Saharan Africa), and mobile helps only where internet access is adequate (10). An AI development index raises human-capital-based educational development in developed economies and not in developing ones (276, with a sharp COVID-period jump).

**Resource cost.** Digitisation is associated with higher carbon productivity, and the effect falls with income: 0.085 for high-income, 0.058 for middle, 0.041 for low countries (162, 136 economies). A digital-economy index lowers green total factor productivity in Belt and Road economies (245). The nonlinear AI-energy poverty relation, using robot stocks, has human capital and institutions flatten the curve (1026, no low-income economies). Four studies are too few.

## 7. Do gains differ by income level? Answer to the main question

Twenty-six studies compare income groups or regions, formally or only descriptively. Reading them one by one:

| Finding | Studies | Notes |
|---|---|---|
| Effect larger in richer or OECD economies | 88, 138, 162, 268 (direct effect), 276, 535, 957, 750 | Several have no test of the difference (88 gives results "on request"; 750 is a handful of countries and its country results could not be checked). 535 is rated critical and its numbers look illustrative. 957 compares OECD with MENA, not income groups |
| Effect larger in poorer or less productive economies | 341, 407, 707, 1192, 268 (moderation of informality drag), 952 | 407 compares Central and Eastern with Western Europe, not income groups. 1192 is a single cross-section rated critical; 952 has a sign flip between pooled and subgroup models |
| No clear difference | 29, 320, 879 | 879 compares low with lower-middle income only |
| Effect negative in all groups, larger in middle-income | 245 | Green TFP outcome |

There is no consensus. The nominal majority points to larger or earlier gains where income, human capital, financial depth and governance are higher, but these studies are mostly OLS or fixed-effects, test the difference informally, and rarely include low-income economies. The studies pointing the other way, based on catch-up and saturation arguments, are fewer and weaker on design. What can be said is more modest: moderators of income level recur (human capital above all, then financial development, governance, infrastructure and trade openness), and the returns often look conditional on them. The claim that one group of economies benefits more than another is not established by this set.

## 8. Is AI like earlier waves?

On the evidence in hand AI cannot be compared with earlier waves on equal terms.
- 13 AI studies against 51 on earlier technologies. Median AI panel starts in 2012 or later and is short; ICT panels run across decades.
- AI exposure is measured by indices (occupational exposure, readiness indices, patents, robot density). None measures realised use of generative AI at country level.
- Where AI studies show an effect, it tends to be larger in richer economies and in high-skill occupations, as ICT results did in the same data set, and shows up as a conditional association.
- Evidence from low-income economies is a single productivity study (879) and two critical-rated studies.

A fair reading is "similar in pattern to ICT where tested, but with too little and too weak evidence to say it is similar in size or incidence."

## 9. Limits

- **Second pass.** A separate model run re-read each included record and every regression estimate against the text. Across 372 result entries it found 19 wrong and 5 unverifiable; across 203 regression estimates, 1 wrong. The record's wrong entries are corrected in `data/extraction.json` under `second_pass`, but the narrative above still reflects the first-pass wording in places. Three papers (298, 878, 1495) were moved to excluded on eligibility grounds, and a human should confirm that. Several included papers are borderline (442, 1645, 392, 1026, 174, 913).
- **Selection.** Only studies with a free or supplied full text, or one the user judged reliable, were read; 144 of the 247 sent to full text remain unread, and paywalled studies are over-represented among them. The venues of four sources were skipped on quality grounds. Reading was a single reviewer plus automated rules.
- **Extraction.** Machine-extracted and quote-checked, but about 30% of quotes could not be matched verbatim but the author has checked the extracted data by hand (scope in `data/human_check.md`). The 90-decision screening sample in `data/verification_sample.csv` has not been returned.
- **Searches.** OpenAlex, Crossref and NBER were searched; arXiv did not complete; Scopus and Web of Science have not been run.
- **Design.** No study has low risk of bias. Most treat adoption as exogenous. The synthesis says where associations differ, not what causes them.
- **Counting.** Direction counts here are descriptive. They are not weighted by sample size or quality and a count of "positive" studies is not an effect size.
- **Interpretation.** All authors' claims of thresholds and inverted-U curves rest on one study each; the pilot meta-regression has 18 papers and only 5 with low or middle-income samples.

## 10. What a conclusion could responsibly say

1. Studies mostly find positive associations between ICT-type adoption and output or productivity, but the pooled size is small to medium, varies a lot across studies, and falls once small-study bias and reverse causation (GMM) are accounted for.
2. Gains are conditional. Human capital, financial depth, governance and infrastructure recur as moderators, mostly through interaction terms.
3. Whether poorer economies gain more or less than richer ones is unsettled. Ignoring design quality, the weight of the evidence leans to larger measured gains in richer or more developed samples, but with poor tests and few low-income observations.
4. Evidence on AI is too thin and short to be put next to ICT. The few studies that exist show patterns similar to ICT where they test them.
5. The main gap in the literature is credible identification for developing and low-income economies, across all six outcome families.

# Second-pass check of the extractions

**What this is.** After the first extraction, every included paper's record and every regression estimate used in the pilot meta-regression was checked a second time against the converted full text by a separate model run that had the record and the text, not the first run's reasoning. This catches transcription and reading errors. It is not a human check, it uses the same family of model as the first pass, and it reads the same machine-converted text (garbled tables stay garbled). The author's own hand check of a random sample against the source papers is recorded in `data/human_check.md`.

## Regression estimates for the meta-regression

- Estimates checked: 206 from 26 papers. Confirmed: 205; corrected: 1; unverifiable: 0; not applicable: 0.
- The one correction (245-10) changes the income label to a combined middle-income group. Five further estimates were excluded as not poolable (`data/mra_exclusions.csv`): 358 (exposure is fintech credit, not ICT adoption), 88-11 to 88-14 (growth outcome mixed with level outcomes) and 988-5 (TFP index in levels).
- Many papers carry pooling warnings in `data/second_pass/mra_ver_*.json` (composite indices instead of single technologies, conditional main effects when interactions are present, overlapping specifications on one sample, generated TFP outcomes). 302 and 323 share authors, panel and index, so they are not independent.

## Full-text records (papers still included or excluded after this check)

- Included records checked: 71. Results: confirmed 392, corrected 19, unverifiable 5. Heterogeneity items: confirmed 130, corrected 14.
- The checker's view of the overall risk-of-bias rating: agree 62, too lenient 3, too harsh 6. The ratings in the record were not changed; the differences are listed below for a human to settle.

| Paper | Record says | Checker says |
|---|---|---|
| 57 | serious | too_lenient |
| 268 | serious | too_harsh |
| 302 | serious | too_harsh |
| 323 | serious | too_harsh |
| 408 | serious | too_harsh |
| 707 | serious | too_harsh |
| 957 | serious | too_lenient |
| 1031 | serious | too_lenient |
| 1469 | serious | too_harsh |

## Eligibility changes and flags

Three papers were moved from include to exclude after this check (reversible, human to confirm): 298 (no own estimation, E4), 1495 (number of economies never stated, E1) and 878 (outcomes are trade ratios, not in the six families, E3). Other papers flagged as borderline and still included: 442 (no effect estimate reported; only Granger and cointegration tests), 1645 (methods written in the future tense; no coefficients in the tables), 392 (accounting decomposition, not regression), 1026 and 174 (industrial robots as the AI measure), 913 (called AI by the author; built from innovation questions), 320 and 1428 (financial-inclusion outcomes, which the protocol counts as family 5).

Checker's eligibility notes:

- 298 (exclude): Borderline, lean exclude. The paper is a descriptive growth-accounting and shift-share decomposition (an accounting identity, no statistical estimation, no standard errors or uncertainty) whose numbers are taken from Van
- 474 (exclude): Judgement call. The exposure actually measured is ICT investment/GDP (OECD), i.e. ICT in general, not AI; the record itself rates the measure 'critical' because it does not capture AI. Under the non-AI rule at least 10 e
- 878 (exclude): Quantitative with own FE and convergence estimation, AI exposure (government AI readiness), 28 economies with explicit AE vs EMDE comparison, so the economy-count and design criteria hold. The outcome criterion fails: th
- 1428 (include): Own panel cointegration (AMG) and Granger estimation, 11 economies, mobile and internet exposure: those criteria hold. The outcomes, though, are the IMF financial institutions access index (bank branches and ATMs per 100
- 1495 (exclude): Eligibility not established. The text never gives the number of economies (only 'several developing countries'; Table 1 is a 30-row country-year excerpt showing India, Indonesia, Kenya), so the 10-economy threshold canno

## Corrections by paper

Each item below is a result or heterogeneity entry where the checker found the record wrong or unsupported. Full text of each correction, with quotes and locators, is in `data/extraction.json` under `second_pass.corrections`.

- **10**: All coefficients match Table 4. The top of the SE range is 0.0463 (L.credit), not 0.0462. Outstanding deposits are significant only at p<0.05 and p<0.1 (lag), not p<0.01.
- **57**: W-bar values and p = .0000 are right, but the Granger test has no sign, so direction 'positive' should be 'not applicable'/not coded as an effect. It is a rejection of no
- **68**: Coefficients and SEs are right (broadband -0.070** (0.028), telephone -0.278*** (0.089), internet -0.077** (0.036), mobile -0.033 (0.033), ICT goods 0.085 (0.095)). Sampl
- **88**: Ln(sh) falls from 0.025 [18.24]** (MRW) to 0.004 [1.82] (phone), 0.004 [1.75]* (mobile), 0.002 [0.88] (PCs), 0.007 [3.38]** (composite). So significance is lost only for 
- **108**: All coefficients are right (Webb younger 0.212***, Felten younger 0.219***, software younger 0.107***, core -0.083*, older -0.117**), but 'about double the core/older gro
- **138**: Sign pattern of IQI holds for IV-GMM (Table 9: high +0.0828***, LM -0.132***, UM +0.125***; low mobile +0.133 ns) but NOT for PSCC-FE (Table 8 mobile: high +0.0605***, lo
- **174**: Coefficients confirmed (Table 10 col 1 -0.0163, t -14.804; Table 11 col 1 c=4.7370, b_LNAI 0.0225, d_LNAI -0.0665, net -0.0440). The 114% level is the extractor's exp() c | Coefficients confirmed (Table 10 col 3 -0.0064, t -6.118; Table 11 col 3 c=2.9072, b 0.0031, d -0.0078, net -0.0047). 'About 50% above' is not in the text; text says only
- **268**: Advanced sample: ΔINT is positive and significant in all three employment-share models (.031* SE .016; .038** SE .017; .03* SE .016), not two; only the VA model is null (
- **320**: The paper has no income-group analysis. It contrasts China and Nigeria with 18 other countries by country dummies and frames them as 'developed and emerging' economies; t
- **321**: Numbers are right (Tn=0.772, bootstrap p=0.108), but the direction should be null/inconclusive rather than positive: it is a non-rejection of equality between the 2019 di
- **358**: Option labels are off by one. In Table 7 the INTRNT row is blank in option I: -0.17*** (t=-4.32) is option II, -0.13** (t=-2.30) is option III, -0.22*** (t=-5.67) option  | Numbers and t-values match Table 12 (0.99** (2.13), 0.99*** (3.11), 1.15*** (3.71), 0.86*** (2.68)), but only options I-II are per-capita income growth; options IV-V are 
- **392**: Direction should be 'mixed', not 'null': no cross-country dependence of TFP on ICT intensity, but a strong negative time-series correlation between ICT growth and TFP gro
- **422**: Numbers confirmed (q10 0.00859 SE 0.00208; q20 0.00604; q30 0.0071; q40 0.000240 SE 0.000182 no stars; q50 0.00854; q60 0.00515 ** SE 0.00204; q70 0.00644; q80 0.00583; q
- **442**: Westerlund p-values confirmed (Gt 0.003, G 0.004, Pt 0.032, Pa 0.010) but the test is of cointegration and has no sign: the direction 'positive' rests only on the authors | Statistics confirmed (mb->w W 5.6610, Z-bar 8.5858; w->mb W 4.1382, Z-bar 5.0146; both p 0.0000). Direction should be 'bidirectional, unsigned' rather than 'mixed': Grang | Statistics confirmed (web->w W 4.6323, Z-bar 6.1733, p 0.0000; w->web W 4.5904, Z-bar 6.0750, p 0.4289), but direction 'positive' is wrong for a Granger test: it is unsig
- **617**: The income-group comparison is a box plot of hosts only (Fig 3). For the small/large contrast, the text speaks of a 'much more strongly positive' relationship (R-sq 0.785
- **707**: Internet result is supported (Model 3: 0.0463**, -0.0448***, -0.0499***; Model 4: 0.0528**, -0.0520**, -0.0577**); the net effect for developing/developed groups is about
- **750**: Coefficients appear only in Figure 2, which is not in the extracted text. The text is internally inconsistent on Malaysia: it first lists Malaysia among reinstatement cou
- **802**: Low-wage group is five countries including Russia (Estonia, Poland, Czech Republic, Slovakia, Russian Federation), not five plus Russia. High = Norway, Denmark, Belgium, 
- **803**: Estimates are right (-0.001, -0.009, -0.013, SE 0.004 each; observed -0.075 in Table 6) but direction 'null' is only right for the exogenous case. With unit-elastic labou
- **879**: Range is wrong at the low end: Table 11 flow-based coefficients are 0.0693, 0.0654, 0.0684, 0.0708, 0.0716, 0.0681, so the range is 0.0654 to 0.0716 (not 0.0681 to 0.0716
- **891**: B2 turning point 21.4 is correct. The A2 turning point is an arithmetic error in the paper: with the printed -0.0026 and 0.0003, 2 x 0.0003 = 0.0006 (printed as 0.00006),
- **957**: The OECD direct internet coefficient is not in Table 5 (blank INTERNET row, three columns) while the text says all OECD ICT effects but mobile are positive and significan
- **988**: Numbers are right (0.093 in col 3 to 0.040 in col 4, institutions 0.033, t 1.95, 10 percent), but this is a control-sensitivity result, not heterogeneity: there is no int
- **1026**: Table 10 lists seven alternative specifications (patent stock, electricity access, excluding oil exporters, excluding 2008-10, 2SLS, Bartik, spatial lag) plus the baselin
- **1031**: Agriculture short-run LNTO in Table 9 is 0.0940, 0.1066, 0.0768, 0.1232* so the range is 0.0768 to 0.1232 (record says 0.0940 to 0.1232); SE 0.0701 to 0.1445 is right. No | Negative significant interactions are TO_IUI, TO_MCS, TO_ICTINF only; TO_FTS in Tables 10-11 is +0.0026 {0.0019}, insignificant, although the text says all four are negat
- **1428**: Stated FIA numbers are right (Mobile to FIA: Hungary 0.000899, Latvia 0.0070361, Lithuania, Poland, Slovenia positive; Czech Republic -0.0014063; Internet to FIA: Latvia  | Statistics and p-values are right (DMOBILE to DFIA W 4.77462, Zbar 2.93274, p 0.0034; DINTERNET to DFIA Zbar 2.07345, p 0.0381; DFIA to DINTERNET Zbar 1.97332, p 0.0485; 
- **1494**: Threshold 0.48 (Gini) and about 0.50 (Theil) are right, but the claim that 'roughly half the sample-years are in each regime' is the extractor's inference: regime counts 
- **1652**: Directions are right but the record says no statistics are available; Appendix A (p.421, after references) does give Dumitrescu-Hurlin W-bar/Z-bar/p: BTCV not-> GDP W=2.8
- **1670**: Text states only that the path is significant; no sign, coefficient or SE appears in the text (Figure 2 is an image). The direction label 'mixed' is a placeholder and sho | Text says the indirect path is significant but gives no sign or size; 'positive' is inferred by the record (and acknowledged in its own evidence field). FII -> MOBILE is 
- **1713**: Supported as descriptive remarks, but the Finland +20% TFP figure is from the m1 (aggregate capital) decomposition, not from the ICT-separated model m2; the Korea/Japan I
- **1798**: Table 1 internet coefficients are -0.0003 (political stability), -0.0003 (voice), 4.17e-06 (regulatory quality, p=0.979), -0.0003 (government effectiveness, p=0.021), -0.

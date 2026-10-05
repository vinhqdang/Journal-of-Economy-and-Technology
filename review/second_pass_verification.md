# Second-pass check of the extractions

**What this is.** After the first extraction, every included paper's record and every regression estimate used in the pilot meta-regression was checked a second time against the converted full text by a separate model run that had the record and the text, not the first run's reasoning. This catches transcription and reading errors. It is not a human check, it uses the same family of model as the first pass, and it reads the same machine-converted text (garbled tables stay garbled). The author's own hand check of a random sample against the source papers is recorded in `data/human_check.md`.

## Regression estimates for the meta-regression

- Estimates checked: 317 from 37 papers. Confirmed: 311; corrected: 6; unverifiable: 0; not applicable: 0.
- 6 estimates were corrected: 245-10 (income label changed to a combined middle-income group) and the five estimates of study 9103, which had been read from the wrong cell of a panel-VAR table (rows are equations, columns are lagged regressors; the paper itself reads the table the other way). Study 9103 reports p-values, so its estimates are not converted in the pilot in any case. Five further estimates were excluded as not poolable (`data/mra_exclusions.csv`): 358 (exposure is fintech credit, not ICT adoption), 88-11 to 88-14 (growth outcome mixed with level outcomes) and 988-5 (TFP index in levels).
- Many papers carry pooling warnings in `data/second_pass/mra_ver_*.json` (composite indices instead of single technologies, conditional main effects when interactions are present, overlapping specifications on one sample, generated TFP outcomes). 302 and 323 share authors, panel and index, so they are not independent.

## Full-text records (papers still included or excluded after this check)

- Included records checked: 88. Results: confirmed 492, corrected 34, unverifiable 5. Heterogeneity items: confirmed 152, corrected 18.
- The checker's view of the overall risk-of-bias rating: agree 77, too lenient 4, too harsh 7. The ratings in the record were not changed; the differences are listed below for a human to settle.

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
| 9204 | serious | too_lenient |
| 9401 | critical | too_harsh |

## Eligibility changes and flags

Four papers were moved from include to exclude after this check (reversible, human to confirm): 298 (no own estimation, E4), 1495 (number of economies never stated, E1), 878 (outcomes are trade ratios, not in the six families, E3) and 474 (too few economies, E1). Other papers flagged as borderline and still included: 442 (no effect estimate reported; only Granger and cointegration tests), 1645 (methods written in the future tense; no coefficients in the tables), 392 (accounting decomposition, not regression), 1026 and 174 (industrial robots as the AI measure), 913 (called AI by the author; built from innovation questions), 320 and 1428 (financial-inclusion outcomes, which the protocol counts as family 5).

Checker's eligibility notes:

- 298 (exclude): Borderline, lean exclude. The paper is a descriptive growth-accounting and shift-share decomposition (an accounting identity, no statistical estimation, no standard errors or uncertainty) whose numbers are taken from Van
- 474 (exclude): Judgement call. The exposure actually measured is ICT investment/GDP (OECD), i.e. ICT in general, not AI; the record itself rates the measure 'critical' because it does not capture AI. Under the non-AI rule at least 10 e
- 878 (exclude): Quantitative with own FE and convergence estimation, AI exposure (government AI readiness), 28 economies with explicit AE vs EMDE comparison, so the economy-count and design criteria hold. The outcome criterion fails: th
- 1428 (include): Own panel cointegration (AMG) and Granger estimation, 11 economies, mobile and internet exposure: those criteria hold. The outcomes, though, are the IMF financial institutions access index (bank branches and ATMs per 100
- 1495 (exclude): Eligibility not established. The text never gives the number of economies (only 'several developing countries'; Table 1 is a 30-row country-year excerpt showing India, Indonesia, Kenya), so the 10-economy threshold canno
- 9202 (exclude): Exclusion E1 is right. The sample is five economies (Egypt, India, Kenya, Saudi Arabia, Sudan), well under the 10-economy minimum for non-AI exposure; Sec. 4.1.1: 'Our analysis is restricted to five countries.' The paper
- 9301 (exclude): Exclusion E4 is right. The paper is a differential-equation model of labour productivity (Eqs. 10-27) with simulated projections to 2042. The only data use is a US-based technological-progress curve built from BLS and Gr
- 9403 (exclude): Exclusion E4 is correct. Section 5.1 says real data collection (WDI, ITU, UNDP, OECD, WGI) 'has not yet been completed' and that every coefficient in Tables 2-7 comes from a 'calibrated synthetic panel: a simulated count

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
- **1580**: Advanced/less-advanced split and USD 10,000 threshold are correct, as are Table 3 interaction (-0.227* GMM only) and Table 8 FE-IV (-0.375***). But 'only ... in Table 8 F
- **1652**: Directions are right but the record says no statistics are available; Appendix A (p.421, after references) does give Dumitrescu-Hurlin W-bar/Z-bar/p: BTCV not-> GDP W=2.8
- **1670**: Text states only that the path is significant; no sign, coefficient or SE appears in the text (Figure 2 is an image). The direction label 'mixed' is a placeholder and sho | Text says the indirect path is significant but gives no sign or size; 'positive' is inferred by the record (and acknowledged in its own evidence field). FII -> MOBILE is 
- **1713**: Supported as descriptive remarks, but the Finland +20% TFP figure is from the m1 (aggregate capital) decomposition, not from the ICT-separated model m2; the Korea/Japan I
- **1798**: Table 1 internet coefficients are -0.0003 (political stability), -0.0003 (voice), 4.17e-06 (regulatory quality, p=0.979), -0.0003 (government effectiveness, p=0.021), -0.
- **9101**: Numbers correct, but direction 'mixed' is wrong: both PCSE (0.090, p=0.052) and FGLS (0.317, p=0.000) are positive; PCSE is only borderline significant. Direction should 
- **9103**: Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Table 11 columns are lagged regressors and rows are dependent variables at t (Table 10 Granger p-values match this: e.g. UMIC RGDP-/->ICT p=0.2380 equals row ICT(t), colu | Under the table's own layout, ICT(t-1) -> RGDP(t) is positive and significant in every group: 0.0389 full, 0.2751 HIC (0.036), 0.0215 UMIC (0.0010), 0.0149 LMIC, 0.0175 L | ICT -> MAV is positive in all five samples (0.0002*, 0.0037**, 0.0005**, 0.0009***, 0.0019**), so there is no internal inconsistency in the full sample; the Granger part 
- **9201**: High-income trade interactions are 0.015 (Internet), 0.014 (mobile) and 0.005 (broadband), so the range is 0.005 to 0.015, not 0.014 to 0.015. FDI interactions lower ineq
- **9203**: Direction is mixed across specifications, not negative: Table 8 Model 2 prints a positive significant coefficient 0.05*** (.010) and Model 6 prints -0.037 (0.028). Negati
- **9302**: Direction should be mixed, predominantly positive: Table 4 also prints significant negatives. Model 12 Ln[e-government x internet users] -0.0081*** (0.002); Model 16 Ln[e
- **9304**: Mobile figures correct (col 1: 0.001** (0.020), -4.94e-06** (0.040); col 2: 0.002*** and -9.86e-06***; col 5: -0.002*). But 'internet terms insignificant' is not fully ri

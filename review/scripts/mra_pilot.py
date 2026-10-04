"""Pilot meta-regression of ICT-type adoption on output and productivity (see review/protocol.md).

Reads review/data/mra_estimates.csv (machine-extracted, number-checked against the source text, NOT yet
human-verified). Converts each estimate to a partial correlation coefficient (PCC) from its t-statistic and
degrees of freedom, then runs: random-effects pooling (DerSimonian-Laird), moderator meta-regression with
standard errors clustered by paper, and FAT-PET / PEESE publication-bias tests. Writes review/mra_pilot.md
and review/figures/funnel.png.
"""
import math, os, re, sys
import numpy as np, pandas as pd
import statsmodels.api as sm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
K_REGRESSORS = int(sys.argv[1]) if len(sys.argv) > 1 else 10   # assumed number of regressors for df

df = pd.read_csv(os.path.join(ROOT, "review/data/mra_estimates.csv"), dtype=str)

def num(s):
    m = re.findall(r"-?\d*\.?\d+", str(s))
    return float(m[0]) if m else np.nan

def parse_coef(s):
    s = str(s).replace("−", "-")
    m = re.findall(r"-?\d*\.?\d+", s)
    return float(m[0]) if m else np.nan

def tstat(row):
    c = parse_coef(row["coef_printed"])
    u = str(row["uncertainty_printed"]).replace("−", "-")
    typ = row["uncertainty_type"]
    v = num(u)
    if np.isnan(c) or np.isnan(v):
        return np.nan
    if typ == "se":
        return c / abs(v) if v else np.nan
    if typ == "t":
        t = abs(v)
        return math.copysign(t, c) if c != 0 else 0.0
    return np.nan                      # p-values and intervals are not converted in the pilot

df["coef"] = df["coef_printed"].map(parse_coef)
df["t"] = df.apply(tstat, axis=1)
df["n"] = pd.to_numeric(df["n_obs"].map(num), errors="coerce")
df["n"] = df["n"].fillna(pd.to_numeric(df["paper_n_obs_main"].map(num), errors="coerce"))
df["df_"] = df["n"] - K_REGRESSORS
df["pcc"] = df["t"] / np.sqrt(df["t"] ** 2 + df["df_"])
df["se"] = np.sqrt((1 - df["pcc"] ** 2) / df["df_"])

tech = df["technology"].fillna("").str.lower()
df["exclude_reason"] = ""
df.loc[tech.str.contains("crypto|bitcoin|artificial|\\bai\\b|generative"), "exclude_reason"] = "technology not ICT-type (crypto or AI)"
df.loc[df["role"] == "interaction", "exclude_reason"] = "interaction term, not a main effect"
df.loc[df["t"].isna(), "exclude_reason"] = df["exclude_reason"].replace("", "uncertainty not convertible to t (p-value or interval)")
df.loc[(df["df_"] <= 5) | df["df_"].isna(), "exclude_reason"] = df["exclude_reason"].replace("", "no usable number of observations")
# exclusions found by the second-pass check against the source texts (see data/mra_exclusions.csv)
excl = pd.read_csv(os.path.join(ROOT, "review/data/mra_exclusions.csv"), dtype=str)
excl_map = dict(zip(excl["estimate_id"], excl["reason"]))
mask = df["estimate_id"].isin(excl_map) & (df["exclude_reason"] == "")
df.loc[mask, "exclude_reason"] = "judged not poolable on second-pass check"
# correction from the second-pass check: 245-10 is a combined middle-income group, not upper-middle
df.loc[df["estimate_id"] == "245-10", "sample_income_group"] = "middle"
use = df[df["exclude_reason"] == ""].copy()
use["idx"] = use["idx"].astype(str)

def dl(y, v):
    w = 1 / v
    mu = np.sum(w * y) / np.sum(w)
    q = np.sum(w * (y - mu) ** 2)
    k = len(y)
    c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    tau2 = max(0.0, (q - (k - 1)) / c) if k > 1 else 0.0
    ws = 1 / (v + tau2)
    mu_r = np.sum(ws * y) / np.sum(ws)
    se_r = math.sqrt(1 / np.sum(ws))
    i2 = max(0.0, (q - (k - 1)) / q) if q > 0 else 0.0
    pi = (mu_r - 1.96 * math.sqrt(tau2 + se_r ** 2), mu_r + 1.96 * math.sqrt(tau2 + se_r ** 2)) if k > 2 else (np.nan, np.nan)
    return mu_r, se_r, tau2, i2, k, pi

out = []
out.append("# Pilot meta-regression: ICT-type adoption and output or productivity\n")
out.append("**Status: exploratory pilot, not a result.** The inputs were extracted by machine and every printed number was checked against the source text twice (an automatic proximity check and a second, independent reading of the tables by a separate model run), and the author has since checked a random sample of the extracted data by hand against the source papers (see `data/human_check.md`; the scope of that check is recorded there). Effect sizes are partial correlation coefficients (PCC) computed from the printed coefficient and its standard error or t-statistic, with degrees of freedom approximated as observations minus %d regressors. The sample is small, comes only from papers with a free or supplied full text, and the underlying studies mostly treat adoption as exogenous, so pooled numbers describe conditional association and not a causal effect.\n" % K_REGRESSORS)
out.append(f"- Estimates extracted: {len(df)} from {df['idx'].nunique()} papers.\n- Usable estimates: {len(use)} from {use['idx'].nunique()} papers. Excluded: " + "; ".join(f"{k} ({v})" for k, v in df[df['exclude_reason']!='']['exclude_reason'].value_counts().items()) + ".\n")

# (1) headline estimate per paper
head = use[use["role"] == "headline"].groupby("idx").first().reset_index()
if len(head) >= 3:
    mu, se, tau2, i2, k, pi = dl(head["pcc"].values, head["se"].values ** 2)
    out.append("## 1. One headline estimate per paper, random-effects pooling\n")
    out.append(f"- Papers: {k}. Pooled PCC = {mu:.3f} (95% CI {mu-1.96*se:.3f} to {mu+1.96*se:.3f}). Between-paper variance tau² = {tau2:.4f}, I² = {100*i2:.0f}%. 95% prediction interval {pi[0]:.3f} to {pi[1]:.3f}.\n")
    out.append("- Reading the numbers (rough Doucouliagos convention for partial correlations: 0.07 small, 0.17 medium, 0.33 large): a pooled value in the small-to-medium range with very high I² means papers disagree a lot about size, even if most signs are positive.\n")
    share_pos = (head["pcc"] > 0).mean()
    sig_pos = ((head["pcc"] > 0) & (head["t"].abs() > 1.96)).mean()
    out.append(f"- Share of headline estimates that are positive: {100*share_pos:.0f}%. Positive and statistically significant: {100*sig_pos:.0f}%.\n")

# (2) moderator meta-regression on all main estimates
m = use.copy()
inc_txt = m["sample_income_group"].fillna("").str.lower() + " " + m["subsample_label"].fillna("").str.lower()
m["lowmid"] = inc_txt.str.contains("low|developing|emerging|lower|middle|africa|sub-saharan|mena").astype(int)
m["highinc"] = inc_txt.str.contains("high|oecd|advanced|developed|eu|europe").astype(int)
m["lowmid"] = np.where(m["highinc"] == 1, 0, m["lowmid"])
m["gmm"] = m["estimator"].fillna("").str.lower().str.contains("gmm").astype(int)
m["mobile"] = tech[m.index].str.contains("mobile|cell").astype(int)
m["internet"] = tech[m.index].str.contains("internet|broadband").astype(int)
m["ident"] = m["paper_identification"].fillna("").str.lower().map(lambda s: 0 if s.startswith("none") or s == "" else 1)
m["caus"] = m["paper_causal_language"].fillna("").str.lower().str.startswith("yes").astype(int)
m = m.dropna(subset=["pcc", "se"])
X = sm.add_constant(m[["lowmid", "gmm", "mobile", "internet"]].astype(float))
w = 1 / (m["se"] ** 2 + 0.01 ** 2)
res = sm.WLS(m["pcc"], X, weights=w).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(m["idx"])[0]})
out.append("\n## 2. Moderator meta-regression (all main estimates, standard errors clustered by paper)\n")
out.append(f"Estimates: {len(m)}; papers (clusters): {m['idx'].nunique()}. With fewer than about 30 clusters the clustered standard errors are optimistic, so treat p-values as indicative only.\n")
out.append("| Moderator | Coefficient | Clustered SE | p |\n|---|---|---|---|")
for name in res.params.index:
    out.append(f"| {name} | {res.params[name]:.3f} | {res.bse[name]:.3f} | {res.pvalues[name]:.2f} |")
out.append("\n`lowmid` = the estimate comes from a low- or middle-income, developing or emerging sample (0 otherwise); `gmm` = system or difference GMM; `mobile`, `internet` = technology type relative to general ICT.\n")
grp = m.groupby("lowmid").agg(estimates=("pcc", "size"), papers=("idx", "nunique"), mean_pcc=("pcc", "mean"))
out.append("\nUnweighted summary by income setting:\n\n| Setting | Estimates | Papers | Mean PCC |\n|---|---|---|---|")
for k_, r_ in grp.iterrows():
    out.append(f"| {'low/middle-income or developing' if k_ == 1 else 'high-income, mixed or not stated'} | {int(r_['estimates'])} | {int(r_['papers'])} | {r_['mean_pcc']:.3f} |")

# (3) publication bias
fat = sm.WLS(m["pcc"], sm.add_constant(m["se"]), weights=1 / m["se"] ** 2).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(m["idx"])[0]})
peese = sm.WLS(m["pcc"], sm.add_constant(m["se"] ** 2), weights=1 / m["se"] ** 2).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(m["idx"])[0]})
out.append("\n## 3. Publication-bias checks\n")
out.append(f"- FAT-PET: PCC = {fat.params['const']:.3f} + {fat.params['se']:.2f} x SE. A slope on SE that is clearly different from zero (here p = {fat.pvalues['se']:.2f}) suggests small-study or selective-reporting bias; the intercept ({fat.params['const']:.3f}, p = {fat.pvalues['const']:.2f}) is the bias-corrected effect.\n")
out.append(f"- PEESE intercept (bias-corrected effect when a true effect exists): {peese.params['const']:.3f} (p = {peese.pvalues['const']:.2f}).\n")
out.append("- Funnel plot: `figures/funnel.png`.\n")
fig, ax = plt.subplots(figsize=(6, 4.2))
ax.scatter(m["pcc"], m["se"], s=18, alpha=0.7)
ax.axvline(0, color="grey", lw=0.8)
ax.invert_yaxis()
ax.set_xlabel("Partial correlation (PCC)")
ax.set_ylabel("Standard error of PCC")
ax.set_title("Funnel plot of main estimates")
plt.tight_layout(); plt.savefig(os.path.join(ROOT, "review/figures/funnel.png"), dpi=140)

# (4) sensitivity to df assumption
sens = []
for k_ in (0, 5, 20):
    d2 = use.copy(); d2["df_"] = d2["n"] - k_
    d2 = d2[d2["df_"] > 5]
    d2["pcc"] = d2["t"] / np.sqrt(d2["t"] ** 2 + d2["df_"]); d2["se"] = np.sqrt((1 - d2["pcc"] ** 2) / d2["df_"])
    h2 = d2[d2["role"] == "headline"].groupby("idx").first()
    if len(h2) >= 3:
        mu2 = dl(h2["pcc"].values, h2["se"].values ** 2)[0]
        sens.append(f"k = {k_}: {mu2:.3f}")
out.append("\n## 4. Sensitivity of the pooled headline estimate to the degrees-of-freedom assumption\n")
out.append("Assumed number of regressors " + "; ".join(sens) + ". A stable value means the result does not hinge on this approximation.\n")
out.append("\n## What this pilot can and cannot support\n")
out.append("- It can show whether there is enough comparable material to run a meta-regression at all, and which moderators are worth pursuing.\n- It cannot support a causal statement, a claim about AI (too few estimates), or a firm statement about income groups until the author's hand check is fully documented and the sample is widened beyond the studies found so far (the search had low recall; see google_scholar_results.md).\n")
with open(os.path.join(ROOT, "review/mra_pilot.md"), "w") as f:
    f.write("\n".join(out) + "\n")
use.to_csv(os.path.join(ROOT, "review/data/mra_effect_sizes.csv"), index=False, columns=["idx","estimate_id","role","subsample_label","sample_income_group","technology","coef","t","n","pcc","se"])
print("\n".join(out))

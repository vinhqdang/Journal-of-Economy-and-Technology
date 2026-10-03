"""Staggered event study with not-yet-treated controls (A4b) and local projections (A7). See spec_amendment.md.

Writes analysis/results_event.md and analysis/figures/event_study_cs.png, lp.png.
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

HERE = os.path.dirname(os.path.abspath(__file__))
END = 2019
P = pd.read_csv(os.path.join(HERE, "data", "wdi_panel.csv"))
GR = {"Low income": "Low", "Lower middle income": "Lower-middle", "Upper middle income": "Upper-middle", "High income": "High"}
P = P[P["income"].isin(GR) & (P["year"] <= END)].copy()
P["grp"] = P["income"].map(GR)
grp = P.drop_duplicates("iso3").set_index("iso3")["grp"]
piv = lambda v: P.pivot(index="iso3", columns="year", values=v)
M, Yd = piv("mobile"), piv("gdppc")
LY = 100 * np.log(Yd)
rng = np.random.default_rng(20261003)
BOOT = int(os.environ.get("BOOT", 400))

def takeoff(thr):
    t = {}
    for iso in M.index:
        r = M.loc[iso].dropna()
        if 1995 not in r.index or r.loc[1995] >= thr or iso not in LY.index or pd.isna(LY.loc[iso].get(1995)):
            continue
        above = r[r >= thr]
        t[iso] = int(above.index.min()) if len(above) else None
    return t

def att_table(isos, to, Y, treat_set, ks):
    """Aggregate ATT(e) over cohorts for the economies in `isos` (bootstrap sample may repeat economies)."""
    out = {}
    byg = {}
    for i in isos:
        g = to.get(i)
        if g and i in treat_set and 1996 <= g <= 2014:
            byg.setdefault(g, []).append(i)
    for e in ks:
        num = den = 0.0
        for g, T in byg.items():
            t, b = g + e, g - 1
            if t < 1995 or t > END or len(T) < 3:
                continue
            C = [i for i in isos if (to.get(i) is None or to[i] > t) and i in Y.index]
            Ti = [i for i in T if i in Y.index]
            Tt = [i for i in Ti if pd.notna(Y.loc[i].get(t)) and pd.notna(Y.loc[i].get(b)) and pd.notna(Y.loc[i].get(1995))]
            Cc = [i for i in C if pd.notna(Y.loc[i].get(t)) and pd.notna(Y.loc[i].get(b)) and pd.notna(Y.loc[i].get(1995))]
            if len(Tt) < 3 or len(Cc) < 8:
                continue
            def X(ids):
                y95 = np.array([Y.loc[i, 1995] for i in ids]); gr = np.array([(Y.loc[i, b] - Y.loc[i, 1995]) / (b - 1995) if b > 1995 else 0.0 for i in ids])
                return np.column_stack([np.ones(len(ids)), y95, gr])
            dC = np.array([Y.loc[i, t] - Y.loc[i, b] for i in Cc]); dT = np.array([Y.loc[i, t] - Y.loc[i, b] for i in Tt])
            beta, *_ = np.linalg.lstsq(X(Cc), dC, rcond=None)
            att = np.mean(dT - X(Tt) @ beta)
            num += len(Tt) * att; den += len(Tt)
        out[e] = num / den if den else np.nan
    return out

def run(thr, Y, treat_groups, label, ks):
    to = takeoff(thr)
    allis = [i for i in to if i in Y.index]
    treat = {i for i in allis if grp.get(i) in treat_groups and to[i]}
    pt = att_table(allis, to, Y, treat, ks)
    reps = []
    for _ in range(BOOT):
        draw = list(rng.choice(allis, size=len(allis), replace=True))
        # repeated economies keep their identity; duplicates are handled by list repetition in means (approximation)
        reps.append(att_table(draw, to, Y, treat & set(draw), ks))
    B = pd.DataFrame(reps)
    lo, hi = B.quantile(0.025), B.quantile(0.975)
    pre_keys = [k for k in ks if -5 <= k <= -2 and not np.isnan(pt[k])]
    pre_mean = np.mean([pt[k] for k in pre_keys]) if pre_keys else np.nan
    pre_boot = B[pre_keys].mean(axis=1) if pre_keys else pd.Series([np.nan])
    plo, phi = pre_boot.quantile(0.025), pre_boot.quantile(0.975)
    n_t = len(treat)
    return dict(label=label, thr=thr, n_treated=n_t, n_pool=len(allis), pt=pt, lo=lo, hi=hi, pre_mean=pre_mean, pre_ci=(plo, phi), pass_pre=(plo <= 0 <= phi) if pre_keys else False)

KS = [k for k in range(-5, 11) if k != -1]
SETS = [("All economies", list(GR.values())), ("Low and lower-middle income", ["Low", "Lower-middle"]), ("Upper-middle income", ["Upper-middle"]), ("High income", ["High"])]
L = ["# Event study (A4b) and local projections (A7), per `spec_amendment.md`", "", f"Bootstrap draws: {BOOT}. Effects are in log points times 100 (a value of 5 means GDP per capita about 5% higher than in the year before takeoff, relative to economies not yet treated). Associations; no instrument.", ""]
res_main = {}
for thr in (10, 25, 50):
    L += [f"## Takeoff at {thr} mobile subscriptions per 100", "", "| Sample | Treated | Pool | Pre-trend: mean of effects at -5..-2 [95% CI] | Passes pre-trend rule | Effect at +3 | Effect at +5 | Effect at +10 |", "|---|---|---|---|---|---|---|---|"]
    for lab, gs in SETS:
        r = run(thr, LY, gs, lab, KS)
        res_main[(thr, lab)] = r
        def eff(k):
            return f"{r['pt'][k]:.1f} [{r['lo'][k]:.1f}, {r['hi'][k]:.1f}]" if not np.isnan(r['pt'][k]) else "n/a"
        L.append(f"| {lab} | {r['n_treated']} | {r['n_pool']} | {r['pre_mean']:.1f} [{r['pre_ci'][0]:.1f}, {r['pre_ci'][1]:.1f}] | {'yes' if r['pass_pre'] else 'no'} | {eff(3)} | {eff(5)} | {eff(10)} |")
    L.append("")
fig, ax = plt.subplots(1, 4, figsize=(13, 3.2), sharey=True)
for i, (lab, gs) in enumerate(SETS):
    r = res_main[(10, lab)]
    ks = [k for k in KS if not np.isnan(r["pt"][k])]
    ax[i].axhline(0, color="grey", lw=0.8); ax[i].axvline(-0.5, color="grey", lw=0.5, ls=":")
    ax[i].plot(ks, [r["pt"][k] for k in ks], marker="o", ms=3); ax[i].fill_between(ks, [r["lo"][k] for k in ks], [r["hi"][k] for k in ks], alpha=0.2)
    ax[i].set_title(f"{lab} (n={r['n_treated']})" + ("" if r["pass_pre"] else "\nfails pre-trend rule"), fontsize=8); ax[i].set_xlabel("Years since takeoff", fontsize=8)
ax[0].set_ylabel("log GDP per capita x 100\nrelative to year -1", fontsize=8)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "figures", "event_study_cs.png"), dpi=140); plt.close()

# ----- A5 secondary outcomes (only for samples that passed the pre-trend rule) -----
L += ["## Secondary outcomes (takeoff at 10 per 100; only samples that pass the pre-trend rule)", "", "| Outcome | Sample | Treated | Pre-trend mean [95% CI] | Effect at +5 | Effect at +10 |", "|---|---|---|---|---|---|"]
for var, lab, logy in [("lifeexp", "Life expectancy (years)", False), ("u5mort", "Under-5 mortality (log x 100)", True), ("unemp", "Unemployment (pp)", False), ("agshare", "Agriculture share of value added (pp)", False), ("elecuse", "Electric power use per capita (log x 100)", True)]:
    Yv = piv(var)
    Yv = 100 * np.log(Yv.where(Yv > 0)) if logy else Yv
    for lab2, gs in SETS:
        if not res_main[(10, lab2)]["pass_pre"]:
            continue
        r = run(10, Yv, gs, lab2, [-5, -4, -3, -2, 5, 10])
        e5 = f"{r['pt'][5]:.2f} [{r['lo'][5]:.2f}, {r['hi'][5]:.2f}]" if not np.isnan(r['pt'][5]) else "n/a"
        e10 = f"{r['pt'][10]:.2f} [{r['lo'][10]:.2f}, {r['hi'][10]:.2f}]" if not np.isnan(r['pt'][10]) else "n/a"
        L.append(f"| {lab} | {lab2} | {r['n_treated']} | {r['pre_mean']:.2f} [{r['pre_ci'][0]:.2f}, {r['pre_ci'][1]:.2f}] ({'passes' if r['pass_pre'] else 'fails'}) | {e5} | {e10} |")
L.append("")

# ----- A7 local projections -----
rows = []
for iso in LY.index:
    if iso not in M.index:
        continue
    for t in range(1998, END - 0 + 1):
        m0, m3 = M.loc[iso].get(t), M.loc[iso].get(t - 3)
        y_t, y_t3 = LY.loc[iso].get(t), LY.loc[iso].get(t - 3)
        if pd.isna(m0) or pd.isna(m3) or pd.isna(y_t) or pd.isna(y_t3):
            continue
        row = dict(iso=iso, year=t, grp=grp[iso], shock=(m0 - m3) / 10, past=y_t - y_t3, y0=y_t)
        for h in range(0, 9):
            yh = LY.loc[iso].get(t + h) if t + h <= END else np.nan
            row[f"c{h}"] = yh - y_t if pd.notna(yh) else np.nan
        mf, yp = M.loc[iso].get(t + 3) if t + 3 <= END else np.nan, LY.loc[iso].get(t - 6)
        row["placebo_shock"] = (mf - m0) / 10 if pd.notna(mf) else np.nan
        row["placebo_y"] = (y_t3 - yp) if pd.notna(yp) else np.nan
        rows.append(row)
D = pd.DataFrame(rows)
L += ["## A7 local projections: cumulative growth of GDP per capita h years after a +10 change in mobile subscriptions per 100 over the previous three years", "", "Percentage points of cumulative growth; country and year fixed effects; standard errors clustered by country.", "", "| Group | Economies | h=0 | h=2 | h=4 | h=6 | h=8 |", "|---|---|---|---|---|---|---|"]
lp = {}
for h in range(0, 9):
    d = D.dropna(subset=[f"c{h}", "shock", "past"])
    r = smf.ols(f"c{h} ~ shock:C(grp) + past + y0 + C(iso) + C(year)", d).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d["iso"])[0]})
    for g in GR.values():
        k = f"shock:C(grp)[{g}]"
        lp[(g, h)] = (r.params[k], *r.conf_int().loc[k], d[d["grp"] == g]["iso"].nunique())
for g in GR.values():
    cells = []
    for h in (0, 2, 4, 6, 8):
        b, lo, hi, n = lp[(g, h)]
        cells.append(f"{b:.2f} [{lo:.2f}, {hi:.2f}]")
    L.append(f"| {g} | {lp[(g, 0)][3]} | " + " | ".join(cells) + " |")
dp = D.dropna(subset=["placebo_shock", "placebo_y", "past", "y0"])
rp = smf.ols("placebo_y ~ placebo_shock:C(grp) + y0 + C(iso) + C(year)", dp).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(dp["iso"])[0]})
L += ["", "Placebo (adoption change in the following three years against growth in the preceding three years; should be near zero if the dynamic profile is not driven by anticipation or trends):", "", "| Group | Placebo coefficient [95% CI] |", "|---|---|"]
for g in GR.values():
    k = f"placebo_shock:C(grp)[{g}]"
    ci = rp.conf_int().loc[k]
    L.append(f"| {g} | {rp.params[k]:.2f} [{ci[0]:.2f}, {ci[1]:.2f}] |")
L.append("")
fig, ax = plt.subplots(1, 1, figsize=(5.2, 3.4))
for g in GR.values():
    hs = list(range(9)); b = [lp[(g, h)][0] for h in hs]
    ax.plot(hs, b, marker="o", ms=3, label=g)
ax.axhline(0, color="grey", lw=0.8); ax.set_xlabel("Years after the adoption change"); ax.set_ylabel("Cumulative growth, pp per +10"); ax.legend(fontsize=7)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "figures", "lp.png"), dpi=140)
open(os.path.join(HERE, "results_event.md"), "w").write("\n".join(L) + "\n")
print("done")

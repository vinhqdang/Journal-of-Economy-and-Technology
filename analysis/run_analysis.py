"""Run analyses A1 to A6 from spec.md on analysis/data/wdi_panel.csv. Writes analysis/results.md and analysis/figures/."""
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

HERE = os.path.dirname(os.path.abspath(__file__))
P = pd.read_csv(os.path.join(HERE, "data", "wdi_panel.csv"))
END = int(sys.argv[1]) if len(sys.argv) > 1 else 2019
GROUPS = {"Low income": "1 Low", "Lower middle income": "2 Lower-middle", "Upper middle income": "3 Upper-middle", "High income": "4 High"}
P = P[P["income"].isin(GROUPS)].copy()
P["grp"] = P["income"].map(GROUPS)
P = P[P["year"] <= END]
W = {v: P.pivot(index="iso3", columns="year", values=v) for v in ["mobile", "internet", "broadband", "gdppc", "lifeexp", "u5mort", "unemp", "agshare", "co2pc", "elecuse", "secenr", "trade", "credit", "elecaccess"] if v in P}
grp = P.drop_duplicates("iso3").set_index("iso3")["grp"]
EDGES = [1995, 2000, 2005, 2010, 2015, END]
out = []

def near(var, iso, year, w=2):
    s = W[var].loc[iso] if iso in W[var].index else None
    if s is None:
        return np.nan
    for d in sorted(range(-w, w + 1), key=abs):
        v = s.get(year + d, np.nan)
        if pd.notna(v):
            return v
    return np.nan

def build(tech):
    rows = []
    isos = W["gdppc"].index
    for iso in isos:
        for p in range(len(EDGES) - 1):
            a, b = EDGES[p], EDGES[p + 1]
            y0, y1 = W["gdppc"].loc[iso].get(a, np.nan), W["gdppc"].loc[iso].get(b, np.nan)
            t0 = W[tech].loc[iso].get(a, np.nan) if iso in W[tech].index else np.nan
            t1 = W[tech].loc[iso].get(b, np.nan) if iso in W[tech].index else np.nan
            tr0, tr1 = near("trade", iso, a), near("trade", iso, b)
            rows.append(dict(iso=iso, grp=grp.get(iso), p=p, yrs=b - a, g=100 * (np.log(y1) - np.log(y0)) / (b - a) if pd.notna(y0) and pd.notna(y1) else np.nan,
                             t0=t0, dm=(t1 - t0) / 10 if pd.notna(t0) and pd.notna(t1) else np.nan, lny0=np.log(y0) if pd.notna(y0) else np.nan,
                             sec0=near("secenr", iso, a), dtrade=tr1 - tr0 if pd.notna(tr0) and pd.notna(tr1) else np.nan,
                             elec0=near("elecaccess", iso, a), credit0=near("credit", iso, a)))
    d = pd.DataFrame(rows).sort_values(["iso", "p"])
    d["g_prev"] = d.groupby("iso")["g"].shift(1)
    d["dm_prev"] = d.groupby("iso")["dm"].shift(1)
    return d

def fmt(b, lo, hi, p):
    return f"{b:.3f} [{lo:.3f}, {hi:.3f}] (p={p:.2f})"

def cluster(model, data):
    return model.fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(data["iso"])[0]})

out += [f"# Results of the macro-panel analysis (spec: `spec.md`)", "",
        f"Data: World Bank WDI, 1995 to {END}. Exploratory associations, not causal effects. Income groups are the current World Bank classification. Coefficients are in percentage points of annual GDP-per-capita growth per 10-unit change in the technology measure, with 95% confidence intervals from standard errors clustered by country. Cells with fewer than 15 economies are marked and not interpreted.", ""]

# ---------- A1 / A2 ----------
for tech, label in [("mobile", "mobile subscriptions per 100"), ("internet", "internet users, % of population"), ("broadband", "fixed broadband subscriptions per 100")]:
    d = build(tech)
    for name, regcol, extra, sub in [("A1 contemporaneous", "dm", "", d), ("A2 predetermined (previous-period change)", "dm_prev", " + g_prev", d[d["p"] >= 1])]:
        dd = sub.dropna(subset=["g", regcol, "lny0", "sec0", "dtrade"] + (["g_prev"] if "g_prev" in extra else [])).copy()
        if len(dd) < 60:
            out += [f"## {name}, {label}", "", f"Too few observations ({len(dd)}); not estimated.", ""]
            continue
        f = f"g ~ C(p) + C(grp) + lny0 + sec0 + dtrade{extra} + {regcol}:C(grp)"
        res = cluster(smf.ols(f, dd), dd)
        out += [f"## {name}, {label}", "", "| Income group | Economies | Observations | Effect of +10 on annual growth (pp) |", "|---|---|---|---|"]
        for gname in sorted(GROUPS.values()):
            key = f"{regcol}:C(grp)[{gname}]"
            n_c = dd[dd["grp"] == gname]["iso"].nunique(); n_o = (dd["grp"] == gname).sum()
            if key in res.params.index:
                ci = res.conf_int().loc[key]
                flag = " (fewer than 15 economies, not interpreted)" if n_c < 15 else ""
                out.append(f"| {gname[2:]} | {n_c} | {n_o} | {fmt(res.params[key], ci[0], ci[1], res.pvalues[key])}{flag} |")
        # country FE version
        f2 = f"g ~ C(p) + lny0 + sec0 + dtrade{extra} + {regcol}:C(grp) + C(iso)"
        r2 = cluster(smf.ols(f2, dd), dd)
        out += ["", "With country fixed effects added: " + "; ".join(f"{g[2:]} {r2.params[f'{regcol}:C(grp)[{g}]']:.3f} (p={r2.pvalues[f'{regcol}:C(grp)[{g}]']:.2f})" for g in sorted(GROUPS.values()) if f"{regcol}:C(grp)[{g}]" in r2.params.index), ""]
        if name.startswith("A1") and tech == "mobile":
            # A3 dose-response
            d3 = dd.copy()
            d3["bin"] = pd.cut(d3["t0"], [-np.inf, 10, 40, 80, np.inf], labels=["a <10", "b 10-40", "c 40-80", "d >80"])
            d3 = d3.dropna(subset=["bin"])
            out += ["## A3 dose-response by baseline mobile level (per 100 people at start of period)", "", "| Sample | Baseline bin | Obs | Effect of +10 on annual growth (pp) |", "|---|---|---|---|"]
            for lab, sel in [("All economies", d3), ("Low and lower-middle income", d3[d3["grp"].isin(["1 Low", "2 Lower-middle"])]), ("Upper-middle and high income", d3[d3["grp"].isin(["3 Upper-middle", "4 High"])])]:
                r3 = cluster(smf.ols("g ~ C(p) + lny0 + sec0 + dtrade + dm:C(bin)", sel), sel)
                for b_ in ["a <10", "b 10-40", "c 40-80", "d >80"]:
                    key = f"dm:C(bin)[{b_}]"
                    n_o = (sel["bin"] == b_).sum()
                    if key in r3.params.index and n_o >= 30:
                        ci = r3.conf_int().loc[key]
                        out.append(f"| {lab} | {b_[2:]} | {n_o} | {fmt(r3.params[key], ci[0], ci[1], r3.pvalues[key])} |")
                    else:
                        out.append(f"| {lab} | {b_[2:]} | {n_o} | not estimated (fewer than 30 observations) |")
            out.append("")
        if name.startswith("A1") and tech == "mobile":
            # A6 heterogeneity within low and lower-middle income
            lm = dd[dd["grp"].isin(["1 Low", "2 Lower-middle"])].copy()
            out += ["## A6 differences inside low and lower-middle income economies (mobile)", "", f"Sample: {lm['iso'].nunique()} economies, {len(lm)} observations. Each moderator is standardised and added to the mobile effect one at a time.", "", "| Moderator (at start of period) | Interaction with +10 mobile (pp growth per SD) | Obs |", "|---|---|---|"]
            for z, lab in [("sec0", "secondary enrolment"), ("elec0", "electricity access"), ("credit0", "private credit"), ("lny0", "log GDP per capita")]:
                l2 = lm.dropna(subset=[z]).copy()
                if len(l2) < 60:
                    out.append(f"| {lab} | not estimated | {len(l2)} |"); continue
                l2["z"] = (l2[z] - l2[z].mean()) / l2[z].std()
                r6 = cluster(smf.ols("g ~ C(p) + lny0 + sec0 + dtrade + dm + dm:z + z", l2) if z not in ("lny0", "sec0") else smf.ols("g ~ C(p) + lny0 + sec0 + dtrade + dm + dm:z", l2), l2)
                ci = r6.conf_int().loc["dm:z"]
                out.append(f"| {lab} | {fmt(r6.params['dm:z'], ci[0], ci[1], r6.pvalues['dm:z'])} | {len(l2)} |")
            out.append("")

# ---------- A4 / A5 event study ----------
def takeoff(tech="mobile", thr=10):
    t = {}
    s = W[tech]
    for iso in s.index:
        r = s.loc[iso].dropna()
        if 1995 not in r.index or r.loc[1995] >= thr:
            continue
        above = r[r >= thr]
        t[iso] = int(above.index.min()) if len(above) else None   # None = never in window
    return t

def stacked(yvar, to, isos_treat, isos_ctrl, logy, pre=5, post=10):
    rows = []
    for g in sorted({v for k, v in to.items() if v and k in isos_treat and 1996 <= v <= END - 3}):
        T = [k for k in isos_treat if to.get(k) == g]
        C_ = [k for k in isos_ctrl if to.get(k) is None or to[k] > g + post]
        for iso, tr in [(i, 1) for i in T] + [(i, 0) for i in C_]:
            for yr in range(max(1995, g - pre), min(END, g + post) + 1):
                v = W[yvar].loc[iso].get(yr, np.nan) if iso in W[yvar].index else np.nan
                if pd.notna(v) and (v > 0 or not logy):
                    rows.append(dict(iso=iso, coh=g, yr=yr, k=yr - g, tr=tr, y=100 * np.log(v) if logy else v))
    return pd.DataFrame(rows)

def demean(df, cols, keys, iters=40):
    X = df[cols].copy()
    for _ in range(iters):
        for key in keys:
            X = X - X.groupby(key).transform("mean")
    return X

def eventstudy(df, ks):
    d = df.copy()
    d["ci"] = d["coh"].astype(str) + "_" + d["iso"]
    d["cy"] = d["coh"].astype(str) + "_" + d["yr"].astype(str)
    for k in ks:
        d[f"e{k}"] = ((d["k"] == k) & (d["tr"] == 1)).astype(float)
    cols = [f"e{k}" for k in ks]
    Xd = demean(d, cols + ["y"], [d["ci"], d["cy"]])
    keep = Xd[cols].columns[(Xd[cols].abs().sum() > 1e-9).values]
    if len(keep) == 0 or d["tr"].nunique() < 2:
        return None, d
    m = __import__("statsmodels.api", fromlist=["OLS"]).OLS(Xd["y"], Xd[list(keep)]).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d["iso"])[0]})
    return m, d

to = takeoff()
treated_all = [k for k, v in to.items() if v]
KS = [k for k in range(-5, 11) if k != -1]
out += ["## A4 event study around the mobile takeoff (first year with at least 10 subscriptions per 100)", "",
        f"Economies below 10 per 100 in 1995: {len(to)}; of these {len(treated_all)} reach 10 by {END}. Window: 5 years before to 10 years after; reference year -1; stacked cohorts with clean controls (control economies reach 10 more than 10 years after the cohort year, or never by {END}); cohort-by-country and cohort-by-year fixed effects. Controls are drawn from the same income-group set as the treated economies (clarification of the spec). Outcome: log GDP per capita times 100, so a coefficient of 5 means GDP per capita about 5% higher than in the reference year, relative to controls.", ""]
def clean_controls(T, Cn):
    """Same-group clean controls if at least 8 exist for the stacked cohorts, otherwise controls from all groups (flagged)."""
    cohorts = {to[k] for k in T}
    ok = [k for k in Cn if to.get(k) is None or all(to[k] > g + 10 for g in cohorts)]
    ok_any = [k for k in Cn if to.get(k) is None or to[k] > min(cohorts) + 10]
    if len(ok_any) >= 8:
        return Cn, False
    allc = [k for k, v in to.items()]
    return allc, True

sets = [("All economies", list(GROUPS.values())), ("Low and lower-middle income", ["1 Low", "2 Lower-middle"]), ("Upper-middle income", ["3 Upper-middle"]), ("High income", ["4 High"])]
fig, ax = plt.subplots(1, 4, figsize=(13, 3.2), sharey=True)
out += ["| Sample | Treated economies | Control economies | Pre-trend (mean of -5 to -2) | Effect at +5 | Effect at +10 |", "|---|---|---|---|---|---|"]
es_store = {}
for i, (lab, gs) in enumerate(sets):
    T = [k for k in treated_all if grp.get(k) in gs]
    Cn = [k for k, v in to.items() if grp.get(k) in gs]
    if len(T) < 15:
        out.append(f"| {lab} | {len(T)} | {len([k for k in Cn if k not in T or True])} | fewer than 15 treated economies, not interpreted | | |")
        # still estimate descriptively for the plot? skip
        ax[i].set_title(f"{lab}\n(n<15, not shown)", fontsize=8); continue
    Cn, widened = clean_controls(T, Cn)
    df = stacked("gdppc", to, T, Cn, True)
    m, d = eventstudy(df, KS)
    if m is None:
        out.append(f"| {lab} | {len(T)} | 0 | no clean control economies; not estimated | | |")
        continue
    ctrl_n = d[d["tr"] == 0]["iso"].nunique()
    if widened:
        lab = lab + " (controls from all income groups)"
    pre = [f"e{k}" for k in (-5, -4, -3, -2) if f"e{k}" in m.params.index]
    pt = m.t_test(" + ".join(f"{c}" for c in pre) + f" = 0") if pre else None
    pre_mean = np.mean([m.params[c] for c in pre]) if pre else np.nan
    def eff(k):
        c = f"e{k}"
        if c not in m.params.index:
            return "n/a"
        ci = m.conf_int().loc[c]
        return f"{m.params[c]:.1f} [{ci[0]:.1f}, {ci[1]:.1f}]"
    out.append(f"| {lab} | {len(T)} | {ctrl_n} | {pre_mean:.1f} | {eff(5)} | {eff(10)} |")
    es_store[lab] = m
    ks = sorted(int(c[1:]) for c in m.params.index)
    b = [m.params[f"e{k}"] for k in ks]; ci = [m.conf_int().loc[f"e{k}"] for k in ks]
    ax[i].axhline(0, color="grey", lw=0.8); ax[i].axvline(-0.5, color="grey", lw=0.5, ls=":")
    ax[i].plot(ks, b, marker="o", ms=3); ax[i].fill_between(ks, [c[0] for c in ci], [c[1] for c in ci], alpha=0.2)
    ax[i].set_title(f"{lab} (n={len(T)})", fontsize=8); ax[i].set_xlabel("Years since takeoff", fontsize=8)
ax[0].set_ylabel("log GDP per capita x 100\nrelative to year -1", fontsize=8)
plt.tight_layout(); os.makedirs(os.path.join(HERE, "figures"), exist_ok=True); plt.savefig(os.path.join(HERE, "figures", "event_study.png"), dpi=140)
out += ["", "Figure: `figures/event_study.png`. Panels with fewer than 15 treated economies are left empty.", ""]

# A5 secondary outcomes
out += ["## A5 secondary outcomes around the mobile takeoff (effect at +5 and +10 years)", "", "| Outcome | Sample | Treated | Effect at +5 | Effect at +10 |", "|---|---|---|---|---|"]
for yv, lab, logy in [("lifeexp", "Life expectancy (years)", False), ("u5mort", "Under-5 mortality (log x 100)", True), ("unemp", "Unemployment (pp)", False), ("agshare", "Agriculture share of value added (pp)", False), ("co2pc", "CO2 per capita (log x 100)", True), ("elecuse", "Electric power use per capita (log x 100)", True)]:
    if yv not in W:
        out.append(f"| {lab} | not available from the API | | | |")
        continue
    for slab, gs in sets[:2] + sets[2:]:
        T = [k for k in treated_all if grp.get(k) in gs and k in W[yv].index and W[yv].loc[k].notna().sum() > 10]
        Cn = [k for k, v in to.items() if grp.get(k) in gs and k in W[yv].index]
        if len(T) < 15:
            continue
        Cn, widened = clean_controls(T, Cn)
        df = stacked(yv, to, T, Cn, logy)
        if len(df) < 200:
            continue
        m, d = eventstudy(df, KS)
        if m is None:
            continue
        if widened:
            slab = slab + " (controls from all groups)"
        def eff(k):
            c = f"e{k}"
            if c not in m.params.index:
                return "n/a"
            ci = m.conf_int().loc[c]
            return f"{m.params[c]:.2f} [{ci[0]:.2f}, {ci[1]:.2f}]"
        out.append(f"| {lab} | {slab} | {len(T)} | {eff(5)} | {eff(10)} |")
out.append("")
open(os.path.join(HERE, "results.md" if END == 2019 else f"results_end{END}.md"), "w").write("\n".join(out) + "\n")
print("done")

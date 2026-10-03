"""Exploratory analyses RQ2 to RQ10 (see review/extra_questions_spec.md). Writes review/extra_questions.md.

Inputs: review/data/mra_estimates.csv (via mra_pilot.py), review/data/extraction.json,
review/data/rq7_classified.json (optional, classification of moderation entries).
"""
import collections as C
import json
import os
import re
import runpy
import statistics as st

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.stats import fisher_exact

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
ns = runpy.run_path(os.path.join(HERE, "mra_pilot.py"))      # reruns the pilot; outputs are identical
m = ns["m"].copy()

ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
L = ["# Additional research questions: results (exploratory)", "",
     "Specified in `extra_questions_spec.md` before the analyses were run. Exploratory: no multiplicity correction, machine-extracted inputs, no human verification. A single p-value below 0.10 among these tests is a hypothesis, not a finding.", ""]

# ---------- RQ2 to RQ4: extra moderators in the meta-regression ----------
def years_mid(s):
    ys = [int(y) for y in re.findall(r"(?:19|20)\d\d", str(s))]
    return (min(ys) + max(ys)) / 2 if ys else np.nan

m["composite"] = m["exposure_variable"].fillna("").str.lower().str.contains(r"index|composite|pca|ictmi|desi|nri|maturity|digital economy").astype(int)
m["growth"] = m["outcome_transform"].fillna("").str.lower().str.contains("growth").astype(int)
m["midyear"] = m["years"].map(years_mid)
m["midyear_c"] = m["midyear"] - m["midyear"].mean()
base = ["lowmid", "gmm", "mobile", "internet"]
w = 1 / (m["se"] ** 2 + 0.01 ** 2)
L += ["## RQ2 to RQ4: extra moderators in the meta-regression", "",
      f"Same weighted regression as the pilot ({len(m)} estimates, {m['idx'].nunique()} papers, standard errors clustered by paper), adding one variable at a time to `lowmid`, `gmm`, `mobile` and `internet`.", "",
      "| Question | Added variable | Share of estimates with variable = 1 (or mean) | Coefficient | Clustered SE | p | Papers with variation |", "|---|---|---|---|---|---|---|"]
for q, var, lab in [("RQ2 measurement", "composite", "composite index as exposure"), ("RQ3 outcome form", "growth", "growth-rate outcome"), ("RQ4 time", "midyear_c", "sample midyear, centred (per year)")]:
    d = m.dropna(subset=[var]).copy()
    X = sm.add_constant(d[base + [var]].astype(float))
    res = sm.WLS(d["pcc"], X, weights=1 / (d["se"] ** 2 + 0.01 ** 2)).fit(cov_type="cluster", cov_kwds={"groups": pd.factorize(d["idx"])[0]})
    pv = d.groupby("idx")[var].nunique().gt(1).sum() if var != "midyear_c" else d["idx"].nunique()
    mean = d[var].mean()
    L.append(f"| {q} | {lab} | {mean:.2f} | {res.params[var]:.4f} | {res.bse[var]:.4f} | {res.pvalues[var]:.2f} | {pv} of {d['idx'].nunique()} |")
L += ["", "A coefficient on `composite` or `growth` is the average difference in partial correlation relative to single-indicator or level estimates. Several papers contribute estimates with the same value of the added variable, so these tests rest on between-paper contrasts and are weak.", ""]

# ---------- helpers on the 67 records ----------
def has_low(x):
    return bool(re.search(r"\blow\b(?!\s*-?\s*middle)", x["sample"]["income_groups_covered"].lower().replace("lower", "x")))
def ident_none(x):
    return x["design"]["identification"].lower().startswith("none")
def rob_mod(x):
    return x["overall_risk_of_bias"] == "moderate"
def fisher(a, b, c, d):
    o, p = fisher_exact([[a, b], [c, d]])
    return o, p

# ---------- RQ5 ----------
L += ["## RQ5: are weaker designs more common where low-income economies are sampled?", ""]
rows = []
for lab, f in [("No identification strategy (versus any)", ident_none), ("Moderate risk of bias (versus serious or critical)", rob_mod)]:
    a = sum(1 for x in ext if has_low(x) and f(x)); b = sum(1 for x in ext if has_low(x) and not f(x))
    c = sum(1 for x in ext if not has_low(x) and f(x)); d = sum(1 for x in ext if not has_low(x) and not f(x))
    o, p = fisher(a, b, c, d)
    rows.append(f"| {lab} | {a} of {a+b} ({100*a/(a+b):.0f}%) | {c} of {c+d} ({100*c/(c+d):.0f}%) | {o:.2f} | {p:.2f} |")
L += ["| Outcome | Studies listing a low-income economy | Studies not listing one | Odds ratio | Fisher p |", "|---|---|---|---|---|"] + rows
L += ["", f"{sum(1 for x in ext if has_low(x))} of {len(ext)} studies list at least one low-income economy; studies that report no income coverage are counted as not listing one, which biases the comparison toward the second column.", ""]

# ---------- RQ6 ----------
L += ["## RQ6: does study quality go with the reported direction for output?", ""]
f1 = [x for x in ext if any(y["family"] == 1 for y in x["results"])]
def all_pos(x):
    ds = {y["direction"] for y in x["results"] if y["family"] == 1}
    return ds == {"positive"}
def any_neg_or_null(x):
    ds = {y["direction"] for y in x["results"] if y["family"] == 1}
    return bool(ds & {"negative", "null"})
for lab, f in [("all family-1 results positive", all_pos), ("at least one negative or null family-1 result", any_neg_or_null)]:
    a = sum(1 for x in f1 if rob_mod(x) and f(x)); b = sum(1 for x in f1 if rob_mod(x) and not f(x))
    c = sum(1 for x in f1 if not rob_mod(x) and f(x)); d = sum(1 for x in f1 if not rob_mod(x) and not f(x))
    o, p = fisher(a, b, c, d)
    L.append(f"- {lab}: moderate-risk studies {a} of {a+b}; serious or critical {c} of {c+d}; odds ratio {o:.2f}, Fisher p = {p:.2f}.")
L += ["", f"Base: {len(f1)} studies with at least one output or productivity result. Most studies report several results, so \"all positive\" is a demanding criterion.", ""]

# ---------- RQ7 ----------
p7 = os.path.join(ROOT, "review/data/rq7_classified.json")
L += ["## RQ7: which enabling conditions are tested, and in which direction?", ""]
if os.path.exists(p7):
    cls = json.load(open(p7))
    c = C.Counter(); studies = C.defaultdict(set); dirs = C.defaultdict(C.Counter)
    for e in cls:
        t = e["moderator_type"]
        if t == "not_a_moderator":
            continue
        studies[t].add(e["idx"]); c[t] += 1; dirs[t][e["direction"]] += 1
    L += ["| Moderator | Studies | Entries | Amplifies | Dampens | Mixed | Null | Unclear | Formally tested entries |", "|---|---|---|---|---|---|---|---|---|"]
    for t, _ in sorted(c.items(), key=lambda kv: -len(studies[kv[0]])):
        ft = sum(1 for e in cls if e["moderator_type"] == t and e.get("tested_formally"))
        d = dirs[t]
        L.append(f"| {t} | {len(studies[t])} | {c[t]} | {d['amplifies']} | {d['dampens']} | {d['mixed']} | {d['null']} | {d['unclear']} | {ft} |")
    nm = sum(1 for e in cls if e["moderator_type"] == "not_a_moderator")
    L += ["", f"{len(cls)} heterogeneity entries from {len(ext)} studies; {nm} are not moderation tests (robustness, control sensitivity or descriptive remarks) and are left out of the table. Classification by one model reader; agreement with a second reader on a random 20% sample is in `data/rq7_agreement.json`.", ""]
else:
    L += ["Not yet run.", ""]

# ---------- RQ8 ----------
L += ["## RQ8: thresholds stated by the studies", "", "| Study | Moderator | Stated threshold |", "|---|---|---|"]
for x in sorted(ext, key=lambda t: int(t["idx"])):
    for h in x["heterogeneity"]:
        tv = h["threshold_value"].strip()
        if tv.lower() in ("none", "not reported", "") or tv.lower().startswith("none"):
            continue
        L.append(f"| {x['idx']} | {h['moderator']} | {tv[:110].replace('|','/')} |")
L += ["", "Thresholds are in different units and rest on one study each. They are listed, not pooled. Where two studies state a threshold for the same variable they do not agree in an obvious way (human capital: composite index of 2.35 in Africa, median splits elsewhere).", ""]

# ---------- RQ9 ----------
fam = {1: "Output and productivity", 2: "Structural change", 3: "Labour market", 4: "Poverty and distribution", 5: "Living standards", 6: "Resource cost"}
def groups(x):
    t = x["sample"]["income_groups_covered"].lower()
    g = []
    if re.search(r"\blow\b(?!\s*-?\s*middle)", t.replace("lower", "x")):
        g.append("low")
    if re.search(r"lower[- ]middle", t):
        g.append("lower-middle")
    if re.search(r"upper[- ]middle", t):
        g.append("upper-middle")
    if "high" in t or "oecd" in t:
        g.append("high")
    return g
L += ["## RQ9: evidence gap map (studies per outcome family and income-group coverage)", "", "A study counts in every income group its sample lists. Studies that report no income coverage appear only in the last column.", "",
      "| Outcome family | Low | Lower-middle | Upper-middle | High | Coverage not reported | Studies |", "|---|---|---|---|---|---|---|"]
for k, v in fam.items():
    ps = [x for x in ext if any(y["family"] == k for y in x["results"])]
    cnt = C.Counter(g for x in ps for g in groups(x))
    nr = sum(1 for x in ps if not groups(x))
    L.append(f"| {v} | {cnt['low']} | {cnt['lower-middle']} | {cnt['upper-middle']} | {cnt['high']} | {nr} | {len(ps)} |")
L.append("")

# ---------- RQ10 ----------
L += ["## RQ10: AI stream versus historical-wave stream", "", "| Measure | Historical waves (H) | AI (AI or both) |", "|---|---|---|"]
H = [x for x in ext if x["stream"] == "H"]; A = [x for x in ext if x["stream"] in ("AI", "both")]
def pct(g, f):
    return f"{sum(1 for x in g if f(x))} of {len(g)} ({100*sum(1 for x in g if f(x))/len(g):.0f}%)"
def nec(x):
    mm = re.search(r"\d+", x["sample"]["n_economies"].replace(",", ""))
    return int(mm.group(0)) if mm else None
def first_year(x):
    mm = re.search(r"(?:19|20)\d\d", x["sample"]["years"])
    return int(mm.group(0)) if mm else None
for lab, f in [("Moderate risk of bias", rob_mod), ("Critical risk of bias", lambda x: x["overall_risk_of_bias"] == "critical"), ("No identification strategy", ident_none),
               ("Compares income groups or regions", lambda x: any(h["moderator"] == "income group" for h in x["heterogeneity"])), ("Lists a low-income economy", has_low)]:
    L.append(f"| {lab} | {pct(H, f)} | {pct(A, f)} |")
for lab, f in [("Median number of economies", nec), ("Median first sample year", first_year)]:
    vh = [f(x) for x in H if f(x) is not None]; va = [f(x) for x in A if f(x) is not None]
    L.append(f"| {lab} | {st.median(vh):g} (n = {len(vh)}) | {st.median(va):g} (n = {len(va)}) |")
a = sum(1 for x in A if has_low(x)); c = sum(1 for x in H if has_low(x))
o, p = fisher(a, len(A) - a, c, len(H) - c)
L += ["", f"Low-income coverage, AI against historical: Fisher p = {p:.2f}. Counts are small (AI n = {len(A)}).", ""]
open(os.path.join(ROOT, "review/extra_questions.md"), "w").write("\n".join(L) + "\n")
print("written")

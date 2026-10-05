"""LaTeX appendix tables built from the project data: per-family study tables, meta-regression inputs, second-pass summary."""
import json
import os
import re

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
ext.sort(key=lambda x: int(x["idx"]))

def esc(s):
    s = str(s)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s

def tech(x):
    t = " ".join(x["technology"]).lower()
    out = [k for k, w in [("AI", "artificial|robot"), ("ICT", r"\bict\b|ict in general|ict capital|ict invest|ict spending|digital economy|telecom"), ("Mobile", "mobile|cellular"), ("Internet", "internet|broadband"), ("Crypto", "crypto")] if re.search(w, t)]
    return ", ".join(out) or "Other"

def estclass(x):
    e = x["design"]["estimator"].lower()
    if "gmm" in e:
        return "GMM"
    if re.search("ardl|coint|fmols|dols|amg|cce|mean group", e):
        return "ARDL/coint./heterog. panel"
    if re.search("fixed|ols|random|pooled|panel", e):
        return "FE/RE/OLS"
    return "Accounting/DEA/other"

def neco(x):
    m = re.search(r"\d+", x["sample"]["n_economies"].replace(",", ""))
    return m.group(0) if m else "n.r."

def yrs(x):
    y = re.findall(r"(?:19|20)\d\d", x["sample"]["years"])
    return f"{min(y)}--{max(y)}" if len(y) >= 2 else (y[0] if y else "n.r.")

FAM = {1: "Output and productivity", 2: "Structural change", 3: "Labour market", 4: "Poverty and distribution", 5: "Living standards beyond income", 6: "Resource cost"}
SYM = {"positive": r"$+$", "negative": r"$-$", "null": "0", "mixed": "mixed", "not reported": "n.r."}
L = []
for f, name in FAM.items():
    ps = [x for x in ext if any(r["family"] == f for r in x["results"])]
    L += [r"{\scriptsize", r"\begin{longtable}{@{}r l r l l p{3.6cm} l@{}}",
          rf"\caption{{Studies reporting {name.lower()} outcomes (n = {len(ps)}). ``Directions'' counts the study's results in this family: $+$ positive, $-$ negative, 0 null, m mixed. Technology codes as in Table~\ref{{tab:included}}.}}\label{{tab:fam{f}}}\\",
          r"\toprule ID & Tech. & Econ. & Years & Estimator & Directions & RoB \\ \midrule \endfirsthead",
          r"\toprule ID & Tech. & Econ. & Years & Estimator & Directions & RoB \\ \midrule \endhead", r"\bottomrule \endfoot"]
    for x in ps:
        c = {k: sum(1 for r in x["results"] if r["family"] == f and r["direction"] == k) for k in ("positive", "negative", "null", "mixed")}
        dirs = ", ".join(f"{v}{s}" for v, s in [(c["positive"], "+"), (c["negative"], "$-$"), (c["null"], "0"), (c["mixed"], "m")] if v)
        L.append(" & ".join([x["idx"], tech(x), neco(x["sample"] and x), yrs(x), estclass(x), dirs, x["overall_risk_of_bias"]]) + r" \\")
    L += [r"\end{longtable}", "}", ""]
open(os.path.join(HERE, "app_families.tex"), "w").write("\n".join(L))

# meta-regression inputs
d = pd.read_csv(os.path.join(ROOT, "review/data/mra_effect_sizes.csv"), dtype={"idx": str})
d["k"] = d["idx"].astype(int)
d = d.sort_values(["k", "estimate_id"])
rows = [f"{r['estimate_id']} & {esc(r['role'])} & {int(r['n']) if pd.notna(r['n']) else 'n.r.'} & {r['pcc']:.3f} & {r['se']:.3f}" for _, r in d.iterrows()]
half = (len(rows) + 1) // 2
left, right = rows[:half], rows[half:] + [""] * (half - len(rows[half:]))
HDR = r"Estimate & Role & Obs. & PCC & SE"
L = [r"{\scriptsize", r"\begin{longtable}{@{}l l r r r@{\hspace{1.2em}}l l r r r@{}}",
     r"\caption{Estimates used in the meta-regression (" + f"{len(d)} estimates from {d['idx'].nunique()} studies" + r"): partial correlation (PCC) and its standard error, computed from the printed coefficient and uncertainty with degrees of freedom equal to observations minus 10. The second half of the list continues in the right-hand block; $t$-statistics are in the repository file \texttt{mra\_effect\_sizes.csv}.}\label{tab:mrainputs}\\",
     r"\toprule " + HDR + " & " + HDR + r" \\ \midrule \endfirsthead",
     r"\toprule " + HDR + " & " + HDR + r" \\ \midrule \endhead", r"\bottomrule \endfoot"]
for l, r in zip(left, right):
    L.append(l + " & " + (r if r else " & & & & ") + r" \\")
L += [r"\end{longtable}", "}"]
open(os.path.join(HERE, "app_mra.tex"), "w").write("\n".join(L))

# second pass summary
L = [r"{\scriptsize", r"\begin{longtable}{@{}r r r r r l@{}}",
     r"\caption{Second-pass check by study: results confirmed (C), corrected (X) or unverifiable (U), heterogeneity entries corrected, and the second reader's view of the overall risk-of-bias rating.}\label{tab:secondpass}\\",
     r"\toprule ID & C & X & U & Het. X & RoB view \\ \midrule \endfirsthead", r"\toprule ID & C & X & U & Het. X & RoB view \\ \midrule \endhead", r"\bottomrule \endfoot"]
for x in ext:
    s = x.get("second_pass")
    if not s:
        L.append(rf"{x['idx']} & \multicolumn{{5}}{{l}}{{not second-passed}} \\")
        continue
    r_, h_ = s["results"], s["heterogeneity"]
    L.append(f"{x['idx']} & {r_.get('confirmed', 0)} & {r_.get('corrected', 0)} & {r_.get('unverifiable', 0)} & {h_.get('corrected', 0)} & {esc((s['risk_of_bias_overall_opinion'] or '').replace('_', ' '))}" + r" \\")
L += [r"\end{longtable}", "}"]
open(os.path.join(HERE, "app_secondpass.tex"), "w").write("\n".join(L))
print("tables done", len(ext))

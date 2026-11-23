"""Human verification sheet for the headline contrasts used in the meta-analysis.
Writes verification/contrast_verification_sheet.{tex,csv}; compile the .tex with pdflatex."""
import csv, json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "..", "manuscript"))
from citekeys import key, CIT
C = {c["idx"]: c for c in json.load(open(os.path.join(ROOT, "data", "contrasts_all.json"))) if c.get("headline")}
E = json.load(open(os.path.join(ROOT, "data", "contrast_effects.json")))
def esc(s):
    s = re.sub(r"[一-鿿]+", "", str(s if s is not None else "")).replace("Δ", "change in ").replace("−", "-")
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", "-"), ("^", "")]:
        s = s.replace(a, b)
    return s
def unc(c, g):
    if c.get(f"se_{g}") is not None: return f"SE {c[f'se_{g}']}"
    if c.get(f"t_{g}") is not None: return f"t {c[f't_{g}']}"
    return ""
rows = []
for n, e in enumerate(sorted(E, key=lambda e: key(e["idx"]).lower()), 1):
    c = C[e["idx"]]
    if c["design"] == "interaction":
        rich = f"interaction {c.get('b_inter')} ({unc(c, 'inter')}), N {c.get('n_obs_inter')}"; poor = "--"
    else:
        rich = f"{c.get('b_rich')} ({unc(c, 'rich')}), N {c.get('n_obs_rich')}"; poor = f"{c.get('b_poor')} ({unc(c, 'poor')}), N {c.get('n_obs_poor')}"
    rows.append({"n": n, "study": key(e["idx"]), "doi": CIT[e["idx"]]["doi"], "outcome": c.get("outcome"), "technology": c.get("technology"),
                 "groups": f"{c.get('richer_group')} vs {c.get('poorer_group')}", "richer": rich, "poorer": poor, "direction": c["direction"],
                 "evidence": c.get("evidence"), "flag": "yes" if c.get("plausibility_flag") else ""})
os.makedirs(os.path.join(ROOT, "verification"), exist_ok=True)
w = csv.DictWriter(open(os.path.join(ROOT, "verification", "contrast_verification_sheet.csv"), "w", newline=""), fieldnames=list(rows[0]) + ["ok", "correction"])
w.writeheader(); w.writerows(rows)
L = [r"\documentclass[10pt,a4paper]{article}", r"\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage{lmodern}\usepackage[landscape,margin=1.3cm]{geometry}\usepackage{longtable,array,booktabs,url}\makeatletter\g@addto@macro\UrlBreaks{\do\.\do\-\do\/}\makeatother",
     r"\begin{document}\small", r"\section*{Verification sheet: the %d headline income contrasts used in the meta-analysis}" % len(rows),
     r"For each row, open the source paper, find the table named in the evidence column and check, for the richer and the poorer group (or the interaction term): the coefficient (including its sign), the uncertainty and its type (standard error or $t$), and the number of observations. Check also that the two groups come from the same specification and that the direction is right in terms of benefit (for inequality, poverty, emissions and similar outcomes a larger reduction is a larger benefit). Tick OK or write the correction. Rows marked F were flagged as implausible or unverifiable by the model check.",
     r"\par\medskip\scriptsize", r"\begin{longtable}{@{}p{0.4cm}p{2.4cm}p{2.6cm}p{3.0cm}p{2.6cm}p{2.6cm}p{1.5cm}p{5.6cm}p{0.3cm}p{1.0cm}p{1.6cm}@{}}",
     r"\toprule \# & Study & Outcome / technology & Groups (richer vs poorer) & Richer: b (unc.), N & Poorer: b (unc.), N & Direction & Evidence (table, page, quote) & F & OK? & Correction\\ \midrule \endhead"]
for r in rows:
    st = esc(r["study"]) + (r" \newline \url{" + r["doi"] + "}" if r["doi"] else "")
    L.append(" & ".join([esc(r["n"]), st] + [esc(x) for x in [f"{r['outcome']} / {r['technology']}", r["groups"], r["richer"], r["poorer"], r["direction"], r["evidence"], "F" if r["flag"] else "", "", ""]]) + r" \\ \midrule")
L += [r"\end{longtable}", r"\par\medskip\normalsize Contrasts checked: \underline{\hspace{2cm}} \quad Corrections: \underline{\hspace{2cm}} \quad Date: \underline{\hspace{3cm}}", r"\end{document}"]
open(os.path.join(ROOT, "verification", "contrast_verification_sheet.tex"), "w").write("\n".join(L) + "\n")
print(len(rows), "rows")

"""Compare an independent (blind) re-extraction of key fields for a random sample of included studies with the original extraction.

Usage: python3 review/scripts/double_extraction_agreement.py <blind_outputs.json> <sample_ids.json>
Writes review/data/double_extraction_agreement.json and review/double_extraction.md.
"""
import collections as C
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
blind = {b["idx"]: b for b in json.load(open(sys.argv[1]))}
ids = json.load(open(sys.argv[2]))
ext = {x["idx"]: x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json")))}

def first_int(s):
    m = re.search(r"\d+", str(s).replace(",", ""))
    return int(m.group(0)) if m else None

def years(s):
    y = [int(v) for v in re.findall(r"(?:19|20)\d\d", str(s))]
    return (min(y), max(y)) if y else (None, None)

def est_class(x):
    e = x["design"]["estimator"].lower()
    if "gmm" in e:
        return "GMM"
    if re.search("ardl|coint|fmols|dols|amg|cce|mean group", e):
        return "ARDL_coint_het"
    if re.search("fixed|ols|random|pooled|panel", e):
        return "FE_RE_OLS"
    return "accounting_DEA_other"

def coverage(x):
    t = x["sample"]["income_groups_covered"].lower()
    t = re.sub(r"\bno (?:[a-z-]+ or )?(?:low|high)[^;).]*", "", t)
    return bool(re.search(r"\blow\b(?!\s*-?\s*middle)", t.replace("lower", "x")))

rows = []
for i in ids:
    x, b = ext[i], blind[i]
    f1 = [r["direction"] for r in x["results"] if r["family"] == 1]
    yo = years(x["sample"]["years"])
    ec_b = b["estimator_class"]
    ec_b = "accounting_DEA_other" if ec_b in ("accounting_DEA", "other") else ("FE_RE_OLS" if ec_b == "IV_2SLS" else ec_b)
    n_o, n_b = first_int(x["sample"]["n_economies"]), b.get("n_economies")
    ident_o = "none" if x["design"]["identification"].lower().startswith("none") else "some"
    ident_b = "none" if b["identification"] == "none" else "some"
    fam_o, fam_b = sorted({r["family"] for r in x["results"]}), sorted(set(b["outcome_families"]))
    tech_o = set(t.lower() for t in x["technology"])
    rows.append(dict(idx=i,
        n_economies=(n_o is not None and n_b is not None and abs(n_o - n_b) <= max(1, 0.05 * max(n_o, n_b))),
        year_first=(yo[0] == b.get("year_first")), year_last=(yo[1] == b.get("year_last")),
        estimator_class=(est_class(x) == ec_b), gmm_vs_not=((est_class(x) == "GMM") == (ec_b == "GMM")),
        identification_none_vs_some=(ident_o == ident_b),
        outcome_families_exact=(fam_o == fam_b), outcome_families_jaccard=len(set(fam_o) & set(fam_b)) / max(1, len(set(fam_o) | set(fam_b))),
        headline_direction=((f1[0] if f1 else "not_applicable") == b["headline_output_direction"]),
        income_group_comparison=(any(h["moderator"] == "income group" for h in x["heterogeneity"]) == bool(b["income_group_comparison"])),
        low_income_listed=(coverage(x) == bool(b["low_income_economy_listed"]) if b.get("low_income_economy_listed") is not None else None),
        overall_risk_of_bias=(x["overall_risk_of_bias"] == b["overall_risk_of_bias"]),
        detail=dict(n=(n_o, n_b), years=(yo, (b.get("year_first"), b.get("year_last"))), est=(est_class(x), ec_b), ident=(x["design"]["identification"], b["identification"]), fam=(fam_o, fam_b), dir=((f1[0] if f1 else None), b["headline_output_direction"]), rob=(x["overall_risk_of_bias"], b["overall_risk_of_bias"]), low=(coverage(x), b.get("low_income_economy_listed")))))
n = len(rows)
fields = ["n_economies", "year_first", "year_last", "estimator_class", "gmm_vs_not", "identification_none_vs_some", "outcome_families_exact", "headline_direction", "income_group_comparison", "low_income_listed", "overall_risk_of_bias"]
res = {}
L = ["# Blind double extraction: agreement with the original extraction", "",
     f"A separate model run extracted key fields from {n} randomly chosen included studies without seeing the original extraction (seed 20261004). Agreement is the share of studies on which the two extractions give the same value. This measures consistency of reading, not truth; where the two disagree the paper's text decides.", "",
     "| Field | Agreeing | Share |", "|---|---|---|"]
for f in fields:
    vals = [r[f] for r in rows if r[f] is not None]
    k = sum(vals); res[f] = dict(agree=k, n=len(vals))
    L.append(f"| {f} | {k} of {len(vals)} | {100*k/len(vals):.0f}% |")
res["outcome_families_mean_jaccard"] = sum(r["outcome_families_jaccard"] for r in rows) / n
L += ["", f"Mean overlap (Jaccard) of the outcome-family sets: {res['outcome_families_mean_jaccard']:.2f}.", "", "## Disagreements", "", "| Study | Field | Original | Blind |", "|---|---|---|---|"]
D = {"n_economies": "n", "year_first": "years", "year_last": "years", "estimator_class": "est", "identification_none_vs_some": "ident", "outcome_families_exact": "fam", "headline_direction": "dir", "overall_risk_of_bias": "rob", "low_income_listed": "low"}
for r in rows:
    for f, key in D.items():
        if r[f] is False:
            o, bl = r["detail"][key]
            L.append(f"| {r['idx']} | {f} | {o} | {bl} |")
json.dump(dict(fields=res, rows=rows), open(os.path.join(ROOT, "review/data/double_extraction_agreement.json"), "w"), indent=1)
open(os.path.join(ROOT, "review/double_extraction.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L[:20]))

"""Attach the second-pass check (a separate reading of each paper against the extracted record) to
review/data/extraction.json and write review/second_pass_verification.md.

Inputs: review/data/second_pass/ft_ver_*.json (full-text records) and mra_ver_*.json (regression estimates).
Run after merge_extractions.py. Idempotent.
"""
import collections as C
import glob
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
D = os.path.join(ROOT, "review/data")
ext = json.load(open(os.path.join(D, "extraction.json")))
by = {x["idx"]: x for x in ext}

ft = {}
for f in glob.glob(os.path.join(D, "second_pass/ft_ver_*.json")):
    for p in json.load(open(f)):
        ft[p["idx"]] = p
mra = {}
for f in glob.glob(os.path.join(D, "second_pass/mra_ver_*.json")):
    for p in json.load(open(f)):
        mra[p["idx"]] = p

# Direction fixes where the second pass found the first-pass direction wrong against the printed numbers
# (study 9103: a panel-VAR table read from the wrong cell; study 9101: both estimates positive).
# The first-pass value is kept in direction_first_pass. Idempotent.
DIRECTION_FIXES = {"9101": {4: "positive"}, "9103": {n: "positive" for n in range(1, 12)}, "9203": {2: "mixed"}, "9302": {5: "mixed"}}
for idx, fixes in DIRECTION_FIXES.items():
    rec = by.get(idx)
    if rec:
        for n, d in fixes.items():
            r = rec["results"][n - 1]
            if r["direction"] != d:
                r.setdefault("direction_first_pass", r["direction"])
                r["direction"] = d

for idx, p in ft.items():
    rec = by.get(idx)
    if not rec:
        continue
    res = C.Counter(r["verdict"] for r in p.get("results", []))
    het = C.Counter(r["verdict"] for r in p.get("heterogeneity", []))
    rec["second_pass"] = {
        "results": dict(res), "heterogeneity": dict(het),
        "eligibility_ok": p.get("eligibility_ok"), "eligibility_note": p.get("eligibility_note", ""),
        "risk_of_bias_overall_opinion": (p.get("risk_of_bias") or {}).get("overall"),
        "sample_corrections": p.get("sample_corrections") or {},
        "corrections": [r for r in p.get("results", []) + p.get("heterogeneity", []) if r["verdict"] != "confirmed"],
        "problems": p.get("problems", ""),
    }
json.dump(ext, open(os.path.join(D, "extraction.json"), "w"), indent=1, ensure_ascii=False)

inc = [x for x in ext if x["fulltext_decision"] == "include" and "second_pass" in x]
res_tot, het_tot = C.Counter(), C.Counter()
for x in inc:
    for k, v in x["second_pass"]["results"].items():
        res_tot[k] += v
    for k, v in x["second_pass"]["heterogeneity"].items():
        het_tot[k] += v
rob_op = C.Counter(x["second_pass"]["risk_of_bias_overall_opinion"] for x in inc)
mra_c = C.Counter(e["verdict"] for p in mra.values() for e in p["estimates"])
elig = [(x["idx"], x["fulltext_decision"], x["second_pass"]["eligibility_note"][:220]) for x in ext
        if "second_pass" in x and x["second_pass"]["eligibility_ok"] is False]
rob_diff = [(x["idx"], x["overall_risk_of_bias"], x["second_pass"]["risk_of_bias_overall_opinion"]) for x in inc
            if x["second_pass"]["risk_of_bias_overall_opinion"] not in ("agree", None)]

L = ["# Second-pass check of the extractions", "",
     "**What this is.** After the first extraction, every included paper's record and every regression estimate used in the pilot meta-regression was checked a second time against the converted full text by a separate model run that had the record and the text, not the first run's reasoning. This catches transcription and reading errors. It is not a human check, it uses the same family of model as the first pass, and it reads the same machine-converted text (garbled tables stay garbled). The author's own hand check of a random sample against the source papers is recorded in `data/human_check.md`.", "",
     "## Regression estimates for the meta-regression", "",
     f"- Estimates checked: {sum(mra_c.values())} from {len(mra)} papers. Confirmed: {mra_c['confirmed']}; corrected: {mra_c['corrected']}; unverifiable: {mra_c['unverifiable']}; not applicable: {mra_c['not_applicable']}.",
     f"- {mra_c['corrected']} estimates were corrected: 245-10 (income label changed to a combined middle-income group) and the five estimates of study 9103, which had been read from the wrong cell of a panel-VAR table (rows are equations, columns are lagged regressors; the paper itself reads the table the other way). Study 9103 reports p-values, so its estimates are not converted in the pilot in any case. Five further estimates were excluded as not poolable (`data/mra_exclusions.csv`): 358 (exposure is fintech credit, not ICT adoption), 88-11 to 88-14 (growth outcome mixed with level outcomes) and 988-5 (TFP index in levels).",
     "- Many papers carry pooling warnings in `data/second_pass/mra_ver_*.json` (composite indices instead of single technologies, conditional main effects when interactions are present, overlapping specifications on one sample, generated TFP outcomes). 302 and 323 share authors, panel and index, so they are not independent.", "",
     "## Full-text records (papers still included or excluded after this check)", "",
     f"- Included records checked: {len(inc)}. Results: confirmed {res_tot['confirmed']}, corrected {res_tot['corrected']}, unverifiable {res_tot['unverifiable']}. Heterogeneity items: confirmed {het_tot['confirmed']}, corrected {het_tot['corrected']}.",
     f"- The checker's view of the overall risk-of-bias rating: agree {rob_op['agree']}, too lenient {rob_op['too_lenient']}, too harsh {rob_op['too_harsh']}. The ratings in the record were not changed; the differences are listed below for a human to settle.", ""]
if rob_diff:
    L += ["| Paper | Record says | Checker says |", "|---|---|---|"] + [f"| {a} | {b} | {c} |" for a, b, c in sorted(rob_diff, key=lambda t: int(t[0]))] + [""]
L += ["## Eligibility changes and flags", "",
      "Four papers were moved from include to exclude after this check (reversible, human to confirm): 298 (no own estimation, E4), 1495 (number of economies never stated, E1), 878 (outcomes are trade ratios, not in the six families, E3) and 474 (too few economies, E1). Other papers flagged as borderline and still included: 442 (no effect estimate reported; only Granger and cointegration tests), 1645 (methods written in the future tense; no coefficients in the tables), 392 (accounting decomposition, not regression), 1026 and 174 (industrial robots as the AI measure), 913 (called AI by the author; built from innovation questions), 320 and 1428 (financial-inclusion outcomes, which the protocol counts as family 5).", "",
      "Checker's eligibility notes:", ""] + [f"- {i} ({d}): {n}" for i, d, n in elig] + [""]
L += ["## Corrections by paper", "", "Each item below is a result or heterogeneity entry where the checker found the record wrong or unsupported. Full text of each correction, with quotes and locators, is in `data/extraction.json` under `second_pass.corrections`.", ""]
for x in sorted(inc, key=lambda t: int(t["idx"])):
    c = x["second_pass"]["corrections"]
    if c:
        L.append(f"- **{x['idx']}**: " + " | ".join((r.get("correction") or r.get("note") or "")[:170] for r in c))
open(os.path.join(ROOT, "review/second_pass_verification.md"), "w").write("\n".join(L) + "\n")
print(len(inc), dict(res_tot), dict(het_tot), dict(rob_op), dict(mra_c))

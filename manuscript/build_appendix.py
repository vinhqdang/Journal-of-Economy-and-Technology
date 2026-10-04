"""Build the appendix table of included studies (manuscript/appendix_studies.tex) from review/data."""
import csv, json, os, re, sys

csv.field_size_limit(sys.maxsize)
ROOT = os.path.join(os.path.dirname(__file__), "..")
rows = {r["idx"]: r for r in csv.DictReader(open(os.path.join(ROOT, "review/data/abstract_stage_decisions.csv"), encoding="utf-8"))}
for _r in csv.DictReader(open(os.path.join(ROOT, "review/data/added_records.csv"), encoding="utf-8")):
    rows.setdefault(_r["idx"], _r)

ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
ext.sort(key=lambda x: int(x["idx"]))

def esc(s):
    s = str(s)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s

def n_econ(s):
    m = re.search(r"\d+", s["n_economies"].replace(",", ""))
    return m.group(0) if m else "n.r."

def techs(x):
    t = " ".join(x["technology"]).lower()
    out = []
    for k, w in [("AI", "artificial|robot"), ("ICT", r"\bict\b|ict in general|ict capital|ict invest|ict spending|digital economy|telecom"), ("Mobile", "mobile|cellular"), ("Internet", "internet|broadband"), ("Crypto", "crypto")]:
        if re.search(w, t):
            out.append(k)
    return ", ".join(out) or "Other"

lines = [r"{\scriptsize", r"\begin{longtable}{@{}r r p{4.9cm} p{1.5cm} r l p{3.7cm}@{}}",
         r"\caption{Studies included in the synthesis (n = %d). Authors are not listed because the extraction database does not store them; the DOI identifies each record. n.r. = not reported. RoB = overall risk of bias in the first-pass rating (moderate, serious, critical); no study was rated low.}\label{tab:included}\\" % len(ext),
         r"\toprule ID & Year & Title & Technology & Econ. & RoB & DOI \\ \midrule \endfirsthead",
         r"\toprule ID & Year & Title & Technology & Econ. & RoB & DOI \\ \midrule \endhead", r"\bottomrule \endfoot"]
for x in ext:
    r = rows[x["idx"]]
    doi = r["doi"] or ""
    lines.append(" & ".join([x["idx"], r["year"], esc(x["title"]), techs(x), n_econ(x["sample"]), esc(x["overall_risk_of_bias"]), (r"\url{https://doi.org/%s}" % doi.replace("%", r"\%").replace("#", r"\#")) if doi else "n.a."]) + r" \\")
lines += [r"\end{longtable}", "}"]
open(os.path.join(os.path.dirname(__file__), "appendix_studies.tex"), "w").write("\n".join(lines) + "\n")
print(len(ext), "studies;", sum(1 for x in ext if not rows[x['idx']]['doi']), "without DOI")

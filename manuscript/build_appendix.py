"""Build the appendix table of included studies (manuscript/appendix_studies.tex) from review/data."""
import csv, json, os, re, sys

csv.field_size_limit(sys.maxsize)
ROOT = os.path.join(os.path.dirname(__file__), "..")
rows = {r["idx"]: r for r in csv.DictReader(open(os.path.join(ROOT, "review/data/abstract_stage_decisions.csv"), encoding="utf-8"))}
for _r in csv.DictReader(open(os.path.join(ROOT, "review/data/added_records.csv"), encoding="utf-8")):
    rows.setdefault(_r["idx"], _r)

ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
from citekeys import CIT, key
ext.sort(key=lambda x: key(x["idx"]).lower())

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

def refline(i, x):
    c = CIT[i]
    au = [a.strip() for a in c["authors"].split(";") if a.strip()]
    def ini(a):
        fam, _, giv = a.partition(",")
        g = "".join(p[0] + "." for p in re.split(r"[ -]+", giv.strip()) if p)
        return f"{fam.strip()}, {g}"
    names = "; ".join(ini(a) for a in au)
    return rf"\textbf{{{esc(key(i))}}}. {esc(names)} ({c['year']}). {esc(c['title'])}. \emph{{{esc(c['venue'])}}}."

lines = [r"{\scriptsize", r"\begin{longtable}{@{}p{7.4cm} p{1.3cm} r l p{3.4cm}@{}}",
         r"\caption{Studies included in the evidence map (n = %d), in alphabetical order of the in-text citation. Technology: AI, ICT in general, mobile, internet or broadband, crypto-assets. Econ. = number of economies (n.r. = not reported). RoB = overall risk of bias (moderate, serious, critical); no study was rated low. Authors and years follow the Crossref record or, where none exists, the paper itself.}\label{tab:included}\\" % len(ext),
         r"\toprule Reference & Technology & Econ. & RoB & DOI \\ \midrule \endfirsthead",
         r"\toprule Reference & Technology & Econ. & RoB & DOI \\ \midrule \endhead", r"\bottomrule \endfoot"]
for x in ext:
    r = rows[x["idx"]]
    doi = CIT[x["idx"]]["doi"] or r["doi"] or ""
    lines.append(" & ".join([refline(x["idx"], x), techs(x), n_econ(x["sample"]), esc(x["overall_risk_of_bias"]), (r"\url{https://doi.org/%s}" % doi.replace("%", r"\%").replace("#", r"\#")) if doi else "n.a."]) + r" \\")
lines += [r"\end{longtable}", "}"]
open(os.path.join(os.path.dirname(__file__), "appendix_studies.tex"), "w").write("\n".join(lines) + "\n")
print(len(ext), "studies;", sum(1 for x in ext if not (CIT[x['idx']]['doi'] or rows[x['idx']]['doi'])), "without DOI")

"""Fetch author lists for the included studies from Crossref (by DOI, else by title match) and write
review/data/study_citations.csv (idx, key, authors, year, title, venue, doi, source, confidence).
Studies Crossref cannot resolve are written with an empty authors field for manual completion."""
import csv, difflib, json, os, re, sys, time, urllib.parse, urllib.request
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
D = os.path.join(ROOT, "review/data")
ext = [x for x in json.load(open(os.path.join(D, "extraction.json"))) if x["fulltext_decision"] == "include"]
meta = {r["idx"]: r for r in csv.DictReader(open(os.path.join(D, "abstract_stage_decisions.csv"), encoding="utf-8"))}
for r in csv.DictReader(open(os.path.join(D, "added_records.csv"))):
    meta.setdefault(r["idx"], r)
out_path = os.path.join(D, "study_citations.csv")
done = {}
if os.path.exists(out_path):
    done = {r["idx"]: r for r in csv.DictReader(open(out_path, encoding="utf-8")) if r["authors"]}

def get(url):
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "evidence-map-citation-check"}), timeout=30))
        except Exception:
            time.sleep(2)
    return None

def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"<[^>]+>", " ", t or "").lower()).split()

def fmt(m):
    au = m.get("author") or []
    return "; ".join(f"{a.get('family','')}, {a.get('given','')}".strip(", ") for a in au if a.get("family"))

rows = []
for x in ext:
    i = x["idx"]
    if i in done:
        rows.append(done[i]); continue
    m = meta.get(i, {})
    title = m.get("title", "")
    doi = (m.get("doi") or "").replace("https://doi.org/", "")
    msg, src, conf = None, "", ""
    if doi:
        j = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        if j and j.get("message", {}).get("author"):
            msg, src, conf = j["message"], "crossref-doi", "high"
    if not msg and title:
        j = get("https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(title))
        for it in (j or {}).get("message", {}).get("items", []):
            t2 = (it.get("title") or [""])[0]
            ratio = difflib.SequenceMatcher(None, norm(title), norm(t2)).ratio()
            if ratio > 0.85 and it.get("author"):
                msg, src, conf = it, "crossref-title", f"title match {ratio:.2f}"; break
    if msg:
        yr = ((msg.get("issued") or {}).get("date-parts") or [[None]])[0][0] or m.get("year", "")
        rows.append(dict(idx=i, authors=fmt(msg), year=yr, title=(msg.get("title") or [title])[0], venue=(msg.get("container-title") or [""])[0], doi=msg.get("DOI", doi), source=src, confidence=conf))
    else:
        rows.append(dict(idx=i, authors="", year=m.get("year", ""), title=title, venue=m.get("venue", ""), doi=doi, source="unresolved", confidence="manual"))
    time.sleep(0.3)

def surname(a):
    return a.split(",")[0].strip()
keys = {}
for r in rows:
    au = [surname(a) for a in r["authors"].split(";") if a.strip()]
    if not au: k = f"Study{r['idx']}"
    elif len(au) == 1: k = au[0]
    elif len(au) == 2: k = f"{au[0]} and {au[1]}"
    else: k = f"{au[0]} et al."
    r["key"] = f"{k} ({r['year']})"
for r in rows:
    r["idx"] = str(r["idx"])
cols = ["idx", "key", "authors", "year", "title", "venue", "doi", "source", "confidence"]
w = csv.DictWriter(open(out_path, "w", newline="", encoding="utf-8"), fieldnames=cols)
w.writeheader(); w.writerows(rows)
print(len(rows), "resolved", sum(1 for r in rows if r["authors"]), "unresolved", [r["idx"] for r in rows if not r["authors"]])

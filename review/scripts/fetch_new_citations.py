"""Bibliographic details for newly included studies (OpenAlex). Appends rows to data/study_citations.csv
with idx = OpenAlex work id. Usage: python3 fetch_new_citations.py"""
import csv, json, os, subprocess, time
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
P = os.path.join(ROOT, "study_citations.csv")
rows = list(csv.DictReader(open(P))); have = {r["idx"] for r in rows}; fields = list(rows[0])
ns = [s for s in json.load(open(os.path.join(ROOT, "new_studies.json"))) if s["eligibility"] == "include"]
def get(u):
    for k in range(6):
        try: return json.loads(subprocess.run(["curl", "-s", "--max-time", "40", u], capture_output=True).stdout)
        except Exception: time.sleep(3 + 3 * k)
    return {}
for s in ns:
    if s["idx"] in have: continue
    w = get(f"https://api.openalex.org/works/{s['idx']}?select=title,authorships,publication_year,primary_location,doi,biblio")
    names = [a["author"]["display_name"] for a in w.get("authorships", [])]
    def fmt(n):
        p = n.split(); return (p[-1] + ", " + " ".join(x[0] + "." for x in p[:-1])) if len(p) > 1 else n
    auth = "; ".join(fmt(n) for n in names[:6]) + (" et al." if len(names) > 6 else "")
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    b = w.get("biblio") or {}
    venue = src + (f" {b['volume']}" if b.get("volume") else "") + (f"({b['issue']})" if b.get("issue") else "") + (f", {b['first_page']}-{b['last_page']}" if b.get("first_page") and b.get("last_page") else "")
    r = {k: "" for k in fields}
    r.update({"idx": s["idx"], "key": "", "authors": auth, "year": str(w.get("publication_year") or ""), "title": w.get("title") or s["title"], "venue": venue,
              "doi": (w.get("doi") or "").replace("https://doi.org/", ""), "source": "openalex", "confidence": "openalex"})
    rows.append(r); time.sleep(0.3)
w = csv.DictWriter(open(P, "w", newline=""), fieldnames=fields); w.writeheader(); w.writerows(rows)
print("rows", len(rows))

"""Supplementary OpenAlex search for studies that compare income groups (no field restriction).
Usage: python3 openalex_income_search.py out.csv [exclude.csv ...]"""
import csv, json, os, re, subprocess, sys, time, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
Q = ('("information and communication technology" OR ICT OR internet OR broadband OR "mobile phone" OR "mobile phones" OR "mobile telephony" '
     'OR "mobile cellular" OR "digital economy" OR digitalization OR "artificial intelligence" OR robots) AND '
     '("economic growth" OR productivity OR "GDP per capita" OR inequality OR poverty OR employment OR "human development" OR emissions) AND '
     '("income groups" OR "income group" OR "low-income countries" OR "high-income countries" OR "middle-income countries" OR '
     '"developed and developing" OR "developing and developed" OR "by income level" OR "OECD and non-OECD")')
def get(url):
    for k in range(10):
        b = subprocess.run(["curl", "-s", "--max-time", "60", url], capture_output=True).stdout
        try:
            d = json.loads(b)
            if "error" in d: raise ValueError(d["error"])
            time.sleep(0.5); return d
        except Exception: time.sleep(3 + 5 * k)
    return {}
def norm(t): return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:80]
seen_doi, seen_t = set(), set()
files = [os.path.join(ROOT, f) for f in ["title_screen_input.csv", "abstract_stage_decisions.csv", "added_records.csv", "study_citations.csv"]] + sys.argv[2:]
for f in files:
    for r in csv.DictReader(open(f, encoding="utf-8")):
        if r.get("doi"): seen_doi.add(r["doi"].lower().replace("https://doi.org/", ""))
        seen_t.add(norm(r.get("title")))
F = "id,doi,title,publication_year,primary_location,abstract_inverted_index,cited_by_count,type"
flt = "title_and_abstract.search:" + Q + ",from_publication_date:1995-01-01,type:article|preprint"
rows, page, total, got = [], 1, None, 0
while page:
    r = get(f"https://api.openalex.org/works?per-page=200&select={F}&filter={urllib.parse.quote(flt, safe=':,|')}&page={page}")
    total = (r.get("meta") or {}).get("count", total)
    got += len(r.get("results", []))
    for x in r.get("results", []):
        doi = (x.get("doi") or "").lower().replace("https://doi.org/", "")
        if (doi and doi in seen_doi) or norm(x.get("title")) in seen_t: continue
        inv = x.get("abstract_inverted_index") or {}
        ab = " ".join(t for _, t in sorted((p, t) for t, ps in inv.items() for p in ps))
        loc = x.get("primary_location") or {}
        rows.append({"id": x["id"].split("/")[-1], "doi": doi, "year": x.get("publication_year"), "title": x.get("title"),
                     "venue": (loc.get("source") or {}).get("display_name"), "type": x.get("type"), "cited": x.get("cited_by_count"), "abstract": ab})
    page = page + 1 if len(r.get("results", [])) == 200 and page < 50 else None
print("hits", total, "retrieved", got, "new", len(rows))
w = csv.DictWriter(open(sys.argv[1], "w", newline="", encoding="utf-8"), fieldnames=["id", "doi", "year", "title", "venue", "type", "cited", "abstract"])
w.writeheader(); w.writerows(rows)

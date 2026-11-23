"""Backward and forward citation searching in OpenAlex from seed studies.
Usage: python3 citation_chase.py seeds.json out.csv
seeds.json: list of study ids (study_citations.csv) or DOIs (strings starting with 10.).
Output: one row per new record (not already among the screened records), with abstract."""
import csv, json, os, re, subprocess, sys, time, urllib.parse
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
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
for f in ["title_screen_input.csv", "abstract_stage_decisions.csv", "added_records.csv", "study_citations.csv"]:
    for r in csv.DictReader(open(os.path.join(ROOT, f), encoding="utf-8")):
        if r.get("doi"): seen_doi.add(r["doi"].lower().replace("https://doi.org/", ""))
        seen_t.add(norm(r.get("title")))
cit = {r["idx"]: r for r in csv.DictReader(open(os.path.join(ROOT, "study_citations.csv")))}
def resolve(s):
    doi = s if s.startswith("10.") else (cit.get(s, {}).get("doi") or "")
    if doi:
        w = get("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi.lower()))
        if w.get("id"): return w
    if s in cit:
        r = get("https://api.openalex.org/works?per-page=1&search=" + urllib.parse.quote(cit[s]["title"][:200]))
        if r.get("results"): return r["results"][0]
    return None
def abstract(w):
    inv = w.get("abstract_inverted_index") or {}
    pos = sorted((p, t) for t, ps in inv.items() for p in ps)
    return " ".join(t for _, t in pos)
F = "id,doi,title,publication_year,primary_location,abstract_inverted_index,cited_by_count,type"
seeds = json.load(open(sys.argv[1])); found = {}
for s in seeds:
    w = resolve(s)
    if not w: print("unresolved", s); continue
    wid = w["id"].split("/")[-1]
    refs = [r.split("/")[-1] for r in w.get("referenced_works") or []]
    for k in range(0, len(refs), 50):
        r = get("https://api.openalex.org/works?per-page=50&select=" + F + "&filter=openalex:" + "|".join(refs[k:k + 50]))
        for x in r.get("results", []): found.setdefault(x["id"], (x, set()))[1].add("backward:" + s)
    page = 1
    while page:
        r = get(f"https://api.openalex.org/works?per-page=200&select={F}&filter=cites:{wid}&page={page}")
        for x in r.get("results", []): found.setdefault(x["id"], (x, set()))[1].add("forward:" + s)
        page = page + 1 if len(r.get("results", [])) == 200 and page < 50 else None
    print(s, "refs", len(refs), "total", len(found)); time.sleep(0.2)
rows = []
for x, src in found.values():
    doi = (x.get("doi") or "").lower().replace("https://doi.org/", "")
    if (doi and doi in seen_doi) or norm(x.get("title")) in seen_t: continue
    loc = x.get("primary_location") or {}
    rows.append({"id": x["id"].split("/")[-1], "doi": doi, "year": x.get("publication_year"), "title": x.get("title"),
                 "venue": ((loc.get("source") or {}).get("display_name")), "type": x.get("type"), "cited": x.get("cited_by_count"),
                 "n_seeds": len(src), "sources": ";".join(sorted(src)), "abstract": abstract(x)})
w = csv.DictWriter(open(sys.argv[2], "w", newline="", encoding="utf-8"), fieldnames=list(rows[0]))
w.writeheader(); w.writerows(sorted(rows, key=lambda r: -r["n_seeds"]))
print("new records", len(rows), "of", len(found))

"""Download open-access PDFs for a list of study ids via OpenAlex locations.
Usage: python3 fetch_oa_pdfs.py ids.json outdir   (study ids from review/data/study_citations.csv or OpenAlex work ids W...)
Writes outdir/<idx>.pdf and prints a status line per study."""
import csv, json, os, sys, time, urllib.parse, urllib.request
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ids = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
cit = {r["idx"]: r for r in csv.DictReader(open(os.path.join(ROOT, "data", "study_citations.csv")))}
UA = {"User-Agent": "Mozilla/5.0 (research literature retrieval)"}
import subprocess
def get(url, t=60):
    return subprocess.run(["curl", "-s", "-L", "--max-time", str(t), "-A", UA["User-Agent"], url], capture_output=True).stdout
def work(r):
    if r.get("doi"):
        try: return json.loads(get("https://api.openalex.org/works/doi:" + urllib.parse.quote(r["doi"].lower())))
        except Exception: pass
    q = urllib.parse.quote(r["title"][:200])
    res = json.loads(get(f"https://api.openalex.org/works?search={q}&per-page=1"))["results"]
    return res[0] if res else None
for i in ids:
    p = os.path.join(out, f"{i}.pdf")
    if os.path.exists(p) and os.path.getsize(p) > 20000: print(i, "have"); continue
    r = cit.get(i)
    if not r and not i.startswith("W"): print(i, "no-citation"); continue
    try: w = json.loads(get("https://api.openalex.org/works/" + i)) if i.startswith("W") else work(r)
    except Exception as e: print(i, "openalex-error", e); continue
    urls = []
    fs = json.load(open(os.path.join(ROOT, "data", "fulltext_status.json"))).get(i) or {} if not i.startswith("W") else {}
    if fs.get("source"): urls.append(fs["source"])
    if w:
        for loc in [w.get("best_oa_location")] + (w.get("locations") or []):
            if loc and loc.get("pdf_url"): urls.append(loc["pdf_url"])
        for loc in w.get("locations") or []:
            if loc and loc.get("landing_page_url") and "arxiv" in loc["landing_page_url"]: urls.append(loc["landing_page_url"].replace("/abs/", "/pdf/"))
    ok = False
    for u in dict.fromkeys(urls):
        try:
            b = get(u)
            if b[:4] == b"%PDF" and len(b) > 20000:
                open(p, "wb").write(b); ok = True; print(i, "ok", u[:80]); break
        except Exception: pass
    if not ok: print(i, "none", len(urls), "urls")
    time.sleep(0.3)

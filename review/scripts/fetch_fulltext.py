"""Look for every free, legal full-text copy of the records sent to full-text assessment.

For each included record this collects all open locations OpenAlex knows about
(publisher open access, repository copies, preprints), tries to download each PDF,
and checks that the first page contains words from the title, so a wrong file is
not accepted. Downloaded files stay outside the repository.

The OpenAlex key is read from OPENALEX_API_KEY and is never written to disk.

Usage: python3 review/scripts/fetch_fulltext.py <output_dir>
"""
import concurrent.futures as cf
import csv
import json
import os
import re
import subprocess
import sys
import time

import requests

csv.field_size_limit(sys.maxsize)
HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, "..", "data")
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (systematic-review pilot)"}
OA = {"Authorization": "Bearer " + os.environ["OPENALEX_API_KEY"], "User-Agent": "systematic-review-pilot/1.0"}
STOP = set("the of and in on for to a an with from by is are as at its their how does do what why evidence study analysis effect effects impact role".split())


def words(t):
    return [w for w in re.findall(r"[a-z]{4,}", t.lower()) if w not in STOP]


def pdf_matches(path, title):
    try:
        txt = subprocess.run(["pdftotext", "-l", "2", path, "-"], capture_output=True, text=True, timeout=60).stdout.lower()
    except Exception:
        return False
    ws = words(title)[:8]
    if not ws:
        return True
    hit = sum(1 for w in ws if w in txt)
    return hit >= max(2, int(0.6 * len(ws)))


def locations(r):
    key = r["id"]
    if key.startswith("oa:"):
        url = f"https://api.openalex.org/works/{key[3:]}"
        params = {"select": "locations,open_access"}
    elif r["doi"]:
        url = "https://api.openalex.org/works/https://doi.org/" + r["doi"]
        params = {"select": "locations,open_access"}
    else:
        return []
    for i in range(3):
        try:
            resp = requests.get(url, headers=OA, params=params, timeout=40)
            if resp.status_code == 200:
                d = resp.json()
                urls = []
                for loc in d.get("locations") or []:
                    if loc.get("pdf_url"):
                        urls.append(loc["pdf_url"])
                for loc in d.get("locations") or []:
                    if loc.get("is_oa") and loc.get("landing_page_url"):
                        urls.append(loc["landing_page_url"])
                if (d.get("open_access") or {}).get("oa_url"):
                    urls.append(d["open_access"]["oa_url"])
                seen, out = set(), []
                for u in urls:
                    if u not in seen:
                        seen.add(u)
                        out.append(u)
                return out
            time.sleep(2 * (i + 1))
        except requests.RequestException:
            time.sleep(2 * (i + 1))
    return []


def semantic_scholar(doi):
    if not doi:
        return []
    try:
        resp = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                            params={"fields": "openAccessPdf"}, timeout=30, headers=UA)
        if resp.status_code == 200:
            u = (resp.json().get("openAccessPdf") or {}).get("url")
            return [u] if u else []
    except requests.RequestException:
        pass
    return []


def try_download(urls, idx, title):
    for u in urls:
        try:
            resp = requests.get(u, headers=UA, timeout=40, allow_redirects=True)
        except requests.RequestException:
            continue
        if resp.status_code == 200 and resp.content[:4] == b"%PDF":
            p = os.path.join(OUT, f"{idx}.pdf")
            open(p, "wb").write(resp.content)
            if pdf_matches(p, title):
                return u
            os.rename(p, os.path.join(OUT, f"{idx}_mismatch.pdf"))
    return None


def work(r):
    idx = r["idx"]
    if os.path.exists(os.path.join(OUT, f"{idx}.pdf")):
        return idx, "have", None
    urls = locations(r)
    got = try_download(urls, idx, r["title"])
    if got:
        return idx, "found", got
    got = try_download(semantic_scholar(r["doi"]), idx, r["title"])
    if got:
        return idx, "found_s2", got
    return idx, "none", urls[:3]


def main():
    rows = [r for r in csv.DictReader(open(os.path.join(DATA, "abstract_stage_decisions.csv"), encoding="utf-8"))
            if r["decision"] in ("INC", "REV")]
    res = {}
    with cf.ThreadPoolExecutor(6) as ex:
        for idx, st, info in ex.map(work, rows):
            res[idx] = {"status": st, "source": info if st != "none" else None, "tried": info if st == "none" else None}
    json.dump(res, open(os.path.join(DATA, "fulltext_status.json"), "w"), indent=1)
    c = {}
    for v in res.values():
        c[v["status"]] = c.get(v["status"], 0) + 1
    print(c)


if __name__ == "__main__":
    main()

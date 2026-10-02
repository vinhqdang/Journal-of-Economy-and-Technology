"""Pilot search for the systematic review (see review/protocol.md).

Sources reachable without credentials: Crossref (journal articles), NBER
working papers, arXiv (econ categories). Each query is a technology term
paired with a context term, because these services do not support the full
Boolean strategy. Every query, hit count and retrieval time is logged.

Usage: python3 review/scripts/search.py crossref|nber|arxiv
"""
import csv
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET

import requests

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)
HEADERS = {"User-Agent": "systematic-review-pilot/1.0"}

TECH = [
    "internet", "broadband", "mobile phones", "information and communication technology",
    "digital technology", "artificial intelligence", "generative AI", "machine learning",
    "cryptocurrency", "bitcoin", "technology diffusion", "general purpose technology",
]
CONTEXT = [
    "cross-country panel economic growth", "developing countries income groups",
    "digital divide", "poverty and inequality countries", "productivity emerging economies",
    "employment and wages across countries", "absorptive capacity human capital",
    "financial inclusion",
]
FROM_YEAR = 1995


def get(url, params=None, tries=4):
    for i in range(tries):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=40)
            if r.status_code == 200:
                return r
            time.sleep(2 * (i + 1))
        except requests.RequestException:
            time.sleep(2 * (i + 1))
    return None


def clean(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", text).strip()


def crossref(q):
    r = get("https://api.crossref.org/works", {
        "query.bibliographic": q, "rows": 30,
        "filter": f"from-pub-date:{FROM_YEAR}-01-01,type:journal-article",
        "select": "DOI,title,issued,abstract,container-title,type",
    })
    if not r:
        return 0, []
    m = r.json()["message"]
    rows = []
    for rank, it in enumerate(m["items"], 1):
        parts = (it.get("issued", {}).get("date-parts") or [[None]])[0]
        rows.append({
            "id": "doi:" + it["DOI"].lower(), "title": clean((it.get("title") or [""])[0]),
            "year": parts[0], "venue": clean((it.get("container-title") or [""])[0]),
            "abstract": clean(it.get("abstract", "")), "type": "journal-article", "rank": rank,
        })
    return m.get("total-results", 0), rows


def nber(q):
    r = get("https://www.nber.org/api/v1/working_page_listing/contentType/working_paper/_/_/search",
            {"page": 1, "perPage": 30, "q": q})
    if not r:
        return 0, []
    d = r.json()
    rows = []
    for rank, it in enumerate(d["results"], 1):
        ym = re.search(r"(19|20)\d\d", it.get("displaydate") or "")
        year = int(ym.group(0)) if ym else None
        if year and year < FROM_YEAR:
            continue
        rows.append({
            "id": "nber:" + (it.get("url") or "").rsplit("/", 1)[-1], "title": clean(it.get("title")),
            "year": year, "venue": "NBER Working Paper", "abstract": clean(it.get("abstract")),
            "type": "working-paper", "rank": rank,
        })
    return d.get("totalResults", 0), rows


def arxiv(q):
    cats = "(cat:econ.GN+OR+cat:econ.EM+OR+cat:econ.TH)"
    terms = "+AND+".join(f"all:{urllib.parse.quote(w)}" for w in q.split()[:6])
    url = f"https://export.arxiv.org/api/query?search_query={cats}+AND+{terms}&max_results=30"
    r = get(url)
    if not r:
        return 0, []
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
    root = ET.fromstring(r.text)
    total = int(root.findtext("o:totalResults", "0", ns))
    rows = []
    for rank, e in enumerate(root.findall("a:entry", ns), 1):
        year = int((e.findtext("a:published", "0000", ns) or "0000")[:4])
        if year < FROM_YEAR:
            continue
        rows.append({
            "id": "arxiv:" + e.findtext("a:id", "", ns).rsplit("/abs/", 1)[-1],
            "title": clean(e.findtext("a:title", "", ns)), "year": year, "venue": "arXiv preprint",
            "abstract": clean(e.findtext("a:summary", "", ns)), "type": "preprint", "rank": rank,
        })
    time.sleep(3)
    return total, rows


BLOCK_A = ['"information and communication technology"', '"information and communication technologies"',
           "ICT", "internet", "broadband", '"mobile phone"', '"mobile phones"', '"mobile telephony"',
           '"mobile telephone"', "smartphone*", '"digital technology"', '"digital technologies"',
           '"digital economy"', '"artificial intelligence"', '"machine learning"', '"deep learning"',
           '"generative AI"', '"large language model"', '"large language models"',
           '"general purpose technology"', '"general-purpose technology"',
           '"general purpose technologies"', "cryptocurrenc*", "bitcoin", '"crypto-asset"',
           '"crypto-assets"', "blockchain"]
BLOCK_B = ["countr*", '"cross-country"', '"cross country"', "nation*", '"developing economy"',
           '"developing economies"', '"emerging economy"', '"emerging economies"', "low-income",
           "middle-income", "high-income", '"income group"', '"income groups"',
           '"developed economy"', '"developed economies"', '"advanced economy"',
           '"advanced economies"']
BLOCK_C = ["growth", "productivity", "GDP", "poverty", "inequality", "employment", "wage*",
           '"labor share"', '"labour share"', '"structural transformation"', '"financial inclusion"',
           "welfare", '"living standard"', '"living standards"', '"human development"']
BLOCK_D = ["heterogene*", '"absorptive capacity"', "complementar*", "threshold*", '"human capital"',
           '"digital divide"', "convergence", "divergence", '"technology diffusion"',
           '"technology adoption"', "leapfrog*"]
# Amendment 1 (see protocol revision log): restricted to the Economics, Econometrics and Finance
# field because the unrestricted query returned ~7,600 records. OpenAlex needs the .exact field
# for wildcards, so phrases with wildcards inside quotes were written out as variants.
OA_FIELD = "20"


def abstract_from_index(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def openalex():
    key = os.environ["OPENALEX_API_KEY"]  # never written to disk
    hdr = {"Authorization": "Bearer " + key, "User-Agent": HEADERS["User-Agent"]}
    blocks = ["(" + " OR ".join(b) + ")" for b in (BLOCK_A, BLOCK_B, BLOCK_C, BLOCK_D)]
    q = " AND ".join(blocks)
    flt = (f"title_and_abstract.search.exact:{q},from_publication_date:{FROM_YEAR}-01-01,"
           f"type:article|preprint,language:en,primary_topic.field.id:{OA_FIELD}")
    with open(os.path.join(OUT, "openalex_query.txt"), "w") as f:
        f.write(flt + "\n")
    sel = ("id,doi,title,publication_year,abstract_inverted_index,type,primary_location,"
           "open_access,cited_by_count,primary_topic")
    rows, cursor, total = [], "*", 0
    while cursor:
        r = requests.get("https://api.openalex.org/works", headers=hdr, timeout=120, params={
            "filter": flt, "per-page": 200, "cursor": cursor, "select": sel})
        if r.status_code != 200:
            print("error", r.status_code, r.text[:200])
            break
        d = r.json()
        total = d["meta"]["count"]
        for it in d["results"]:
            loc = it.get("primary_location") or {}
            src = (loc.get("source") or {}).get("display_name") or ""
            oa = it.get("open_access") or {}
            rows.append({
                "source": "openalex", "query": "protocol-boolean", "rank": len(rows) + 1,
                "id": "oa:" + it["id"].rsplit("/", 1)[-1], "doi": (it.get("doi") or "").replace("https://doi.org/", "").lower(),
                "title": clean(it.get("title")), "year": it.get("publication_year"), "venue": src,
                "type": it.get("type"), "abstract": clean(abstract_from_index(it.get("abstract_inverted_index"))),
                "cited": it.get("cited_by_count"), "oa_url": oa.get("oa_url") or "",
                "landing": loc.get("landing_page_url") or "",
            })
        cursor = d["meta"].get("next_cursor")
        time.sleep(0.3)
    cols = ["source", "query", "rank", "id", "doi", "title", "year", "venue", "type", "abstract",
            "cited", "oa_url", "landing"]
    with open(os.path.join(OUT, "raw_openalex.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(OUT, "log_openalex.json"), "w") as f:
        json.dump([{"source": "openalex", "query": "protocol-boolean (see openalex_query.txt)",
                    "total_hits": total, "retrieved": len(rows),
                    "time": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"}], f, indent=1)
    print("openalex total:", total, "retrieved:", len(rows))


def main(source):
    if source == "openalex":
        return openalex()
    fn = {"crossref": crossref, "nber": nber, "arxiv": arxiv}[source]
    # arXiv is rate-limited, so it uses a smaller query set
    pairs = [(t, c) for t in TECH for c in CONTEXT]
    if source == "arxiv":
        pairs = [(t, c) for t in TECH for c in CONTEXT[:4]]
    records, log = [], []
    for t, c in pairs:
        q = f"{t} {c}"
        total, rows = fn(q)
        log.append({"source": source, "query": q, "total_hits": total, "retrieved": len(rows),
                    "time": datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"})
        for row in rows:
            row["source"], row["query"] = source, q
            records.append(row)
        time.sleep(0.4)
    cols = ["source", "query", "rank", "id", "title", "year", "venue", "type", "abstract"]
    with open(os.path.join(OUT, f"raw_{source}.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows([{k: r.get(k) for k in cols} for r in records])
    with open(os.path.join(OUT, f"log_{source}.json"), "w") as f:
        json.dump(log, f, indent=1)
    print(source, "queries:", len(log), "records:", len(records))


if __name__ == "__main__":
    main(sys.argv[1])

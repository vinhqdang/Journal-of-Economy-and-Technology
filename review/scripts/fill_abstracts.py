"""Fill missing abstracts by looking up DOIs in OpenAlex.

Reads review/data/records_dedup.csv, looks up records that have a DOI but no
abstract, writes review/data/abstract_fill.csv (doi, abstract, oa_url).
The API key is read from the OPENALEX_API_KEY environment variable and is never
written to disk.
"""
import csv
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(__file__))
from search import abstract_from_index, clean  # noqa: E402

csv.field_size_limit(sys.maxsize)
DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def main():
    hdr = {"Authorization": "Bearer " + os.environ["OPENALEX_API_KEY"], "User-Agent": "systematic-review-pilot/1.0"}
    dois = []
    with open(os.path.join(DATA, "records_dedup.csv"), newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["doi"] and not r["abstract"]:
                dois.append(r["doi"])
    out, found = [], 0
    for i in range(0, len(dois), 50):
        chunk = dois[i:i + 50]
        flt = "doi:" + "|".join("https://doi.org/" + d for d in chunk)
        r = requests.get("https://api.openalex.org/works", headers=hdr, timeout=120, params={
            "filter": flt, "per-page": 50, "select": "doi,abstract_inverted_index,open_access"})
        if r.status_code != 200:
            print("error", r.status_code, r.text[:150])
            continue
        for it in r.json()["results"]:
            ab = clean(abstract_from_index(it.get("abstract_inverted_index")))
            if ab:
                found += 1
            out.append({"doi": (it.get("doi") or "").replace("https://doi.org/", "").lower(),
                        "abstract": ab, "oa_url": (it.get("open_access") or {}).get("oa_url") or ""})
        time.sleep(0.3)
    with open(os.path.join(DATA, "abstract_fill.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["doi", "abstract", "oa_url"])
        w.writeheader()
        w.writerows(out)
    print("dois looked up:", len(dois), "abstracts found:", found)


if __name__ == "__main__":
    main()

"""Merge, deduplicate and apply automated stage-1 screening rules.

Stage 1 only removes records that clearly fail the eligibility table. Everything
that passes goes to manual title/abstract reading (stage 2). Records without an
abstract cannot be judged on content and are kept apart, not guessed.

Usage: python3 review/scripts/screen.py
"""
import csv
import json
import os
import re
import sys

csv.field_size_limit(sys.maxsize)
DATA = os.path.join(os.path.dirname(__file__), "..", "data")
SOURCES = ["openalex", "crossref", "nber", "arxiv"]

TECH = re.compile(
    r"\b(ict|icts|information and communication technolog\w*|internet|broadband|mobile (phone|phones|telephon\w*|money|banking|internet|technolog\w*)|"
    r"smartphone\w*|digital (technolog\w*|economy|transformation|divide|financial|infrastructure)|artificial intelligence|ai|machine learning|deep learning|"
    r"generative|large language model\w*|general[- ]purpose technolog\w*|cryptocurrenc\w*|bitcoin|crypto[- ]?assets?|blockchain|technology (diffusion|adoption))\b", re.I)
MULTI = re.compile(
    r"(cross[- ]country|multi[- ]?country|multiple countries|across countries|\b\d{2,3}\s+(countries|economies|nations)\b|panel (of|data)|developing (countries|economies|nations)|"
    r"emerging (markets?|economies)|income[- ]group\w*|low[- ]income|middle[- ]income|high[- ]income|oecd|asean|brics|g7|g20|sub-saharan|"
    r"advanced economies|developed (countries|economies)|worldwide|global sample|countries)", re.I)
OUTC = re.compile(
    r"\b(growth|productivity|gdp|poverty|inequality|employment|wage\w*|labou?r share|structural (transformation|change)|financial inclusion|welfare|"
    r"living standard\w*|human development|income|consumption|unemployment|jobs?|convergence|divergence)\b", re.I)
HET = re.compile(
    r"(heterogene\w*|absorptive capacity|complementar\w*|threshold\w*|human capital|digital divide|convergence|divergence|technology diffusion|technology adoption|"
    r"leapfrog\w*|income level|enabling|moderat\w*|non-?linear\w*|depends on|differ\w* (across|between|by))", re.I)


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def load():
    recs = []
    for s in SOURCES:
        p = os.path.join(DATA, f"raw_{s}.csv")
        if not os.path.exists(p):
            continue
        with open(p, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                r["source"] = s
                recs.append(r)
    return recs


def main():
    recs = load()
    identified = {}
    for r in recs:
        identified[r["source"]] = identified.get(r["source"], 0) + 1

    # per-source distinct records first (queries overlap), then cross-source deduplication
    seen_src, distinct = set(), []
    for r in recs:
        k = (r["source"], r["id"])
        if k in seen_src:
            continue
        seen_src.add(k)
        distinct.append(r)
    distinct_by_src = {}
    for r in distinct:
        distinct_by_src[r["source"]] = distinct_by_src.get(r["source"], 0) + 1

    by_doi, by_title, merged = {}, {}, []
    order = {s: i for i, s in enumerate(SOURCES)}
    for r in sorted(distinct, key=lambda x: order[x["source"]]):
        doi = (r.get("doi") or (r["id"][4:] if r["id"].startswith("doi:") else "")).lower()
        tkey = (norm_title(r["title"]), str(r.get("year") or ""))
        hit = by_doi.get(doi) if doi else None
        hit = hit or by_title.get(tkey)
        if hit is not None:
            hit["also_in"] = (hit.get("also_in", "") + "," + r["source"]).strip(",")
            if not hit.get("abstract") and r.get("abstract"):
                hit["abstract"] = r["abstract"]
            continue
        r["doi"] = doi
        r["also_in"] = ""
        merged.append(r)
        if doi:
            by_doi[doi] = r
        by_title[tkey] = r

    fill = {}
    fp = os.path.join(DATA, "abstract_fill.csv")
    if os.path.exists(fp):
        with open(fp, newline="", encoding="utf-8") as f:
            fill = {r["doi"]: r for r in csv.DictReader(f)}
    for r in merged:
        if not r.get("abstract") and r["doi"] in fill and fill[r["doi"]]["abstract"]:
            r["abstract"] = fill[r["doi"]]["abstract"]
            r["abstract_filled"] = "openalex"
        if not r.get("oa_url") and r["doi"] in fill:
            r["oa_url"] = fill[r["doi"]]["oa_url"]
    out = []
    counts = {"no_abstract": 0, "auto_excluded_no_tech": 0, "auto_excluded_no_econ_outcome": 0,
              "auto_excluded_no_multi_or_het": 0, "candidate": 0}
    for r in merged:
        text = f"{r['title']}. {r.get('abstract') or ''}"
        has_abs = bool(r.get("abstract"))
        if not TECH.search(r["title"] + " " + (r.get("abstract") or "")):
            stage1 = "auto_excluded_no_tech"
        elif not has_abs:
            stage1 = "no_abstract"
        elif not OUTC.search(text):
            stage1 = "auto_excluded_no_econ_outcome"
        elif not (MULTI.search(text) or HET.search(text)):
            stage1 = "auto_excluded_no_multi_or_het"
        else:
            stage1 = "candidate"
        counts[stage1] += 1
        r["stage1"] = stage1
        out.append(r)

    cols = ["id", "doi", "source", "also_in", "stage1", "year", "type", "venue", "title", "abstract",
            "cited", "oa_url", "landing"]
    with open(os.path.join(DATA, "records_dedup.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    summary = {"records_identified_per_source_rows": identified,
               "distinct_per_source": distinct_by_src,
               "distinct_total_before_cross_source_dedup": len(distinct),
               "duplicates_removed_across_sources": len(distinct) - len(merged),
               "records_after_deduplication": len(merged), "stage1": counts}
    with open(os.path.join(DATA, "prisma_counts_stage1.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

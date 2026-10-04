"""Merge per-batch extraction outputs, check quotes against the source text and rebuild the summary.

Inputs : extraction outputs (out_*.json), converted full texts, review/data/adjustments.json
Outputs: review/data/extraction.json, review/extraction_summary.md, and the full-text section of review/prisma_flow.md
Usage  : python3 review/scripts/merge_extractions.py <scratchpad_dir>
"""
import collections, csv, glob, json, os, re, sys

csv.field_size_limit(sys.maxsize)
SP = sys.argv[1]
ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
rows = {r["idx"]: r for r in csv.DictReader(open(os.path.join(ROOT, "review/data/abstract_stage_decisions.csv"), encoding="utf-8"))}
adj = json.load(open(os.path.join(ROOT, "review/data/adjustments.json")))

def clean(t):
    t = t.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("­", "")
    return re.sub(r"-\s*\n\s*", "", t)

def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", clean(t).lower()).strip()

PAT = [re.compile(r"'([^']{15,300})'"), re.compile(r'"([^"]{15,300})"'), re.compile("“([^”]{15,300})”")]

def evidence_strings(r):
    out = []
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "evidence" and isinstance(v, str):
                    out.append(v)
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(r)
    return out

recs = []
for p in sorted(glob.glob(f"{SP}/extract/out_*.json")):
    recs += json.load(open(p))
seen = {}
for r in recs:
    seen[r["idx"]] = r
recs = sorted(seen.values(), key=lambda r: int(r["idx"]))
for r in recs:
    r.pop("_batch", None)
    a = adj.get(r["idx"])
    if a:
        r["fulltext_decision"], r["exclusion_reason"], r["decision_rationale"] = a["decision"], a["reason"], a["note"]
    txt = norm(open(f"{SP}/txt/{r['idx']}.txt", encoding="utf-8", errors="ignore").read())
    n = g = 0
    for s in evidence_strings(r):
        for pat in PAT:
            for q in pat.findall(s):
                parts = [x for x in re.split(r"\.\.\.|…|\[[^\]]*\]", q) if len(norm(x)) >= 12]
                if not parts:
                    continue
                n += 1
                g += all(norm(x) in txt for x in parts)
    r["quote_check"] = {"verified": g, "checked": n}
    r["quote_flag"] = "ok" if n == 0 or g / n >= 0.8 else "needs human check"
json.dump(recs, open(os.path.join(ROOT, "review/data/extraction.json"), "w"), indent=1, ensure_ascii=False)

inc = [r for r in recs if r["fulltext_decision"] == "include"]
exc = [r for r in recs if r["fulltext_decision"] == "exclude"]
ctx = [r for r in recs if r["fulltext_decision"] == "context"]
na = [r for r in recs if r["fulltext_decision"] == "not_assessed"]
tq = sum(r["quote_check"]["checked"] for r in recs)
gq = sum(r["quote_check"]["verified"] for r in recs)
reasons = collections.Counter(r["exclusion_reason"] for r in exc)
fl = [r for r in inc if r["quote_flag"] != "ok"]
borderline = ["1495", "913", "878", "1026"]
names = {1: "Output and productivity", 2: "Structural change", 3: "Labour market", 4: "Poverty and distribution", 5: "Living standards beyond income", 6: "Resource cost"}
fam = collections.defaultdict(collections.Counter)
for r in inc:
    for x in r.get("results") or []:
        fam[x.get("family")][x.get("direction")] += 1
dom = collections.defaultdict(collections.Counter)
for r in inc:
    for d, v in (r.get("risk_of_bias") or {}).items():
        dom[d][v.get("rating") if isinstance(v, dict) else str(v)] += 1
oc = collections.Counter(r.get("overall_risk_of_bias") for r in inc)
mod = collections.Counter(h.get("moderator") for r in inc for h in (r.get("heterogeneity") or []))
def has_ig(r):
    return any(v and "not reported" not in str(v).lower() and "not applicable" not in str(v).lower() for v in (r.get("income_group_results") or {}).values())
igc = sum(1 for r in inc if has_ig(r))
def tech(r):
    return "; ".join(t.split("(")[0].strip() for t in (r.get("technology") or [])[:2])[:50]

L = ["# Preliminary extraction summary (machine-extracted, re-checked by a second model run and, on a random sample, by the author by hand; see data/human_check.md)", "",
 f"**Read this first.** These records were extracted from the {len(recs)} full texts obtained so far, using the frozen extraction form. Every extracted result carries a page or table locator and a short quote. An automated check found that **{100*gq//max(tq,1)}% of the quotes appear verbatim in the source text** (PDF layout, tables and paraphrase explain part of the gap); papers where fewer than 80% of quotes could be matched are flagged *needs human check*. Nothing here is pooled and nothing is a conclusion yet. Only {len(recs)-len(na)} of 256 papers sent to full-text assessment have been read.", "",
 f"## Full-text assessment outcome (n = {len(recs)-len(na)} read)", "",
 f"- Included: {len(inc)}  |  excluded: {len(exc)}  |  context only: {len(ctx)}  |  wrong document retrieved: {len(na)} (to be re-retrieved)",
 "- Reasons for exclusion: " + ", ".join(f"{k} {v}" for k, v in sorted(reasons.items())) + " (E1 single or fewer than 10 economies, E2 exposure not eligible, E4 conceptual, review, theory or no own estimates)",
 "- Post-merge adjustments are listed with reasons in `data/adjustments.json`.",
 "- About a third of the papers that looked eligible on the abstract failed at full text. The same attrition should be expected for the papers not yet read.", "",
 "## Included studies", "", "| # | Year | Stream | Technology | Economies | Years | Overall risk of bias | Quotes |", "|---|---|---|---|---|---|---|---|"]
for r in inc:
    s = r.get("sample") or {}
    L.append(f"| {r['idx']} | {rows[r['idx']]['year']} | {r.get('stream')} | {tech(r)} | {str(s.get('n_economies'))[:18]} | {str(s.get('years'))[:16]} | {r.get('overall_risk_of_bias')} | {r['quote_flag']} |")
L += ["", "## Direction of reported results by outcome family", "", "Counts of reported results (a paper can contribute several), not of papers, and not weighted by size or quality. The mix of positive, null, mixed and negative results in the first row is the main thing to notice.", "", "| Family | Positive | Mixed | Null | Negative |", "|---|---|---|---|---|"]
for f in range(1, 7):
    c = fam[f]
    L.append(f"| {f}. {names[f]} | {c['positive']} | {c['mixed']} | {c['null']} | {c['negative']} |")
L += ["", "## Risk of bias (adapted ROBINS-I-style tool, 6 domains)", "", "| Domain | Low | Moderate | Serious | Critical |", "|---|---|---|---|---|"]
for d, c in dom.items():
    L.append(f"| {d.replace('_', ' ')} | {c['low']} | {c['moderate']} | {c['serious']} | {c['critical']} |")
L += ["", f"Overall: low {oc['low']}, moderate {oc['moderate']}, serious {oc['serious']}, critical {oc['critical']}. The weakest domain is confounding and reverse causation: most studies treat adoption as exogenous.", "",
 f"Venue check: {sum(1 for r in inc if str(r.get('venue_quality_concern','')).startswith('possible'))} of {len(inc)} included papers were flagged for a possible venue-quality concern (for example unfamiliar journals or working-paper series). This is a screening flag, not a finding, and needs a proper check against journal lists.", "",
 "## Heterogeneity reported", "",
 "Moderators examined (counts of findings): " + ", ".join(f"{k} {v}" for k, v in mod.most_common()) + ".", "",
 f"{igc} of {len(inc)} included papers report at least one income-group-specific result. Before any synthesis these need to be read against each other by a human, because the estimates are on different scales and the income groupings are defined differently.", "",
 "## Papers flagged for human check", "",
 "Quotes could not be fully matched for: " + ", ".join(r["idx"] for r in fl) + ". Borderline eligibility: " + ", ".join(borderline) + " (number of economies or exposure or outcome family does not clearly meet the criteria; a human decision is needed)."]
open(os.path.join(ROOT, "review/extraction_summary.md"), "w").write("\n".join(L) + "\n")

p = open(os.path.join(ROOT, "review/prisma_flow.md")).read().split("\n## Full-text stage (updated)")[0].rstrip("\n")
requested_left = 26 - len([r for r in recs if r["idx"] in {x for x in rows if rows[x].get("tier") == "A"} and False])
p += f"""

## Full-text stage (updated)

| Stage | n | Note |
|---|---|---|
| Full texts read | {len(recs)-len(na)} | {len(recs)} files received; {len(na)} was the wrong document (idx 242) and needs re-retrieval |
| Excluded at full text | {len(exc)} | {', '.join(f'{k} {v}' for k, v in sorted(reasons.items()))} |
| Context only (no payoff outcome estimated) | {len(ctx)} | |
| **Included, preliminary** | **{len(inc)}** | Machine-extracted, quotes partly verified, see `extraction_summary.md`. {len(fl)} are flagged for human check |
"""
open(os.path.join(ROOT, "review/prisma_flow.md"), "w").write(p + "\n")
print(len(recs), "records | include", len(inc), "exclude", len(exc), "context", len(ctx), "not_assessed", len(na), "| quotes", gq, "/", tq, "| flagged", len(fl))

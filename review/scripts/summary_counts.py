"""Counts quoted in the manuscript (characteristics of included studies). Usage: python3 review/scripts/summary_counts.py"""
import collections as C, csv, json, os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
D = os.path.join(ROOT, "review/data")
ext = [x for x in json.load(open(os.path.join(D, "extraction.json"))) if x["fulltext_decision"] == "include"]
def cov(x):
    if x["idx"] == "1372":
        return ""
    t = x["sample"]["income_groups_covered"].lower()
    return re.sub(r"\bno (?:[a-z-]+ or )?(?:low|high)[^;).]*", "", t)
def low(x): return bool(re.search(r"\blow\b(?!\s*-?\s*middle)", cov(x).replace("lower", "x")))
def est(x):
    e = x["design"]["estimator"].lower()
    if "gmm" in e: return "GMM"
    if re.search("ardl|coint|fmols|dols|amg|cce|mean group", e): return "ARDL"
    if re.search("fixed|ols|random|pooled|panel", e): return "FE"
    return "other"
yr = {r["idx"]: int(r["year"]) for r in csv.DictReader(open(os.path.join(D, "abstract_stage_decisions.csv"), encoding="utf-8"))}
for r in csv.DictReader(open(os.path.join(D, "added_records.csv"))):
    yr.setdefault(r["idx"], int(r["year"]))
ys = [yr[x["idx"]] for x in ext]
print("included", len(ext), "| streams", dict(C.Counter(x["stream"] for x in ext)))
print("risk of bias", dict(C.Counter(x["overall_risk_of_bias"] for x in ext)))
print("estimators", dict(C.Counter(est(x) for x in ext)))
print("country-year panels", sum(x["sample"]["unit"].startswith("country-year") for x in ext))
print("no identification", sum(x["design"]["identification"].lower().startswith("none") for x in ext))
print("lists a low-income economy", sum(low(x) for x in ext))
print("families", {k: sum(any(r["family"] == k for r in x["results"]) for x in ext) for k in range(1, 7)})
print("years", min(ys), max(ys), "from 2020:", sum(y >= 2020 for y in ys))
dis = C.Counter(x["second_pass"]["risk_of_bias_overall_opinion"] for x in ext if "second_pass" in x)
print("cross-check opinion on risk of bias", dict(dis))
res = C.Counter()
het = C.Counter()
for x in ext:
    sp = x.get("second_pass") or {}
    res.update(sp.get("results", {})); het.update(sp.get("heterogeneity", {}))
print("results", dict(res), sum(res.values()), "| heterogeneity", dict(het), sum(het.values()))

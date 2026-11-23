"""Merge coded contrasts of the included studies (data/contrasts.json) with the coded new records
(agent outputs new_out*.json) into data/contrasts_all.json and data/new_studies.json.
Usage: python3 merge_contrasts.py new_out1.json [new_out2.json ...]"""
import json, os, subprocess, sys, time
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
old = json.load(open(os.path.join(ROOT, "contrasts.json")))
for c in old: c["source"] = "included (main search)"
studies, new = [], []
ROB = {x["idx"]: x["overall"] for x in json.load(open(os.path.join(ROOT, "rob_new.json")))} if os.path.exists(os.path.join(ROOT, "rob_new.json")) else {}
def label(wid):
    for k in range(5):
        try:
            w = json.loads(subprocess.run(["curl", "-s", "--max-time", "40", f"https://api.openalex.org/works/{wid}?select=authorships,publication_year"], capture_output=True).stdout)
            a = [x["author"]["display_name"].split()[-1] for x in w.get("authorships", [])]
            name = a[0] if len(a) == 1 else (f"{a[0]} and {a[1]}" if len(a) == 2 else f"{a[0]} et al.") if a else wid
            return f"{name} {w.get('publication_year')}"
        except Exception: time.sleep(3)
    return wid
for f in sys.argv[1:]:
    for r in json.load(open(f)):
        lab = label(r["idx"])
        s = {k: r.get(k) for k in ["idx", "title", "eligibility", "code", "stream", "technology", "families", "n_economies", "years", "estimator", "risk_of_bias"]}
        if r["idx"] in ROB: s["risk_of_bias"] = ROB[r["idx"]]
        s["study"] = lab; studies.append(s)
        if r.get("eligibility") != "include": continue
        for c in r.get("contrasts") or []:
            c["idx"] = r["idx"]; c["study"] = lab; c["source"] = "new (citation or income-group search)"; c["risk_of_bias"] = ROB.get(r["idx"], r.get("risk_of_bias")); new.append(c)
json.dump(old + new, open(os.path.join(ROOT, "contrasts_all.json"), "w"), indent=1)
json.dump(studies, open(os.path.join(ROOT, "new_studies.json"), "w"), indent=1)
print("old contrasts", len(old), "new", len(new), "new records", len(studies), "eligible", sum(s["eligibility"] == "include" for s in studies))

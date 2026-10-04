"""Agreement and recall estimates from the independent blind re-screening (data/rescreen_outputs.json) and the adjudication of disagreements (data/rescreen_adjudication.json).

Samples (seed 20261004): S1 = 100 of the 1,545 records removed by automated stage-1 rules; S2 = 120 of the 1,611 removed at title level;
S3 = 120 of the 456 records assessed at abstract level. Writes review/rescreening.md.
"""
import collections as C
import csv
import json
import math
import os
import sys

csv.field_size_limit(sys.maxsize)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
D = os.path.join(ROOT, "review/data")
out = json.load(open(os.path.join(D, "rescreen_outputs.json")))
adj = {a["sid"]: a for a in json.load(open(os.path.join(D, "rescreen_adjudication.json")))}
dec = {r["idx"]: r["decision"] for r in csv.DictReader(open(os.path.join(D, "abstract_stage_decisions.csv"), encoding="utf-8"))}
stage = lambda s: s.split("-")[0]

def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d

def kappa(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = C.Counter(a), C.Counter(b); pe = sum(ca[k] * cb[k] for k in set(a) | set(b)) / n / n
    return po, (po - pe) / (1 - pe)

L = ["# Independent re-screening of a random sample (blind second screener)", "",
     "A separate model run, given only the review criteria and each record's title and abstract (no earlier decision), screened 340 randomly chosen records. This is a second screener of the same model family as the first, so it checks consistency and recall, not truth. Disagreements about exclusions were then adjudicated by a third blind reading of the abstract. Sample size per stage is small, so intervals are wide.", ""]
s3 = [o for o in out if stage(o["sid"]) == "S3"]
orig = ["INC" if dec[o["sid"][3:]] == "INC" else "OTHER" for o in s3]
L += ["## Abstract stage (S3, n = 120 of 456)", "", "| Second screener's UNSURE counted as | Agreement | Cohen's kappa |", "|---|---|---|"]
for lab, f in [("include", lambda d: "INC" if d in ("INC", "UNSURE") else "OTHER"), ("not include", lambda d: "INC" if d == "INC" else "OTHER")]:
    po, k = kappa(orig, [f(o["decision"]) for o in s3])
    L.append(f"| {lab} | {100*po:.0f}% | {k:.2f} |")
c = C.Counter((dec[o["sid"][3:]], o["decision"]) for o in s3)
f6 = [o for o in s3 if dec[o["sid"][3:]] == "F6"]
f6_inc = sum(1 for o in f6 if o["decision"] in ("INC", "UNSURE"))
L += ["", f"Of the {len(f6)} sampled records the first screener had set aside as \"environmental outcome only, low priority\" (protocol amendment 2), the second screener would have sent {f6_inc} to full text. Carbon and electricity outcomes are in the protocol's outcome family 6, so these records meet the eligibility criteria; setting them aside was a prioritisation choice, and it is why only 4 included studies report resource-cost outcomes.", ""]
L += ["## Recall: records excluded by the first screener that a second reader would include", "", "| Stage excluded | Sample | Second screener: include or unsure | After adjudication: meets or probably meets | Share (95% CI) | Implied number among all excluded at this stage |", "|---|---|---|---|---|---|"]
tot = 0; tlo = 0; thi = 0
for st, lab, N in [("S1", "Automated stage-1 rules", 1545), ("S2", "Title level", 1611)]:
    g = [o for o in out if stage(o["sid"]) == st]
    fl = [o for o in g if o["decision"] in ("INC", "UNSURE")]
    ok = sum(1 for o in fl if adj[o["sid"]]["verdict"] in ("meets", "probably"))
    lo, hi = wilson(ok, len(g)); tot += ok / len(g) * N; tlo += lo * N; thi += hi * N
    L.append(f"| {lab} | {len(g)} | {len(fl)} | {ok} | {100*ok/len(g):.1f}% ({100*lo:.1f} to {100*hi:.1f}) | about {round(ok/len(g)*N)} of {N} (range {round(lo*N)} to {round(hi*N)}) |")
ex = [o for o in s3 if dec[o["sid"][3:]] == "EXC"]
ok3 = sum(1 for o in s3 if dec[o["sid"][3:]] == "EXC" and o["decision"] in ("INC", "UNSURE") and adj.get(o["sid"], {}).get("verdict") in ("meets", "probably"))
lo, hi = wilson(ok3, len(s3))
L.append(f"| Abstract level (coded exclusions only) | {len(s3)} | {sum(1 for o in s3 if dec[o['sid'][3:]]=='EXC' and o['decision'] in ('INC','UNSURE'))} | {ok3} | {100*ok3/len(s3):.1f}% ({100*lo:.1f} to {100*hi:.1f}) | about {round(ok3/len(s3)*456)} of 456 (range {round(lo*456)} to {round(hi*456)}) |")
tot += ok3 / len(s3) * 456; tlo += lo * 456; thi += hi * 456
cannot = sum(1 for a in adj.values() if a["verdict"] == "cannot_tell")
L += ["", f"Taken together, the screening may have excluded on the order of {round(tot)} records (range about {round(tlo)} to {round(thi)}) that a careful reader would have sent to full text, in addition to the 22 records set aside on purpose as environmental-outcome-only. {cannot} of the 30 adjudicated records could not be judged because no abstract was available. The estimate rests on small samples and on model readers; it is a warning about recall, not a count.", "",
      "Adjudicated records judged to meet or probably meet the criteria are listed in `data/rescreen_adjudication.json`. Typical cases: artificial-intelligence or digital-economy panels with carbon or energy outcomes, small panels of fewer than 10 economies judged eligible under the AI rule, and financial-inclusion studies in Africa and the Arab world.", ""]
open(os.path.join(ROOT, "review/rescreening.md"), "w").write("\n".join(L) + "\n")
print("\n".join(L))

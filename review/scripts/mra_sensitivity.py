"""Sensitivity analyses planned in the protocol: leave-one-study-out and exclusion of studies at critical risk of bias.

Writes review/mra_sensitivity.md. Uses the pooled headline estimates from mra_pilot.py.
"""
import json
import os
import runpy

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
ns = runpy.run_path(os.path.join(HERE, "mra_pilot.py"))
head, dl = ns["head"], ns["dl"]
ext = {x["idx"]: x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json")))}
y, v = head["pcc"].values, head["se"].values ** 2
ids = head["idx"].tolist()
mu, se, tau2, i2, k, pi = dl(y, v)
L = ["# Sensitivity of the pooled headline estimate", "", f"All {k} papers: pooled PCC {mu:.3f} (95% CI {mu-1.96*se:.3f} to {mu+1.96*se:.3f}), I2 {100*i2:.0f}%.", "",
     "## Leave one study out", "", "| Study left out | Pooled PCC | 95% CI | I2 |", "|---|---|---|---|"]
res = []
for j, i in enumerate(ids):
    m = np.ones(len(ids), bool); m[j] = False
    a, b, t, i2_, kk, _ = dl(y[m], v[m])
    res.append((i, a, b, i2_))
    L.append(f"| {i} | {a:.3f} | {a-1.96*b:.3f} to {a+1.96*b:.3f} | {100*i2_:.0f}% |")
lo, hi = min(r[1] for r in res), max(r[1] for r in res)
L += ["", f"Range of the pooled value across leave-one-out runs: {lo:.3f} to {hi:.3f}.", ""]
for lab, keep in [("Excluding studies rated critical", lambda i: ext[i]["overall_risk_of_bias"] != "critical"), ("Excluding studies rated serious or critical (moderate only)", lambda i: ext[i]["overall_risk_of_bias"] == "moderate"),
                  ("Excluding studies that share authors, panel and index (302 or 323; keep 302)", lambda i: i != "323"), ("Excluding studies with no identification strategy", lambda i: not ext[i]["design"]["identification"].lower().startswith("none"))]:
    m = np.array([keep(i) for i in ids])
    if m.sum() >= 3:
        a, b, t, i2_, kk, _ = dl(y[m], v[m])
        L.append(f"- {lab}: {kk} papers, pooled PCC {a:.3f} (95% CI {a-1.96*b:.3f} to {a+1.96*b:.3f}), I2 {100*i2_:.0f}%.")
    else:
        L.append(f"- {lab}: {int(m.sum())} papers, too few to pool.")
open(os.path.join(ROOT, "review/mra_sensitivity.md"), "w").write("\n".join(L) + "\n")
print("done")

"""Figures for the manuscript, from the project data. Writes manuscript/fig_*.png."""
import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from citekeys import short
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
PAL = {"a": "#1f4e79", "b": "#c0504d", "c": "#7f7f7f", "d": "#4f9a5f", "e": "#d98c1f"}

# ---- PRISMA flow: main search (left) and supplementary searches (right) ----
fig, ax = plt.subplots(figsize=(8.6, 8.2)); ax.set_xlim(0, 12); ax.set_ylim(0, 12.4); ax.axis("off")
def box(x, y, w, h, txt, fc="#eef3f8"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec="#44546a", lw=0.9))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.0)
def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color="#44546a", lw=0.9))
ax.text(2.9, 12.25, "Main search (evidence map)", ha="center", fontsize=8, weight="bold")
ax.text(9.1, 12.25, "Supplementary searches (income contrasts)", ha="center", fontsize=8, weight="bold")
box(0.3, 10.8, 5.2, 1.2, "OpenAlex 1,840; Crossref 1,285; NBER 579\n3,612 after deduplication\nGoogle Scholar: 8 queries, first page")
box(0.3, 9.0, 5.2, 1.3, "Excluded by rules 1,545; at title level 1,611;\nat abstract level 121; held as context 88\nSent to full text 247", fc="#f4f4f4")
box(0.3, 7.2, 5.2, 1.3, "Full texts read 143\n(106 of the 247, 5 after re-screening,\n31 from Google Scholar, 1 review)")
box(0.3, 5.4, 5.2, 1.3, "Excluded at full text 45 (too few economies 15,\nexposure 6, outcome 1, no own estimation 23)\nContext only 1", fc="#f4f4f4")
box(0.3, 3.8, 5.2, 1.1, "Included in the evidence map\n97 (80 ICT, 15 AI, 2 both)", fc="#e6f2e8")
box(6.5, 10.8, 5.2, 1.2, "Citation search from 33 studies: 3,595 new\nOpenAlex income-group query: 2,280 new\n(records already screened removed)")
box(6.5, 9.0, 5.2, 1.3, "Excluded by rules 4,116\nScreened 1,759; includable or possible 563\nWith an income comparison 181", fc="#f4f4f4")
box(6.5, 7.2, 5.2, 1.3, "Full texts read 82\n(64 open access, 18 supplied)\nNot obtained 99", fc="#eef3f8")
box(6.5, 5.4, 5.2, 1.3, "Excluded at full text 15\n(exposure 10, outcome 3, too few economies 2)", fc="#f4f4f4")
box(6.5, 3.8, 5.2, 1.1, "Eligible studies added\n67 (64 ICT, 3 AI)", fc="#e6f2e8")
box(2.6, 1.9, 6.8, 1.2, "Studies with a richer-versus-poorer contrast: 82\n(27 from the evidence map, 55 added); 363 contrasts", fc="#e6f2e8")
box(2.6, 0.2, 6.8, 1.1, "Headline contrasts with an effect size: 44\n(pooled in the meta-analysis)", fc="#e6f2e8")
for x in (2.9, 9.1):
    for y1, y2 in [(10.8, 10.3), (9.0, 8.5), (7.2, 6.7), (5.4, 4.9)]:
        arrow(x, y1, x, y2)
arrow(2.9, 3.8, 4.5, 3.1); arrow(9.1, 3.8, 7.5, 3.1); arrow(6.0, 1.9, 6.0, 1.3)
plt.savefig(os.path.join(HERE, "fig_prisma.png"), dpi=170, bbox_inches="tight"); plt.close()

# ---- forest plot of headline estimates ----
d = pd.read_csv(os.path.join(ROOT, "review/data/mra_effect_sizes.csv"), dtype={"idx": str})
h = d[d["role"] == "headline"].groupby("idx").first().reset_index()
h = h.sort_values("pcc")
fig, ax = plt.subplots(figsize=(6.4, 0.32 * len(h) + 1.2))
y = np.arange(len(h))
ax.errorbar(h["pcc"], y, xerr=1.96 * h["se"], fmt="o", ms=4, color=PAL["a"], ecolor="#9db7d3", capsize=2)
ax.axvline(0, color="grey", lw=0.8)
ax.set_yticks(y); ax.set_yticklabels([short(i) for i in h["idx"]], fontsize=7)
ax.set_xlabel("Partial correlation (headline estimate, 95% interval)", fontsize=8)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "fig_forest.png"), dpi=170); plt.close()

# ---- risk of bias by outcome family ----
FAM = {1: "Output and\nproductivity", 2: "Structural\nchange", 3: "Labour\nmarket", 4: "Poverty and\ndistribution", 5: "Living\nstandards", 6: "Resource\ncost"}
rows = []
for f, lab in FAM.items():
    ps = [x for x in ext if any(r["family"] == f for r in x["results"])]
    for lev in ("moderate", "serious", "critical"):
        rows.append((lab, lev, sum(1 for x in ps if x["overall_risk_of_bias"] == lev)))
R = pd.DataFrame(rows, columns=["fam", "lev", "n"]).pivot(index="fam", columns="lev", values="n").reindex([v for v in FAM.values()])
fig, ax = plt.subplots(figsize=(6.4, 3.3))
bot = np.zeros(len(R))
for lev, col in [("moderate", PAL["d"]), ("serious", PAL["e"]), ("critical", PAL["b"])]:
    ax.bar(range(len(R)), R[lev], bottom=bot, label=lev, color=col, width=0.65); bot += R[lev].values
ax.set_xticks(range(len(R))); ax.set_xticklabels(R.index, fontsize=7); ax.set_ylabel("Studies", fontsize=8); ax.legend(fontsize=7, title="Overall risk of bias", title_fontsize=7)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "fig_rob.png"), dpi=170); plt.close()

# ---- publication year by stream ----
import csv, sys
csv.field_size_limit(sys.maxsize)
yr = {r["idx"]: int(r["year"]) for r in csv.DictReader(open(os.path.join(ROOT, "review/data/abstract_stage_decisions.csv"), encoding="utf-8"))}
for _r in csv.DictReader(open(os.path.join(ROOT, "review/data/added_records.csv"), encoding="utf-8")):
    yr.setdefault(_r["idx"], int(_r["year"]))
bins = list(range(2003, 2028, 4))
fig, ax = plt.subplots(figsize=(6.0, 3.0))
H = [yr[x["idx"]] for x in ext if x["stream"] == "H"]; A = [yr[x["idx"]] for x in ext if x["stream"] != "H"]
ax.hist([H, A], bins=bins, stacked=True, color=[PAL["a"], PAL["b"]], label=["Historical waves", "AI (AI or both)"], width=3.2)
ax.set_xlabel("Publication year", fontsize=8); ax.set_ylabel("Studies", fontsize=8); ax.legend(fontsize=7)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "fig_years.png"), dpi=170); plt.close()

# ---- evidence gap heat map from extra_questions.md ----
t = open(os.path.join(ROOT, "review/extra_questions.md")).read().split("## RQ9")[1].split("## RQ10")[0]
rows = [l.strip("|").split("|") for l in t.split("\n") if l.startswith("| ") and "---" not in l and "Outcome family" not in l]
lab = [r[0].strip() for r in rows]; mat = np.array([[int(c) for c in r[1:5]] for r in rows])
fig, ax = plt.subplots(figsize=(5.6, 3.2))
ax.imshow(mat, cmap="Blues", vmin=0, vmax=24)
ax.set_xticks(range(4)); ax.set_xticklabels(["Low", "Lower-\nmiddle", "Upper-\nmiddle", "High"], fontsize=7)
ax.set_yticks(range(len(lab))); ax.set_yticklabels(lab, fontsize=7)
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        ax.text(j, i, mat[i, j], ha="center", va="center", fontsize=8, color="white" if mat[i, j] > 14 else "black")
plt.tight_layout(); plt.savefig(os.path.join(HERE, "fig_gap.png"), dpi=170); plt.close()
print("figures done")

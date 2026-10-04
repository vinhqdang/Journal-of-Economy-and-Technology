"""Figures for the manuscript, from the project data. Writes manuscript/fig_*.png."""
import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyBboxPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ext = [x for x in json.load(open(os.path.join(ROOT, "review/data/extraction.json"))) if x["fulltext_decision"] == "include"]
PAL = {"a": "#1f4e79", "b": "#c0504d", "c": "#7f7f7f", "d": "#4f9a5f", "e": "#d98c1f"}

# ---- PRISMA flow ----
fig, ax = plt.subplots(figsize=(7.2, 8.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 12); ax.axis("off")
def box(x, y, w, h, txt, fc="#eef3f8"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec="#44546a", lw=0.9))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.4)
def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color="#44546a", lw=0.9))
box(0.3, 10.6, 4.4, 1.0, "Records identified\nOpenAlex 1,840; Crossref 1,285; NBER 579\n(3,704 before cross-source deduplication)")
box(5.3, 10.4, 4.4, 1.4, "Not searched: arXiv (attempted), Scopus,\nWeb of Science, EconLit. Google Scholar:\none page of one query (10 results),\n9 not in the main search, 6 obtained", fc="#f6e9e9")
box(0.3, 9.0, 4.4, 1.0, "Records after deduplication\n3,612 (92 duplicates removed)")
box(5.3, 9.0, 4.4, 1.0, "Excluded by automated stage-1 rules\n1,545", fc="#f4f4f4")
box(0.3, 7.4, 4.4, 1.0, "Read at title level\n2,067")
box(5.3, 7.4, 4.4, 1.0, "Excluded at title level\n1,611", fc="#f4f4f4")
box(0.3, 5.8, 4.4, 1.0, "Assessed at abstract level\n456")
box(5.3, 5.2, 4.4, 2.0, "Excluded at abstract level 121\nDuplicates 8; context 46\nenvironmental-only 22; reviews 9\nsupplementary micro evidence 3", fc="#f4f4f4")
box(0.3, 4.2, 4.4, 1.0, "Sent to full-text assessment\n247")
box(5.3, 3.0, 4.4, 1.4, "Not read: no free full text\nor venue judged unreliable\n141 of 247 (about)", fc="#f6e9e9")
box(0.3, 2.6, 4.4, 1.0, "Full texts read\n118 (106 of the 247, one review,\nfive added after re-screening,\nsix from Google Scholar)")
box(5.3, 1.1, 4.4, 1.4, "Excluded at full text 40\nE1 too few economies 13; E2 exposure 5\nE3 outcome 1; E4 no own estimation 21\nContext only 1", fc="#f4f4f4")
box(0.3, 1.0, 4.4, 1.0, "Studies included\n77 (62 historical waves, 13 AI, 2 both)", fc="#e6f2e8")
for y1, y2 in [(10.6, 10.0), (9.0, 8.4), (7.4, 6.8), (5.8, 5.2), (4.2, 3.6), (2.6, 2.0)]:
    arrow(2.5, y1, 2.5, y2)
for y in (9.5, 7.9, 6.2, 3.7, 1.8):
    arrow(4.7, y, 5.3, y if y not in (6.2,) else 6.2)
plt.savefig(os.path.join(HERE, "fig_prisma.png"), dpi=170, bbox_inches="tight"); plt.close()

# ---- forest plot of headline estimates ----
d = pd.read_csv(os.path.join(ROOT, "review/data/mra_effect_sizes.csv"), dtype={"idx": str})
h = d[d["role"] == "headline"].groupby("idx").first().reset_index()
h = h.sort_values("pcc")
fig, ax = plt.subplots(figsize=(6.4, 0.32 * len(h) + 1.2))
y = np.arange(len(h))
ax.errorbar(h["pcc"], y, xerr=1.96 * h["se"], fmt="o", ms=4, color=PAL["a"], ecolor="#9db7d3", capsize=2)
ax.axvline(0, color="grey", lw=0.8)
ax.set_yticks(y); ax.set_yticklabels([f"Study {i}" for i in h["idx"]], fontsize=7)
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

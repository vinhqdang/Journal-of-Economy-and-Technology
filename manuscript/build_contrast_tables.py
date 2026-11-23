"""Tables and figure for the within-study income contrasts (reads review/data/contrasts_all.json,
contrast_effects.json, contrast_results.json written by review/scripts/contrast_meta.py)."""
import json, math, os, re
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from citekeys import short
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "review", "data")
C = [c for c in json.load(open(os.path.join(D, "contrasts_all.json"))) if c.get("headline") and c.get("design") != "region"]
E = {e["idx"]: e for e in json.load(open(os.path.join(D, "contrast_effects.json")))}
R = json.load(open(os.path.join(D, "contrast_results.json")))
FAM = {1: "Output and productivity", 2: "Structural change", 3: "Labour market", 4: "Poverty and distribution", 5: "Living standards", 6: "Resource cost"}
def esc(s): return re.sub(r"([&%_#$])", r"\\\1", re.sub(r"[\u4e00-\u9fff]+", "", str(s).replace("\u0394", "change in ")))
def stream(c):
    t = (c.get("technology") or "").lower()
    return "AI" if re.search(r"\bai\b|artificial|robot|automation", t) else "ICT"
cols = ["richer larger", "poorer larger", "opposite signs"]
def row(name, xs):
    k = sum(1 for c in xs if c["idx"] in E)
    other = sum(1 for c in xs if c["direction"] not in cols)
    return f"{name} & {len(xs)} & " + " & ".join(str(sum(c['direction'] == d for c in xs)) for d in cols) + f" & {other} & {k}\\\\"
L = [r"\begin{table}[ht]\centering\small", r"\caption{Direction of the headline within-study contrast, by outcome family. Directions are in benefit terms (for inequality, poverty, emissions and similar outcomes a larger reduction counts as a larger benefit). The last column counts contrasts with enough information to compute an effect size.}\label{tab:cdirs}",
     r"\begin{tabular}{@{}lrrrrrr@{}}\toprule Family & Studies & Richer larger & Poorer larger & Opposite signs & Other & Effect size\\\midrule"]
for f in range(1, 7): L.append(row(FAM[f], [c for c in C if c.get("family") == f]))
L.append(r"\midrule " + row("AI and automation", [c for c in C if stream(c) == "AI"]))
L.append(row(r"\textbf{All}", C))
L += [r"\bottomrule\end{tabular}\end{table}", ""]
open(os.path.join(HERE, "tab_cdirs.tex"), "w").write("\n".join(L))
lab = {"All headline contrasts": "All headline contrasts", "Excluding contrasts flagged as implausible": "Excluding contrasts flagged as implausible",
       "Verified against the full text and not flagged": "Checked against the full text and not flagged", "Output and productivity (family 1)": "Output and productivity",
       "Output family, excluding flagged": "Output and productivity, excluding flagged", "Split-sample only": "Split-sample designs only",
       "World Bank income groups only": "World Bank income groups only", "Difference formally tested": "Difference formally tested in the study",
       "Excluding studies rated critical": "Excluding studies rated critical", "Included studies from the main search": "Studies from the main search",
       "New studies from the supplementary searches": "Studies from the supplementary searches"}
L = [r"\begin{table}[ht]\centering\small", r"\caption{Difference in partial correlations between the richer and the poorer group (richer minus poorer; positive means a larger benefit in richer economies). Random effects, one headline contrast per study, Hartung--Knapp--Sidik--Jonkman intervals.}\label{tab:csens}",
     r"\begin{tabular}{@{}lrrrr@{}}\toprule Sample & $k$ & Difference & 95\% CI & $I^2$\\\midrule"]
for r in R["rows"]:
    name = lab.get(r["label"], r["label"]) if not r["label"].startswith("Missing N") else "Missing observations imputed at the median"
    L.append(f"{name} & {int(r['k'])} & {r['mu']:+.3f} & [{r['lo']:+.3f}, {r['hi']:+.3f}] & {100*r['I2']:.0f}\\%\\\\")
L += [r"\bottomrule\end{tabular}\end{table}", ""]
open(os.path.join(HERE, "tab_csens.tex"), "w").write("\n".join(L).replace("+0.000", "0.000"))
# forest
flag = {c["idx"]: bool(c.get("plausibility_flag")) for c in C}
es = sorted(E.values(), key=lambda e: e["d"])
fig, ax = plt.subplots(figsize=(6.6, 0.15 * len(es) + 1.3))
for y, e in enumerate(es):
    lo, hi = e["d"] - 1.96 * e["se"], e["d"] + 1.96 * e["se"]
    ax.plot([max(lo, -1), min(hi, 1)], [y, y], color="#44546a", lw=0.8)
    ax.plot(e["d"], y, "o", ms=3.5, mfc="white" if flag.get(e["idx"]) else "#1f4e79", mec="#1f4e79")
ax.set_yticks(range(len(es))); ax.set_yticklabels([short(e["idx"]) + f" [{e['family']}]" for e in es], fontsize=6)
ax.axvline(0, color="grey", lw=0.6, ls=":")
rr = {r["label"]: r for r in R["rows"]}
for j, (k, txt) in enumerate([("Excluding contrasts flagged as implausible", "Pooled, excluding flagged"), ("Output and productivity (family 1)", "Pooled, output family")]):
    r = rr[k]; y = len(es) + 1 + j
    ax.fill([r["lo"], r["mu"], r["hi"], r["mu"]], [y, y + 0.35, y, y - 0.35], color="#c55a11")
    ax.text(0.98, y, txt, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=7)
ax.set_ylim(-1, len(es) + 3); ax.set_xlim(-1, 1)
ax.set_xlabel("Difference in partial correlation, richer minus poorer (95% CI)", fontsize=8); ax.tick_params(axis="x", labelsize=7)
plt.tight_layout(); plt.savefig(os.path.join(HERE, "fig_cforest.png"), dpi=200); plt.close()
# appendix table
L = [r"{\scriptsize\setlength{\tabcolsep}{3pt}\begin{longtable}{@{}p{3.0cm} p{0.4cm} p{3.3cm} p{3.7cm} p{1.8cm} p{2.9cm}@{}}",
     r"\caption{Headline within-study income contrasts. Fam.: outcome family (1 output and productivity, 2 structural change, 3 labour market, 4 poverty and distribution, 5 living standards, 6 resource cost). $d$: difference in partial correlations, richer minus poorer, in benefit terms; $\dagger$ flagged as implausible.}\label{tab:capp}\\",
     r"\toprule Study & Fam. & Technology & Groups (richer vs poorer) & Direction & $d$ [95\% CI]\\\midrule\endfirsthead", r"\toprule Study & Fam. & Technology & Groups (richer vs poorer) & Direction & $d$ [95\% CI]\\\midrule\endhead", r"\bottomrule\endfoot"]
for c in sorted(C, key=lambda c: short(c["idx"]).lower()):
    e = E.get(c["idx"])
    d = (f"{e['d']:+.3f} [{e['d']-1.96*e['se']:+.2f}, {e['d']+1.96*e['se']:+.2f}]" + (r"$\dagger$" if flag.get(c["idx"]) else "")) if e else "--"
    def tidy(t, n):
        t = re.sub(r"\s*\([^)]*\)?", "", str(t or "")).strip(" ,;")
        if len(t) > n: t = t[:n].rsplit(" ", 1)[0].rstrip(" ,;-") + "..."
        return t
    tech = esc(tidy(c.get("technology"), 38)); grp = esc(tidy(c.get("richer_group"), 26) + " vs " + tidy(c.get("poorer_group"), 26))
    L.append(f"{esc(short(c['idx']))} & {c.get('family') or ''} & {tech} & {grp} & {esc(c['direction'])} & {d}\\\\")
L.append(r"\end{longtable}}")
open(os.path.join(HERE, "app_contrasts.tex"), "w").write("\n".join(L) + "\n")
print("contrast tables done", len(C), len(E))

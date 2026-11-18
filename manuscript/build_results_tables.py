"""Main-text summary tables (tab_families.tex, tab_design.tex, tab_conditions.tex)."""
import collections as C, csv, json, os, re, statistics as S
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "review", "data")
ext = [x for x in json.load(open(os.path.join(D, "extraction.json"))) if x["fulltext_decision"] == "include"]
def cov(x):
    if x["idx"] == "1372": return ""
    t = x["sample"]["income_groups_covered"].lower()
    return re.sub(r"\bno (?:[a-z-]+ or )?(?:low|high)[^;).]*", "", t)
def low(x): return bool(re.search(r"\blow\b(?!\s*-?\s*middle)", cov(x).replace("lower", "x")))
def high(x): return bool(re.search(r"\bhigh\b", cov(x)))
def est(x):
    e = x["design"]["estimator"].lower()
    if "gmm" in e: return "GMM"
    if re.search("ardl|coint|fmols|dols|amg|cce|mean group", e): return "ARDL"
    if re.search("fixed|ols|random|pooled|panel", e): return "FE"
    return "other"
def ne(x):
    m = re.search(r"\d+", str(x["sample"]["n_economies"]).replace(",", "")); return int(m.group()) if m else None
def noid(x): return x["design"]["identification"].lower().startswith("none")
yr = {r["idx"]: int(r["year"]) for r in csv.DictReader(open(os.path.join(D, "abstract_stage_decisions.csv"), encoding="utf-8"))}
for r in csv.DictReader(open(os.path.join(D, "added_records.csv"))): yr.setdefault(r["idx"], int(r["year"]))
def pct(a, b): return f"{a} ({round(100*a/b)}\\%)" if b else "0"
names = {1: "Output and productivity", 2: "Structural change", 3: "Labour market", 4: "Poverty and distribution", 5: "Living standards beyond income", 6: "Resource cost"}
L = [r"\begin{table}[ht]\centering\small", r"\caption{Included studies by outcome family. Direction columns count studies with at least one result of that direction in the family, so a study can appear in several columns. Med. econ.: median number of economies; Low-inc.: studies listing a low-income economy.}\label{tab:families}",
     r"\begin{adjustbox}{max width=\linewidth}\begin{tabular}{@{}lrrrrrrrr@{}}\toprule Family & Studies & AI & Med. econ. & Pos. & Mixed & Null & Neg. & Low-inc.\\\midrule"]
for k in range(1, 7):
    xs = [x for x in ext if any(r["family"] == k for r in x["results"])]
    dirs = {d: sum(any(r["family"] == k and r["direction"] == d for r in x["results"]) for x in xs) for d in ("positive", "mixed", "null", "negative")}
    med = S.median([ne(x) for x in xs if ne(x)])
    L.append(f"{names[k]} & {len(xs)} & {sum(x['stream'] != 'H' for x in xs)} & {med:.0f} & {dirs['positive']} & {dirs['mixed']} & {dirs['null']} & {dirs['negative']} & {sum(low(x) for x in xs)}\\\\")
L += [r"\bottomrule\end{tabular}\end{adjustbox}\end{table}", ""]
open(os.path.join(HERE, "tab_families.tex"), "w").write("\n".join(L))

grp = {"Historical waves": [x for x in ext if x["stream"] == "H"], "AI": [x for x in ext if x["stream"] != "H"], "All": ext}
rows = [("Studies", lambda g: str(len(g))),
 ("Median publication year", lambda g: f"{S.median([yr[x['idx']] for x in g]):.0f}"),
 ("Median number of economies", lambda g: f"{S.median([ne(x) for x in g if ne(x)]):.0f}"),
 ("System or difference GMM", lambda g: pct(sum(est(x) == "GMM" for x in g), len(g))),
 ("Fixed effects, random effects or OLS", lambda g: pct(sum(est(x) == "FE" for x in g), len(g))),
 ("ARDL, cointegration, heterogeneous panels", lambda g: pct(sum(est(x) == "ARDL" for x in g), len(g))),
 ("No identification strategy beyond controls", lambda g: pct(sum(noid(x) for x in g), len(g))),
 ("Lists a low-income economy", lambda g: pct(sum(low(x) for x in g), len(g))),
 ("Lists a high-income economy", lambda g: pct(sum(high(x) for x in g), len(g))),
 ("Risk of bias moderate", lambda g: pct(sum(x["overall_risk_of_bias"] == "moderate" for x in g), len(g))),
 ("Risk of bias serious", lambda g: pct(sum(x["overall_risk_of_bias"] == "serious" for x in g), len(g))),
 ("Risk of bias critical", lambda g: pct(sum(x["overall_risk_of_bias"] == "critical" for x in g), len(g)))]
L = [r"\begin{table}[ht]\centering\small", r"\caption{Design and coverage of the included studies by technology stream (studies on both streams count under AI).}\label{tab:design}",
     r"\begin{tabular}{@{}lrrr@{}}\toprule & Historical waves & AI & All\\\midrule"]
for n, f in rows: L.append(f"{n} & " + " & ".join(f(g) for g in grp.values()) + r"\\")
L += [r"\bottomrule\end{tabular}\end{table}", ""]
open(os.path.join(HERE, "tab_design.tex"), "w").write("\n".join(L))

cond = [("Human capital", 16, 10, 3, 4), ("Income group", 31, 10, 8, 9), ("Infrastructure or connectivity", 11, 5, 2, 2), ("Institutions or governance", 10, 3, 2, 6), ("Trade openness", 9, 4, 3, 2)]
L = [r"\begin{table}[ht]\centering\small", r"\caption{Conditions tested as moderators (studies; direction of the moderated association). For income group, ``raises'' means larger in richer economies. Entries where the direction was unclear are omitted.}\label{tab:conditions}",
     r"\begin{tabular}{@{}lrrrr@{}}\toprule Condition & Studies & Raises & Lowers & Mixed\\\midrule"]
for c in cond: L.append(" & ".join(map(str, c)) + r"\\")
L += [r"\bottomrule\end{tabular}\end{table}", ""]
open(os.path.join(HERE, "tab_conditions.tex"), "w").write("\n".join(L))
print(open(os.path.join(HERE, "tab_families.tex")).read()); print(open(os.path.join(HERE, "tab_design.tex")).read())

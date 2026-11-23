"""Meta-analysis of within-study income contrasts.
Input: review/data/contrasts.json (coded per agent_instructions/contrast_extract.md).
Effect: difference in partial correlations, richer minus poorer group, oriented so that positive = larger benefit
in the richer group. Split-sample contrasts: PCC_rich - PCC_poor with summed variances; interaction contrasts:
PCC of the interaction term, signed by the coded direction. One headline contrast per study, DerSimonian-Laird
random effects with a Hartung-Knapp-Sidik-Jonkman interval; sign test on all studies with a codable direction.
Usage: python3 contrast_meta.py [k_regressors]"""
import json, math, os, re, sys
import numpy as np
from scipy import stats
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
K = int(sys.argv[1]) if len(sys.argv) > 1 else 10
C = json.load(open(os.path.join(ROOT, "contrasts.json")))
ext = {x["idx"]: x for x in json.load(open(os.path.join(ROOT, "extraction.json")))}
def tval(b, se, t, p):
    if t is not None: return float(t)
    if b is not None and se not in (None, 0): return float(b) / float(se)
    return None
def pcc(t, n):
    if t is None or not n: return None
    df = max(int(n) - K, 3); r = t / math.sqrt(t * t + df)
    return r, (1 - r * r) ** 2 / df
def effect(c):
    sgn = {"richer larger": 1, "poorer larger": -1}.get(c["direction"])
    if c["design"] == "interaction":
        e = pcc(tval(c.get("b_inter"), c.get("se_inter"), c.get("t_inter"), c.get("p_inter")), c.get("n_obs_inter"))
        if not e or sgn is None: return None
        return abs(e[0]) * sgn, e[1]
    if c["design"] != "split-sample" or not c.get("same_units", True): return None
    a = pcc(tval(c.get("b_rich"), c.get("se_rich"), c.get("t_rich"), c.get("p_rich")), c.get("n_obs_rich"))
    b = pcc(tval(c.get("b_poor"), c.get("se_poor"), c.get("t_poor"), c.get("p_poor")), c.get("n_obs_poor"))
    if not a or not b: return None
    lib = c.get("lower_is_better")
    if lib is None: lib = bool(re.search(r"gini|inequal|poverty|emission|co2|carbon intensity|mortality|unemploy|concentration", (c.get("outcome") or "").lower()))
    flip = -1 if lib else 1
    return flip * (a[0] - b[0]), a[1] + b[1]
def re_pool(y, v):
    y, v = np.array(y), np.array(v); w = 1 / v; k = len(y)
    mu_fe = (w * y).sum() / w.sum(); Q = (w * (y - mu_fe) ** 2).sum()
    tau2 = max(0, (Q - (k - 1)) / (w.sum() - (w ** 2).sum() / w.sum())) if k > 1 else 0
    ws = 1 / (v + tau2); mu = (ws * y).sum() / ws.sum()
    se_dl = math.sqrt(1 / ws.sum())
    q = (ws * (y - mu) ** 2).sum() / (k - 1) if k > 1 else 1
    se_hk = math.sqrt(max(q, 1) / ws.sum()) if k > 1 else se_dl
    tc = stats.t.ppf(0.975, k - 1) if k > 1 else 1.96
    I2 = max(0, (Q - (k - 1)) / Q) if Q > 0 else 0
    return dict(k=k, mu=mu, lo=mu - tc * se_hk, hi=mu + tc * se_hk, p=2 * stats.t.sf(abs(mu / se_hk), max(k - 1, 1)), I2=I2, tau2=tau2)
def report(label, rows):
    e = [(c, effect(c)) for c in rows]; e = [(c, x) for c, x in e if x]
    if len(e) < 2: print(f"{label}: k={len(e)} (too few)"); return None
    r = re_pool([x[0] for _, x in e], [x[1] for _, x in e])
    print(f"{label}: k={r['k']} mean diff PCC {r['mu']:+.3f} [{r['lo']:+.3f}, {r['hi']:+.3f}] p={r['p']:.2f} I2={100*r['I2']:.0f}%")
    return r, e
head = [c for c in C if c.get("headline")]
studies = sorted({c["idx"] for c in C})
print(f"studies with a contrast {len(studies)}; contrasts {len(C)}; headline {len(head)}; df = N - {K}")
dirs = [c["direction"] for c in head]
nr, npo = dirs.count("richer larger"), dirs.count("poorer larger")
print("headline directions:", {d: dirs.count(d) for d in sorted(set(dirs))})
print(f"sign test richer vs poorer larger: {nr} vs {npo}, two-sided p = {stats.binomtest(nr, nr + npo).pvalue:.2f}" if nr + npo else "no directional contrasts")
res = report("All headline contrasts", head)
report("Output and productivity (family 1)", [c for c in head if c.get("family") == 1])
report("Split-sample only", [c for c in head if c["design"] == "split-sample"])
report("World Bank income groups only", [c for c in head if c.get("comparison") == "WB income groups"])
report("Difference formally tested", [c for c in head if c.get("diff_test_reported")])
report("Excluding studies rated critical", [c for c in head if ext.get(c["idx"], {}).get("overall_risk_of_bias") != "critical"])
if res:
    out = [{"idx": c["idx"], "study": c.get("study"), "family": c.get("family"), "design": c["design"], "comparison": c.get("comparison"),
            "richer": c.get("richer_group"), "poorer": c.get("poorer_group"), "d": round(x[0], 4), "se": round(math.sqrt(x[1]), 4)} for c, x in res[1]]
    json.dump(out, open(os.path.join(ROOT, "contrast_effects.json"), "w"), indent=1)

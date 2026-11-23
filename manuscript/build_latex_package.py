"""Flatten a LaTeX manuscript into one .tex file (all \\input files inlined) and collect its PNG figures.
Usage: python3 build_latex_package.py source.tex outdir [--keep-figures]
Writes outdir/manuscript.tex and copies each figure used by \\includegraphics."""
import os, re, shutil, sys
src, out = sys.argv[1], sys.argv[2]
base = os.path.dirname(os.path.abspath(src)); os.makedirs(out, exist_ok=True)
def inline(path, depth=0):
    t = open(path, encoding="utf-8").read()
    def rep(m):
        f = m.group(1); f = f if f.endswith(".tex") else f + ".tex"
        p = os.path.join(base, f)
        return inline(p, depth + 1) if os.path.exists(p) else m.group(0)
    return re.sub(r"\\input\{([^}]+)\}", rep, t)
t = inline(src)
t = re.sub(r"(?m)^%.*\n", "", t)
figs = sorted(set(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", t)))
for f in figs:
    f2 = f if os.path.splitext(f)[1] else f + ".png"
    shutil.copy(os.path.join(base, f2), os.path.join(out, os.path.basename(f2)))
    t = t.replace("{" + f + "}", "{" + os.path.basename(f2) + "}")
if "landscape" not in t: t = t.replace(",pdflscape}", "}")
open(os.path.join(out, "manuscript.tex"), "w", encoding="utf-8").write(t)
print("figures:", figs, "| input left:", re.findall(r"\\input\{[^}]+\}", t))

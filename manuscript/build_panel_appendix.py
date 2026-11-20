"""Appendix with panel variables and additional results, converted from analysis/results*.md."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(HERE, "..", "analysis")

def esc(s):
    s = str(s).replace("−", "-")
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s

def section_table(path, heading):
    t = open(path).read()
    i = t.find(heading)
    if i < 0:
        return None
    sec = t[i + len(heading):].split("\n## ")[0]
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in sec.split("\n") if l.startswith("|")]
    return [r for r in rows if not set("".join(r)) <= set("-: ")]

def tab(rows, caption, label):
    n = len(rows[0])
    spec = "@{}l" + "r" * (n - 2) + "p{6.4cm}@{}" if n == 4 else "@{}" + "l" * n + "@{}"
    out = [r"\begin{table}[!ht]\centering\footnotesize", rf"\caption{{{caption}}}\label{{{label}}}", r"\begin{adjustbox}{max width=\linewidth}"+rf"\begin{{tabular}}{{{spec}}}\toprule", " & ".join(esc(c) for c in rows[0]) + r" \\ \midrule"]
    for r in rows[1:]:
        out.append(" & ".join(esc(c) for c in r) + r" \\")
    out += [r"\bottomrule\end{tabular}\end{adjustbox}\end{table}", ""]
    return "\n".join(out)

L = [r"\subsection*{Variables}", r"\begin{table}[!ht]\centering\footnotesize\caption{World Bank WDI indicators used.}\label{tab:wdi}\begin{tabular}{@{}lll@{}}\toprule Role & Variable & WDI code\\\midrule",
     "Technology & Mobile cellular subscriptions per 100 people & IT.CEL.SETS.P2\\\\", "Technology & Individuals using the internet, \\% of population & IT.NET.USER.ZS\\\\", "Technology & Fixed broadband subscriptions per 100 people & IT.NET.BBND.P2\\\\",
     "Outcome & GDP per capita, constant 2015 US\\$ & NY.GDP.PCAP.KD\\\\", "Outcome & Life expectancy at birth & SP.DYN.LE00.IN\\\\", "Outcome & Under-5 mortality rate & SH.DYN.MORT\\\\", "Outcome & Unemployment, \\% of labour force & SL.UEM.TOTL.ZS\\\\",
     "Outcome & Agriculture, value added \\% of GDP & NV.AGR.TOTL.ZS\\\\", "Outcome & Electric power consumption per capita & EG.USE.ELEC.KH.PC\\\\", "Control or moderator & School enrolment, secondary, gross & SE.SEC.ENRR\\\\",
     "Control & Trade, \\% of GDP & NE.TRD.GNFS.ZS\\\\", "Moderator & Domestic credit to private sector, \\% of GDP & FS.AST.PRVT.GD.ZS\\\\", "Moderator & Access to electricity, \\% of population & EG.ELC.ACCS.ZS\\\\", "Other & Population, total & SP.POP.TOTL\\\\",
     r"\bottomrule\end{tabular}\end{table}", "",
     r"Income groups follow the World Bank's current classification of 217 economies (25 low, 47 lower-middle, 59 upper-middle and 86 high income; the analysis sample is smaller because of missing data). Aggregates were removed. CO$_2$ emissions per capita could not be retrieved from the API and are not analysed.", ""]
rows = section_table(os.path.join(A, "results.md"), "## A3 dose-response by baseline mobile level (per 100 people at start of period)")
L.append(tab(rows, "Dose-response (A3): change in annual growth (pp) per +10 mobile subscriptions per 100, by baseline adoption level.", "tab:a3"))
rows = section_table(os.path.join(A, "results.md"), "## A6 differences inside low and lower-middle income economies (mobile)")
L.append(tab(rows, "Differences inside low and lower-middle income economies (A6).", "tab:a6"))

for head, cap, lab in [("## Secondary outcomes (takeoff at 10 per 100; only samples that pass the pre-trend rule)", "Event study, secondary outcomes (takeoff at 10 per 100): effects at five and ten years. Rows marked fails do not pass the pre-trend rule and are not interpreted.", "tab:essec")]:
    rows = section_table(os.path.join(A, "results_event.md"), head)
    if rows:
        L.append(tab(rows, cap, lab))
open(os.path.join(HERE, "app_panel.tex"), "w").write("\n".join(L))
print("panel appendix done")

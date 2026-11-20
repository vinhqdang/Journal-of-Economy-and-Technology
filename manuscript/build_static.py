"""Static appendix pieces: search strategy, criteria, PRISMA checklist, and the panel appendix (converted from analysis/results*.md)."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")

def esc(s):
    s = str(s).replace("−", "-")
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s

def md_tables(path, heading, upto_next=True):
    """Return (intro text, list of table rows) for the first markdown table after the heading."""
    t = open(path).read()
    i = t.find(heading)
    if i < 0:
        return None
    sec = t[i:].split("\n## ")[0 if False else 1] if False else t[i + len(heading):].split("\n## ")[0]
    rows = [l.strip().strip("|").split("|") for l in sec.split("\n") if l.startswith("|")]
    rows = [[c.strip() for c in r] for r in rows if not set("".join(r)) <= set("-: ")]
    return rows

def to_tex(rows, caption, label, widths=None, font=r"\footnotesize"):
    n = len(rows[0])
    colspec = widths or ("@{}l" + "l" * (n - 1) + "@{}")
    L = [r"\begin{table}[H]\centering" + font, rf"\caption{{{caption}}}\label{{{label}}}", rf"\begin{{tabular}}{{{colspec}}}\toprule"]
    L.append(" & ".join(esc(c) for c in rows[0]) + r" \\ \midrule")
    for r in rows[1:]:
        L.append(" & ".join(esc(c) for c in r) + r" \\")
    L += [r"\bottomrule\end{tabular}\end{table}", ""]
    return "\n".join(L)

# ---------------- search ----------------
q = open(os.path.join(ROOT, "review/data/openalex_query.txt")).read().strip()
S = [r"\subsection*{Search blocks (protocol)}", "Four concept blocks were combined with AND and searched in title and abstract. The OpenAlex query below is the exact string that was run (restricted to the economics, econometrics and finance field), and the Crossref and NBER searches used 96 combinations of a technology term and a context term.", "",
     r"{\footnotesize\begin{itemize}[leftmargin=1.2em,itemsep=2pt]",
     r"\item \textbf{Block A (technology):} information and communication technolog*, ICT, internet, broadband, mobile phone*, mobile telephon*, smartphone*, digital technolog*, digital economy, artificial intelligence, machine learning, deep learning, generative AI, large language model*, general purpose technolog*, cryptocurrenc*, bitcoin, crypto-asset*, blockchain.",
     r"\item \textbf{Block B (economy level):} countr*, cross-country, nation*, developing econom*, emerging econom*, low-income, middle-income, high-income, income group*, developed econom*, advanced econom*.",
     r"\item \textbf{Block C (outcomes):} growth, productivity, GDP, poverty, inequality, employment, wage*, labor or labour share, structural transformation, financial inclusion, welfare, living standard*, human development.",
     r"\item \textbf{Block D (heterogeneity):} heterogene*, absorptive capacity, complementar*, threshold*, human capital, digital divide, convergence, divergence, technology diffusion, technology adoption, leapfrog*.",
     r"\end{itemize}}", "",
     r"\subsection*{OpenAlex query as run (2 October 2026)}", r"{\fontsize{6.6}{7.6}\selectfont\begin{verbatim}"]
import textwrap
S += textwrap.wrap(q, 110) + [r"\end{verbatim}}", "",
      r"\subsection*{Crossref and NBER searches}",
      "Technology terms: internet; broadband; mobile phones; information and communication technology; digital technology; artificial intelligence; generative AI; machine learning; cryptocurrency; bitcoin; technology diffusion; general purpose technology. Context terms: cross-country panel economic growth; developing countries income groups; digital divide; poverty and inequality countries; productivity emerging economies; employment and wages across countries; absorptive capacity human capital; financial inclusion. All pairs (12 by 8 = 96) were run from 1995.", "",
      r"\subsection*{Google Scholar queries run (first page of 10 results each; September to November 2026)}",
      r"{\scriptsize\begin{itemize}[leftmargin=1.2em,itemsep=1pt]",
      r"\item G1: (``mobile phones'' OR ``mobile telephony'' OR internet OR broadband OR ICT) ``economic growth'' ``developing countries'' ``income groups'' panel cross-country",
      r"\item G2: ``information and communication technology'' growth ``low-income'' ``middle-income'' ``high-income'' countries panel GMM",
      r"\item G3: ``digital economy'' OR digitalization ``economic growth'' countries ``income level'' heterogeneity OR threshold panel",
      r"\item G4: (internet OR mobile OR ICT) ``labor productivity'' OR ``total factor productivity'' countries ``human capital'' OR institutions interaction OR threshold",
      r"\item G5: (ICT OR internet OR mobile OR digital) ``income inequality'' OR poverty ``developing countries'' panel data",
      r"\item G6: (mobile OR internet OR digital) ``financial inclusion'' countries panel ``developing countries'' OR ``sub-Saharan Africa'' OR ``Asia''",
      r"\item G7: ``artificial intelligence'' ``economic growth'' OR productivity countries panel ``developing countries'' OR ``emerging economies'' OR ``income''",
      r"\item G14 (existing meta-analyses): ``meta-analysis'' (ICT OR telecommunications OR internet OR broadband) ``economic growth'' OR productivity",
      r"\end{itemize}}",
      r"\subsection*{Records by source}",
      r"\begin{tabular}{@{}lr@{}}\toprule Source & Distinct records\\\midrule OpenAlex & 1,840\\ Crossref & 1,285\\ NBER working papers & 579\\ arXiv & 0 (attempted, not completed)\\ Scopus, Web of Science, EconLit & 0 (not run)\\ Google Scholar (queries G1, G2, G4, G7, first page each) & 40 results, 29 not in the main search\\\bottomrule\end{tabular}"]
open(os.path.join(HERE, "app_search.tex"), "w").write("\n".join(S) + "\n")

# ---------------- criteria ----------------
C = [r"\subsection*{Eligibility}", r"\begin{table}[H]\centering\small\begin{tabular}{@{}p{3cm}p{6cm}p{6cm}@{}}\toprule Criterion & Include & Exclude\\\midrule",
     r"Study design & Quantitative empirical studies and meta-analyses with their own estimation strategy & Opinion pieces, purely conceptual papers, case descriptions without estimation, simulation-only studies\\",
     r"Sample, historical waves & At least 10 economies, or an explicit comparison of income groups & Single-country and few-country studies\\",
     r"Sample, AI & At least 3 economies, or an explicit comparison across income levels & Single-country firm or worker studies are listed separately as supplementary evidence\\",
     r"Exposure & ICT in general, mobile, internet or broadband, smartphones and mobile data, crypto-assets, AI & Technology used as a control only\\",
     r"Outcome & At least one of six families: output and productivity; structural change; labour market; poverty and distribution; living standards beyond income; resource cost & Adoption or diffusion as the only outcome (kept as context)\\",
     r"Period and language & 1995 to the search date; English & Earlier; other languages\\",
     r"Status & Peer-reviewed articles and working papers from named series; preprints flagged & Conference abstracts, blog posts, reports without methods\\\bottomrule\end{tabular}\end{table}", "",
     r"Exclusion codes at full text: E1 too few economies and no income-group comparison; E2 exposure not eligible; E3 no outcome in the six families; E4 conceptual, review, or no own estimation; DUP duplicate or earlier version of another paper.", "",
     r"\subsection*{Extraction form (frozen before extraction)}",
     r"For each study: decision and coded reason; stream (historical waves, AI or both); technology and exposure measure; sample (number of economies, groups, income coverage, years, unit); design (estimator, identification strategy, controls); results by outcome family (indicator, direction, estimate, uncertainty, horizon, locator and quote); heterogeneity findings (moderator, finding, threshold, locator); results by income group; number of specifications; whether the headline estimate is the preferred specification; risk-of-bias ratings with reasons; venue concern; free-text notes. Every extracted result carries a page or table locator and a verbatim quote of at most 25 words.", "",
     r"\subsection*{Risk-of-bias domains and rating guide}",
     r"\begin{enumerate}[leftmargin=1.6em,itemsep=1pt]\small",
     r"\item Confounding and reverse causation: is adoption treated as exogenous, and is there a credible instrument or timing design?",
     r"\item Exposure measurement: does the adoption measure capture use, or only access or investment?",
     r"\item Selection of countries and years: missing-data patterns and survivorship.",
     r"\item Outcome measurement: quality of the national statistics used.",
     r"\item Specification and researcher degrees of freedom: number of specifications and sensitivity.",
     r"\item Selective reporting.",
     r"\end{enumerate}",
     r"Rating guide: \emph{low} = credible design for the claim; \emph{moderate} = standard panel design with reasonable controls but exogeneity not established; \emph{serious} = causal language with no strategy for reverse causation, or a measure that does not capture the exposure; \emph{critical} = the conclusions cannot be trusted from this design."]
open(os.path.join(HERE, "app_criteria.tex"), "w").write("\n".join(C) + "\n")

# ---------------- PRISMA checklist ----------------
items = [("1", "Title", "Identifies the report type", "Partly", "Title (evidence map)"),
 ("2", "Abstract", "Structured abstract", "Partly", "Abstract"),
 ("3--4", "Rationale, objectives", "Context and explicit questions", "Yes", "Introduction; Section 2"),
 ("5", "Eligibility criteria", "Inclusion and exclusion", "Yes", "Section 3.2; Appendix C"),
 ("6--7", "Sources, search strategy", "Databases, dates, full strategy", "Partly", "Section 3.3; Appendix B; partial"),
 ("8", "Selection process", "Screening method, reviewers", "Partly", "Section 3.4; one reviewer"),
 ("9--10", "Data collection, items", "Extraction method and items", "Partly", "Section 3.5; Appendix C"),
 ("11, 18", "Risk of bias", "Tool, reviewers, results", "Partly", "Sections 3.6, 4.3; Appendix A"),
 ("12--14", "Effect measures, synthesis", "Measures and methods", "Partly", "Section 3.7; Appendices D, E"),
 ("15, 22", "Certainty of evidence", "GRADE or similar", "No", "Not done; see Limitations"),
 ("16--21", "Results", "Flow, studies, bias, synthesis", "Yes", "Section 4; Appendices A, D, E, F"),
 ("23--27", "Discussion, declarations", "Limits, protocol, funding, data", "Partly", "Sections 6--7; Declarations")]
P = [r"{\scriptsize\begin{longtable}{@{}l p{3.6cm} p{4.2cm} l p{4.6cm}@{}}", r"\caption{PRISMA 2020 checklist: where each item is reported. Section numbers refer to this paper.}\label{tab:prismacheck}\\",
     r"\toprule Item & Topic & Requirement & Reported & Where \\ \midrule \endfirsthead", r"\toprule Item & Topic & Requirement & Reported & Where \\ \midrule \endhead", r"\bottomrule \endfoot"]
for it in items:
    P.append(" & ".join(esc(c).replace("--", "--") for c in it) + r" \\")
P += [r"\end{longtable}}"]
open(os.path.join(HERE, "app_prisma.tex"), "w").write("\n".join(P) + "\n")
print("static done")

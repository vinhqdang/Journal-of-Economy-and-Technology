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
     r"\subsection*{OpenAlex query as run (2 October 2026)}", r"{\scriptsize\begin{verbatim}"]
import textwrap
S += textwrap.wrap(q, 110) + [r"\end{verbatim}}", "",
      r"\subsection*{Crossref and NBER searches}",
      "Technology terms: internet; broadband; mobile phones; information and communication technology; digital technology; artificial intelligence; generative AI; machine learning; cryptocurrency; bitcoin; technology diffusion; general purpose technology. Context terms: cross-country panel economic growth; developing countries income groups; digital divide; poverty and inequality countries; productivity emerging economies; employment and wages across countries; absorptive capacity human capital; financial inclusion. All pairs (12 by 8 = 96) were run from 1995.", "",
      r"\subsection*{Records by source}",
      r"\begin{tabular}{@{}lr@{}}\toprule Source & Distinct records\\\midrule OpenAlex & 1,840\\ Crossref & 1,285\\ NBER working papers & 579\\ arXiv & 0 (attempted, not completed)\\ Scopus, Web of Science, EconLit & 0 (not run)\\ Google Scholar (query G1, first page) & 10 results, 9 not in the main search\\\bottomrule\end{tabular}"]
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
items = [("1", "Title", "Identifies the report as a systematic review", "Yes", "Title"),
 ("2", "Abstract", "Structured abstract", "Partly", "Abstract (not the full PRISMA abstract checklist)"),
 ("3", "Rationale", "Rationale in context of existing knowledge", "Yes", "Introduction; Conceptual background"),
 ("4", "Objectives", "Explicit objectives and questions", "Yes", "Introduction; Conceptual background"),
 ("5", "Eligibility criteria", "Inclusion and exclusion criteria", "Yes", "Methods (eligibility); Appendix D"),
 ("6", "Information sources", "Databases, dates, last search", "Partly", "Methods (sources); Scopus, Web of Science and EconLit not searched; Google Scholar only the first page of one query"),
 ("7", "Search strategy", "Full strategy for all sources", "Yes", "Appendix C"),
 ("8", "Selection process", "How records were screened, number of reviewers", "Partly", "Methods (screening); one assisted reviewer plus a blind model re-screen of a random sample (Results, cross-checks)"),
 ("9", "Data collection process", "Methods of extraction, number of reviewers", "Partly", "Methods (extraction, second pass); machine extraction, machine second pass, blind re-extraction of 16 studies, author hand check of a random sample"),
 ("10", "Data items", "Outcomes and other variables", "Yes", "Methods (eligibility); Appendix D"),
 ("11", "Risk of bias", "Tools and reviewers", "Partly", "Methods (risk of bias); adapted tool, single rater"),
 ("12", "Effect measures", "Measures used for each outcome", "Yes", "Methods (meta-regression)"),
 ("13a--f", "Synthesis methods", "Eligibility for synthesis, methods, heterogeneity, sensitivity", "Partly", "Methods (synthesis, meta-regression); leave-one-out and quality-restricted analyses in Results (meta-regression)"),
 ("14", "Reporting bias assessment", "Methods to assess reporting bias", "Yes", "Methods and Results (meta-regression: FAT-PET, PEESE)"),
 ("15", "Certainty assessment", "Methods to assess certainty (e.g. GRADE)", "No", "Not done; listed as a limitation"),
 ("16", "Study selection results", "Flow diagram, excluded studies", "Yes", "Results (study selection), Figure 1; reasons coded"),
 ("17", "Study characteristics", "Cite and present characteristics", "Yes", "Results (characteristics), Appendix A"),
 ("18", "Risk of bias in studies", "Assessments for each study", "Yes", "Results (risk of bias), Appendix A"),
 ("19", "Results of individual studies", "Summary and effect estimates", "Partly", "Appendices B and E; no forest plot for all outcomes"),
 ("20", "Results of syntheses", "Results, heterogeneity, sensitivity", "Yes", "Results (all synthesis subsections)"),
 ("21", "Reporting biases", "Assessments of reporting bias", "Yes", "Results (meta-regression)"),
 ("22", "Certainty of evidence", "Certainty for each outcome", "No", "Not done"),
 ("23", "Discussion", "Interpretation, limitations, implications", "Yes", "Discussion; Limitations"),
 ("24", "Registration and protocol", "Registration number, protocol access", "Partly", "Protocol in repository; not registered"),
 ("25", "Support", "Funding and sponsors", "Yes", "Declarations (author to confirm)"),
 ("26", "Competing interests", "Declared", "No", "Author to complete"),
 ("27", "Availability of data and code", "Public availability", "Yes", "Declarations; repository")]
P = [r"{\footnotesize\begin{longtable}{@{}l p{2.9cm} p{4.3cm} l p{4.8cm}@{}}", r"\caption{PRISMA 2020 checklist: where each item is reported. Section numbers refer to this paper.}\label{tab:prismacheck}\\",
     r"\toprule Item & Topic & Requirement & Reported & Where \\ \midrule \endfirsthead", r"\toprule Item & Topic & Requirement & Reported & Where \\ \midrule \endhead", r"\bottomrule \endfoot"]
for it in items:
    P.append(" & ".join(esc(c).replace("--", "--") for c in it) + r" \\")
P += [r"\end{longtable}}"]
open(os.path.join(HERE, "app_prisma.tex"), "w").write("\n".join(P) + "\n")
print("static done")

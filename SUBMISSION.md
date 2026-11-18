# Submission log

- **Journal:** Journal of Economy and Technology (KeAi)
- **Status:** submitted (author-confirmed, October 2026)
- **Files submitted:** `manuscript/Anonymous_Manuscript_v2026-10-19.pdf` (44 pages, anonymised) and `manuscript/Title_Page_v2026-10-19.pdf`
- **Source of the submitted version:** commit `52a3a4c` on `main`; the full (non-anonymous) manuscript is `manuscript/Dang_Digital-waves-income-gaps_manuscript_v2026-10-19.pdf`
- **Content at submission:** 88 included studies; pilot meta-regression on 22 studies with a headline estimate; World Bank macro-panel analysis; search stated as incomplete (OpenAlex, Crossref, NBER, first page of four Google Scholar queries)
- **Manuscript ID:** JETECH-D-26-00130 (Editorial Manager)
- **Decision:** returned by the associate editor before peer review (editorial assessment, 18 Nov 2026); resubmission with major changes invited. No reviewer comments.

## Open items declared in the paper
- Hand check of the extractions: several random samples, sizes and corrections not logged
- Protocol not registered before the search
- Eleven Google Scholar queries, Scopus, Web of Science and EconLit not searched

## Before revising
Any revision should start from the files in `review/` and `manuscript/`, rerun `review/scripts/*` (merge, second pass, pilot, exploratory questions), rebuild with `manuscript/build_*.py` and `manuscript/build_submission.py`, and save new dated PDFs rather than overwriting these.

## Correspondence
- **20 Oct 2026, editorial office, initial administrative screening:** topic in scope, declarations present, no duplicate references. One request: the keywords in the submission metadata (digital technology; artificial intelligence; income level; systematic review; meta-regression) differ from those in the manuscript (digital technology; ICT; artificial intelligence; income level; systematic review; meta-regression; event study). The editors recommend the full manuscript set and will send the paper to external review once the metadata is standardised and the submission is resubmitted.
- **Action (author, on the submission site):** replace the metadata keywords with the manuscript set: the submission system allows only five keywords, so the manuscript was changed to match the metadata instead: `digital technology; artificial intelligence; income level; systematic review; meta-regression`. Current PDFs: `manuscript/Anonymous_Manuscript_v2026-10-20-r2.pdf` and `manuscript/Title_Page_v2026-10-20-r2.pdf` (full manuscript: `manuscript/Dang_Digital-waves-income-gaps_manuscript_v2026-10-20-r2.pdf`); resubmit with these. Revision r2 also removes every reference to repository file names from the manuscript (the data and code link is on the title page only) and lists the four Google Scholar queries in Appendix C.
- **Resubmitted (author-confirmed, October 2026):** with five keywords in both the metadata and the manuscript, and the PDFs `Anonymous_Manuscript_v2026-10-20-r2.pdf` and `Title_Page_v2026-10-20-r2.pdf`. Next step: the editorial office sends the paper to external peer review. Add reviewer comments and the decision here when received.

## Associate editor decision (before peer review)
The manuscript cannot go to peer review in its present form. Points raised:
1. Search critically incomplete (no Scopus, Web of Science, EconLit; 29 of 40 first-page Google Scholar results missing from the main search); pooled and moderator estimates are conditional on what was found. Either complete the search or downgrade the quantitative synthesis.
2. The meta-regression is unstable (moderator signs flip when studies are added; 22 headline papers; optimistic clustered SEs); the identification-strategy restriction contradicts H4. The moderator analysis should not occupy a central place.
3. The four macro-panel designs give contradictory results with no principled preference; event-study estimates at ten years (about 48 log points) are implausible but still discussed.
4. Extraction relies on AI output not fully verified by a person; the hand check was not logged (sample size, corrections), so it cannot be assessed.
5. Not publication-ready: studies are cited by internal IDs (e.g. study 9102) instead of author-year; process-log language ("garbled tables stay garbled").
6. Single reviewer, no registration, model-based adjudication: noted as a design choice, flagged under PRISMA 2020.
7. For resubmission the editor expects: (i) a substantially expanded search or a reframing as a pilot mapping exercise rather than a systematic review; (ii) removal or major rework of the unstable moderator analysis; (iii) a clearer contribution from the panel section or its reduction to a supplementary exercise; (iv) full human verification of all extracted effect sizes; (v) a complete rewrite without internal IDs or process-log language.

## Revision for resubmission (18 Nov 2026, draft)
Direction agreed with the author: reframe the paper as a **pilot evidence map**, not a systematic review.
- Title: *Do the gains from digital technology waves differ by income level? A pilot evidence map of cross-country studies*. Keywords (5): digital technology; artificial intelligence; income level; evidence map; productivity.
- Meta-regression demoted to one descriptive pooled figure (0.16, 22 studies) with its instability stated; moderator regressions, small-study tests and sensitivity moved to Appendix `app:sens` and not interpreted; hypotheses H1 to H6 replaced by four questions.
- Macro-panel analysis reduced to a one-page supplementary check; full tables moved to the appendix; the ten-year event-study estimates are no longer discussed in the main text.
- Studies cited by author and year (data: `review/data/study_citations.csv`; seven authors were completed by web search and should be confirmed); internal IDs and process-log wording removed; appendix of included studies is now the reference list.
- **Still open before resubmitting:** the author's check of the 22 headline estimates against the source papers (`review/verification/human_verification_sheet.pdf`). The Methods contain a marked placeholder for the number of studies verified and corrections; the Abstract and Limitations already say the author verified these estimates, so they must not be submitted until the check is done.
- Draft PDFs: `manuscript/Anonymous_Manuscript_v2026-11-18-evidence-map-DRAFT.pdf`, `manuscript/Title_Page_v2026-11-18-evidence-map-DRAFT.pdf`, `manuscript/Full_Manuscript_v2026-11-18-evidence-map-DRAFT.pdf`.
- The title and keywords in the submission system must be changed to match.

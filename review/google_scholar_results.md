# Google Scholar supplementary search: first results

Query G1, first page (10 results), pasted by the author on 4 October 2026. Checked against the 3,612 records of the main search by normalised title and by keywords.

Result: **9 of the 10 are not among the 3,612 records** (the tenth, Adeleye et al. 2022 on SAARC economies, is, and was excluded at abstract level for too few economies). The nine are listed in `data/scholar_g1_page1.csv`. All nine concern ICT, mobile or internet and economic growth across income groups, that is the review question itself.

Implication: the OpenAlex, Crossref and NBER search has a recall problem that the re-screening of retrieved records (`rescreening.md`) could not detect, because that check only looked at records the search had already retrieved. The estimate of about 180 missed records in `rescreening.md` is therefore a lower bound on what is missing.

## Query G2, first page (10 results), pasted by the author on 4 October 2026

Data: `data/scholar_g2_page1.csv`. Of the 10 results, 2 are already included (9104 and 9105, found through G1), 1 (Omer et al. 2026) appears twice, as a preprint and as a published version, and had been identified through G1. Five are new to the review (Karaman et al. 2021, Kumari and Singh 2024, Singh and Kumari 2023, Richard 2022, Ashraf et al. 2025). One, Yin and Choi 2023 (income inequality in the G20), was among the 3,612 records of the main search but was removed by the automated stage-1 rule, which found no technology term in its title or abstract ("digitalization" is not in the term list). That is a second source of missed records, separate from the retrieval problem: the stage-1 rules were too narrow. Four full texts were requested (Karaman et al., Kumari and Singh, Yin and Choi, and Omer et al. in the MDPI version). Singh and Kumari 2023 is probably an earlier version of Kumari and Singh 2024 and was not requested; Ashraf et al. study financial development as the outcome and were not requested; Richard 2022 is from a venue the author should judge.

# Google Scholar supplementary search: first results

Query G1, first page (10 results), pasted by the author on 4 October 2026. Checked against the 3,612 records of the main search by normalised title and by keywords.

Result: **9 of the 10 are not among the 3,612 records** (the tenth, Adeleye et al. 2022 on SAARC economies, is, and was excluded at abstract level for too few economies). The nine are listed in `data/scholar_g1_page1.csv`. All nine concern ICT, mobile or internet and economic growth across income groups, that is the review question itself.

Implication: the OpenAlex, Crossref and NBER search has a recall problem that the re-screening of retrieved records (`rescreening.md`) could not detect, because that check only looked at records the search had already retrieved. The estimate of about 180 missed records in `rescreening.md` is therefore a lower bound on what is missing.

## Query G2, first page (10 results), pasted by the author on 4 October 2026

Data: `data/scholar_g2_page1.csv`. Of the 10 results, 2 are already included (9104 and 9105, found through G1), 1 (Omer et al. 2026) appears twice, as a preprint and as a published version, and had been identified through G1. Five are new to the review (Karaman et al. 2021, Kumari and Singh 2024, Singh and Kumari 2023, Richard 2022, Ashraf et al. 2025). One, Yin and Choi 2023 (income inequality in the G20), was among the 3,612 records of the main search but was removed by the automated stage-1 rule, which found no technology term in its title or abstract ("digitalization" is not in the term list). That is a second source of missed records, separate from the retrieval problem: the stage-1 rules were too narrow. Four full texts were requested (Karaman et al., Kumari and Singh, Yin and Choi, and Omer et al. in the MDPI version). Singh and Kumari 2023 is probably an earlier version of Kumari and Singh 2024 and was not requested; Ashraf et al. study financial development as the outcome and were not requested; Richard 2022 is from a venue the author should judge.

## Query G4, first page (10 results), pasted by the author on 4 October 2026

Data: `data/scholar_g4_page1.csv`. Of the 10 results, 1 is already included (422, Yong et al.), 2 were in the main search (Ahmed 2010, excluded at abstract stage; Ahmed 2017, retrieved but without an abstract and not read), 1 is a review (Biagi 2013) and 1 covers one country only (Li et al. 2020, China). Five are new and eligible on title and abstract: Asongu and Acha-Anyi 2020, Samoilenko and Osei-Bryson 2008, Dedrick et al. 2013, Rehman and Nunziante 2023 and, as an optional request, Akaev and Sadovnichii 2021. The yield is lower than for G1 and G2: 4 requested out of 10, against 6 of 10 for G1 and 4 of 10 for G2. Two of the new ones were published before 2010, so older studies are under-represented in the main search too.

## Query G7, first page (10 results), pasted by the author on 5 October 2026

Data: `data/scholar_g7_page1.csv`. Of the 10 results, 1 is already included (1564, Cetin and Kutlu), 2 were in the main search (Gonzales 2023, judged includable on the abstract but never read for lack of a full text; Khan et al. 2024, excluded at abstract stage), 1 covers one economy only (Kurantin 2026) and 2 are from venues the reviewer cannot place (Alotaibi, no venue; Inal et al., an engineering journal) and were not requested. Five full texts were requested: Aly 2022, Saba 2025, Maswana 2024, Amavilah 2026 and Gonzales 2023. After this page the author and the reviewer agreed to stop requesting from Google Scholar: queries G3, G5, G6 and G8 to G15 have not been run.

## Query G3, first page (10 results), pasted by the author on 18 November 2026

Data: `data/scholar_g3_page1.csv`. Of the 10 results, 3 are already included (Samariya et al., Abdelhak et al., Yin and Choi), 2 are the Omer et al. paper already read and excluded (published and preprint versions), 1 covers one country (Ruan et al., Chinese provinces) and 1 is a student thesis (Ibrahim). Three are new and were requested: Wang and Shen 2024, Donnibe et al. 2026 and Bergantino and Nademi. The raw list of 3,612 records of the main search was not available in this session, so novelty was checked against the screening files that remain (abstract and title stages), not against the full list.

## Query G6, first page (10 results), pasted by the author on 18 November 2026

Data: `data/scholar_g6_page1.csv`. Of the 10 results, 2 are already included, 1 was excluded at abstract stage (fewer than 10 economies) and 1 has financial inclusion as its exposure, not ICT. Four are new and requested (Oyedotun and Makoni 2026, Kouladoum et al. 2022, Alimi and Okunade 2020, Anifowose and Chummun 2025); two more are optional (Onyejiaku et al. 2026, digital financial inclusion as exposure; Gebrehiwot and Makina 2015, mobile penetration as one determinant).

## Query G5, first page (10 results), pasted by the author on 18 November 2026

Data: `data/scholar_g5_page1.csv`. Of the 10 results, 2 are already included, 1 (Omar and Inaba) was seen in G6 and is not eligible because financial inclusion is its exposure. Five are new and requested (Popowska 2022, Phan 2023, Asongu et al. 2021, Shah and Krishnan 2024, Richmond and Triplett 2018); two are optional (Polloni-Silva et al. 2021, financial inclusion as exposure; Yilmaz and Koyuncu 2018, venue to be judged).

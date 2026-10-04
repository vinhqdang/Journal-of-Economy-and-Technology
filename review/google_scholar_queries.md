# Google Scholar queries (supplementary search, to run by the author)

Scopus and Web of Science are not available, so this supplementary search uses Google Scholar. The blind re-screening (`rescreening.md`) suggests that the OpenAlex, Crossref and NBER searches missed records, so this search is meant to catch them. Google Scholar queries are limited to about 256 characters and cannot be fully reproduced (results are ranked and can change), so the search is described in the paper as supplementary, with the date and the number of results screened per query.

## How to run

1. Install the free program Publish or Perish (Harzing) and choose Google Scholar as the source, or use scholar.google.com directly.
2. For each query below: set the years 1995 to 2026, sort by relevance, and take the first 200 results (20 pages of 10 in the web interface; in Publish or Perish set the maximum results to 200).
3. Export every query as CSV (Publish or Perish: Save results, CSV) with title, authors, year, source and DOI where available. Do not edit the files. Send them (or put them in the project) and each file's query name (G1 to G15).
4. The records are then merged and deduplicated against the 3,612 already screened, the new ones are screened blind (two independent readers), and the included ones are added to the review. Record the search date.

## Queries

| Name | Query (copy exactly) | Characters |
|---|---|---|
| G1 Output, general | `("mobile phones" OR "mobile telephony" OR internet OR broadband OR ICT) "economic growth" "developing countries" "income groups" panel cross-country` | 148 |
| G2 Output, income groups | `"information and communication technology" growth "low-income" "middle-income" "high-income" countries panel GMM` | 112 |
| G3 Digital economy | `"digital economy" OR digitalization "economic growth" countries "income level" heterogeneity OR threshold panel` | 111 |
| G4 Productivity and complements | `(internet OR mobile OR ICT) "labor productivity" OR "total factor productivity" countries "human capital" OR institutions interaction OR threshold` | 146 |
| G5 Distribution | `(ICT OR internet OR mobile OR digital) "income inequality" OR poverty "developing countries" panel data` | 103 |
| G6 Financial inclusion | `(mobile OR internet OR digital) "financial inclusion" countries panel "developing countries" OR "sub-Saharan Africa" OR "Asia"` | 126 |
| G7 AI and growth | `"artificial intelligence" "economic growth" OR productivity countries panel "developing countries" OR "emerging economies" OR "income"` | 134 |
| G8 AI and labour | `"artificial intelligence" employment OR wages OR unemployment countries panel "income level" OR "developing countries"` | 118 |
| G9 AI, energy, carbon | `("artificial intelligence" OR robots OR digitalization) "carbon emissions" OR "energy consumption" countries panel income` | 121 |
| G10 Structural change | `(ICT OR internet OR digital) "structural transformation" OR "structural change" OR "export diversification" countries panel` | 123 |
| G11 Labour market | `(ICT OR internet OR mobile) employment OR unemployment "labor market" "developed and developing countries" panel` | 112 |
| G12 Digital divide | `"digital divide" "economic growth" OR productivity "low-income countries" OR "developing countries" empirical` | 109 |
| G13 Living standards | `(mobile OR internet OR ICT) health OR education OR schooling OR "human development" countries panel "developing countries"` | 122 |
| G14 Existing meta-analyses | `"meta-analysis" (ICT OR telecommunications OR internet OR broadband) "economic growth" OR productivity` | 102 |
| G15 Existing reviews | `"systematic review" OR "meta-analysis" "artificial intelligence" OR digital "economic growth" OR employment countries` | 117 |

All queries are within Google Scholar's length limit. G14 and G15 look for existing meta-analyses and systematic reviews, which the protocol requires and which have not yet been searched for in a systematic way.

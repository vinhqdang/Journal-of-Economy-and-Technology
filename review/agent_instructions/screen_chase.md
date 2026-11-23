# Title and abstract screening of citation-search records

Each record: id, year, title, venue, abstract (may be empty).

Eligible (decision "include") only if all hold:
1. Quantitative empirical study with its own estimation (panel regression, IV, GMM, ARDL, growth accounting, event study, structural estimation). Not reviews, meta-analyses, theory, conceptual or bibliometric papers.
2. Exposure is adoption, diffusion, investment or capability of ICT in general, mobile telephony, internet or broadband, crypto-assets or AI (including robots/automation and digital-economy indices built mainly from ICT).
3. Outcome in at least one family: output/productivity/growth; structural change; labour market (employment, wages, skills); poverty and distribution (inequality, poverty); living standards beyond income (consumption, health, schooling, financial inclusion, human development); resource cost (electricity use, carbon/CO2 intensity or emissions).
4. Cross-country: at least 10 economies, or an explicit comparison of income groups (any number of economies for AI). Single-country, firm- or household-level studies within one country are excluded.
5. Published 1995 or later, in English.

Decision values: "include", "maybe" (abstract missing or ambiguous but plausibly eligible), "exclude".
Exclusion code when excluding: E1 too few economies or single country; E2 exposure not eligible (e.g. technology is only the outcome, or generic innovation/R&D/financial development); E3 outcome not eligible; E4 not an empirical study with own estimation; E5 other.

Also code "income_split": "yes" if the title/abstract says the study estimates or compares effects across income groups, developed vs developing, OECD vs non-OECD, or by income level/threshold; "no" if clearly not; "unclear" otherwise.

Output a JSON list: [{"id": "...", "decision": "...", "code": "E1|E2|E3|E4|E5|null", "income_split": "...", "reason": "max 15 words"}], one entry per input record, no omissions.

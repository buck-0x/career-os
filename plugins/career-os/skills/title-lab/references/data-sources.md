# Title Market Data Sources

Use these in order. Each step works without an API key; keys only add volume and structure. Tag every finding `[researched: <URL>]` with the access date.

## 1. O*NET (occupation, reported titles, related occupations)

US Department of Labor occupational database: 900+ occupations, each with sample reported job titles, related occupations, tasks, skills, and wage links.

- **No key:** search O*NET OnLine and read the occupation summary pages with WebFetch.
  - Search: `https://www.onetonline.org/find/result?s=<title, url-encoded>`
  - Summary: `https://www.onetonline.org/link/summary/<O*NET-SOC code>` (e.g. `15-1254.00`). Use its "Sample of reported job titles", "Related occupations", and wage sections.
- **With a key:** O*NET Web Services (free registration at services.onetcenter.org) offers the same search and occupation reports as a REST API. Check the current reference for endpoint paths; if the user has set up a key, they'll say where it is. Never ask them to paste the key into chat.
- **Attribution (required; O*NET data is CC BY 4.0)** whenever O*NET data appears in a workspace file, add this line with a link: "This file incorporates information from [O*NET Web Services](https://services.onetcenter.org/) by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). O*NET® is a trademark of USDOL/ETA."
- **Limits:** hybrid titles collapse into broad codes (a search for "design engineer" returns mechanical and aerospace engineering first). Use O*NET for the anchor layer and adjacent titles, not to define the expressive layer. If no code fits, say so.

## 2. ESCO (users outside the US, other languages)

The European Commission's multilingual occupations and skills taxonomy, with a public REST API (`https://ec.europa.eu/esco/api`) and a browsable portal (`https://esco.ec.europa.eu`). O*NET also publishes an O*NET-to-ESCO crosswalk. Use it for the user's local title vocabulary and language.

## 3. Wage floor (BLS OEWS)

Bureau of Labor Statistics Occupational Employment and Wage Statistics by SOC code, reachable from the O*NET summary's wage section or `https://www.bls.gov/oes/`. The BLS public API works without a key at 25 queries a day.

Treat it as a **floor**, not a market rate: broad codes under-describe hybrid roles, and the API returns only the latest year. Compare against posted ranges in live postings, and label both with source and date.

## 4. Live postings (meaning and demand of the exact title string)

Search job boards and company career pages for the exact title in quotes. Record:
- a rough count of current postings and where they cluster (company type, industry, location)
- 2–3 example postings with what they actually ask for
- posted pay ranges, where the posting states them

This is the only reliable source for emerging titles, whose meaning shifts within months.

## Not usable

- **Lightcast:** free self-serve access ended in April 2026; commercial use needs a contract.
- **Levels.fyi:** terms forbid scraping and AI training. The user may paste numbers they looked up; tag those `[source: Levels.fyi, pasted by user, <date>]`.
- **LinkedIn Economic Graph:** approved researchers only.

## Privacy

Search with the title and location only. Never put the user's name, current employer, salary, or other restricted ground-truth details into a search query or URL.

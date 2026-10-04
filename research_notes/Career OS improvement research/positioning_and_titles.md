# Positioning Methods, Title Data Sources, and Hiring-Side Evidence (for title-lab and positioning-studio)

Research date: 2026-10-04. Scope: frameworks transferable to individual positioning; structured title data with agent-queryable APIs; how recruiters and ATS actually process titles and profiles; evidence on hybrid titles; market-validation methods.

## Q1: Which positioning frameworks transfer to individuals, and what concrete steps carry over?

### Takeaway
April Dunford's five-component method is the most directly transferable: it maps cleanly onto career-os's For / Problem / What I am / How I'm different / Proof / Not for structure, and its strongest lesson for titles is "position in an existing market category first; create a category only with momentum." Play Bigger's "Point of View" and StoryBrand's "customer as hero" are useful for bios and intros, not for title choice.

### Cited Findings
- Dunford's sequence starts from competitive alternatives ("What would customers do if our solution didn't exist?"), then differentiated capabilities, value for customers, best-fit customer segmentation, and finally market category: the category is chosen last, as the context that makes the value obvious — [Dunford, Quickstart Guide to Positioning](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning)
- Dunford recommends positioning in an existing market by default; category creation is described as high-risk because it requires teaching the market new terminology; she cites that about 90% of recent IPOs used existing markets, and recommends a progressive approach (start in an existing category, expand boundaries later) — [Dunford, Quickstart](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning)
- Dunford warns against "phantom competitors": alternatives that are theoretically relevant but never actually show up in deals; list only alternatives buyers genuinely consider — [Dunford, Quickstart](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning)
- The longer 10-step process from *Obviously Awesome* begins with "understand the customers who love your product," then aligns vocabulary and drops "positioning baggage," lists true alternatives, isolates unique attributes, maps attributes to value themes, and determines who cares a lot — [Userlist case study of the 10-step method](https://userlist.com/blog/positioning-overhaul/); [Startup Archive summary](https://www.startuparchive.org/p/april-dunford-s-five-steps-of-product-positioning)
- Play Bigger's Point of View (POV) frames a category problem, the consequences of not solving it, a vision of the future, and the company's unique answer; it is explicitly a narrative to "move a market," not a pitch — [Play Bigger, What is Category Design](https://playbigger.com/what-is-category-design); [Notion Capital summary](https://www.notioncapital.com/resources/category-design-with-play-bigger)
- StoryBrand SB7: a character (customer) with a problem meets a guide who gives a plan, calls them to action, helps avoid failure, ends in success; central rule is the customer is the hero and the brand is the guide — [Umbrex SB7 summary](https://umbrex.com/resources/frameworks/marketing-frameworks/storybrand-sb7-framework/)

### Inferences
- Concrete transfers for positioning-studio (inference, mapping Dunford onto careers):
  1. **Competitive alternatives** = "who would the hiring manager hire, or what would they do, if you did not exist?" For a design engineer: a frontend engineer plus a designer pair, an agency, a design-systems contractor, or "ship without polish." This should become an explicit, required step before "How I'm different," and fill the "Not for" field (teams whose real alternative is a pure specialist).
  2. **Differentiated capabilities -> value** maps to "How I'm different" -> "Proof." Enforce that each unique attribute has a value statement and a proof artifact; drop attributes that have none.
  3. **Best-fit customer** = hiring context (company stage, team shape, product type) rather than demographic; this is the "For" field.
  4. **Market category** = the searchable anchor title. Dunford's "existing market first" maps directly to the title-stack design: anchor title must be an existing, searched category; the expressive positioning title is a sub-segment framing ("big fish, small pond" style narrowing); a coined title is category creation and should be flagged as high-risk unless the user already has inbound momentum.
  5. **Phantom competitors** check: an anti-pattern stress test where the user differentiates against roles that never actually compete for the same requisition.
  6. Dunford's step "understand the customers who love your product" maps to mining past managers/clients who valued the user most; a good input-collection step.
- Play Bigger POV is useful for the long-form bio or a "point of view" paragraph (what the user believes about how design and engineering should work), but category design should not drive the anchor title.
- StoryBrand fits intros/outreach: frame the hiring manager's problem as the story, the candidate as the guide. Good structural check for "intro" outputs (does it open on the reader's problem, not the candidate's history?).

### Gaps
- No peer-reviewed research found validating Dunford, Play Bigger, or StoryBrand applied to individual job seekers; transfers above are inference.
- Did not research Jobs-to-be-Done applied to careers or academic personal-branding literature in this pass (tool budget); the JTBD "hire" metaphor (what job is the employer hiring this role to do?) is a plausible addition but unsourced here.

## Q2: Which structured title data sources are free with APIs an agent could query (normalization, demand, comp, adjacent titles)?

### Takeaway
The free, agent-friendly core is **O*NET Web Services** (title normalization, alternate titles, related occupations; free with API key, CC BY 4.0) plus **ESCO API** (free, multilingual occupations/skills, crosswalk to O*NET) plus **BLS OEWS via BLS API** (comp/employment by SOC; free key). Lightcast closed its self-serve free tier in April 2026; Levels.fyi and LinkedIn Economic Graph are not open APIs. None of the free government taxonomies resolve emerging hybrid titles (design engineer, creative technologist, FDE) to distinct occupations, so live postings remain necessary for those.

### Cited Findings
**O*NET Web Services (US DoL)**
- Free REST API (current v2, OpenAPI 3.1 spec; v1.9 still available for legacy), X-API-Key auth after developer registration; data is CC BY 4.0 and attribution is required in applications — [O*NET Web Services About](https://services.onetcenter.org/about)
- Rate limits are "best-effort," throttled under heavy load; high-volume users are told to cache or download the database — [O*NET Web Services About](https://services.onetcenter.org/about)
- Keyword search returns occupations matching a word, phrase, title, or full/partial O*NET-SOC code, closest matches first; covers 900+ occupations — [O*NET Reference v2](https://services.onetcenter.org/reference/); [Keyword search reference](https://services.onetcenter.org/v1.9/reference/online/search)
- Occupation reports include "sample of reported titles," a subset of the full Alternate Titles list drawn from top incumbent and employer write-in titles — [O*NET occupation reports v2](https://services.onetcenter.org/reference/online/occupation); [O*NET Alternate Titles procedures (PDF)](https://www.onetcenter.org/dl_files/AltTitles.pdf)
- O*NET Web Services includes an ESCO crosswalk search endpoint — [O*NET ESCO crosswalk reference](https://services.onetcenter.org/reference/online/crosswalk/esco)
- Full database is also downloadable — [O*NET Database](https://www.onetcenter.org/database.html)

**ESCO (European Commission)**
- Public REST API for searching and browsing ESCO occupations, skills, and concept schemes by URI, with language parameter (multilingual); supports machine-to-machine use across ESCO versions — [ESCO REST API docs](https://ec.europa.eu/esco/api/doc/esco_api_doc.html)
- (No API key requirement was stated in the docs excerpt reviewed; verify before relying on it.)

**BLS OEWS (comp and employment by SOC)**
- BLS Public Data API v1 needs no key: 25 queries/day, 25 series/query, 10 years; v2 requires free registration: 500 queries/day, 50 series/query, 20 years — [BLS Developers](https://www.bls.gov/developers/home.htm); [BLS API FAQ](https://www.bls.gov/developers/api_faqs.htm)
- For OEWS series the API returns only the most recent year; historical data needs the OEWS data tables — [jobspipe BLS API guide](https://jobspipe.dev/blog/bls-api) (secondary source)

**Lightcast (formerly Emsi)**
- Titles API offers job title search and normalization against a taxonomy of 75,000+ titles; Skills taxonomy 33,000+ skills, versioned monthly — [Lightcast Taxonomy API features](https://docs.lightcast.io/lightcast-api/docs/free-api-features); [jobspipe Lightcast guide](https://jobspipe.dev/blog/lightcast-api)
- Since April 2026 the free self-serve model ended: free "public-good" tier is for nonprofits/public sector only (skills extraction capped at 50 calls/month); commercial use requires a contract license with no public pricing; OAuth2 client-credentials auth — [jobspipe Lightcast guide](https://jobspipe.dev/blog/lightcast-api); [Lightcast API Access](https://lightcast.io/open-skills/access)
- The Skills Taxonomy itself remains browsable/open — [Lightcast Open Skills](https://lightcast.io/open-skills)

**Levels.fyi**
- No public developer API; data is proprietary; terms prohibit scraping, bulk export, building databases, or AI training; commercial access via a Levels.fyi Data License — [Levels.fyi Terms](https://www.levels.fyi/about/terms.html)

**LinkedIn Economic Graph**
- Research access only via the Economic Graph Research Program: approved researchers work in a LinkedIn-hosted sandbox, cannot publish data without consent or retain it beyond project scope — [LinkedIn Engineering, Economic Graph details](https://engineering.linkedin.com/teams/data/projects/economic-graph-research/economic-graph-details); [EGRP announcement](https://engineering.linkedin.com/blog/2017/03/announcing-the-economic-graph-research-program)

**Indeed Hiring Lab**
- Publishes free reports and analyses (no general public title API found); e.g., 2026 analysis of AI-touched job titles across US and Europe — [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-is-no-longer-just-a-tech-occupation-story/)

### Inferences
- Recommended title-lab pipeline (inference): (1) O*NET keyword search to map candidate anchor titles to SOC codes and pull alternate/reported titles and related occupations (adjacent-title candidates); (2) ESCO crosswalk for non-US users or multilingual variants; (3) BLS OEWS by SOC for a comp/employment baseline; (4) live job-board searches (current ad hoc WebSearch) for emerging titles, counting postings per exact title string. Steps 1-3 are free and API-keyed; the API keys are the user's to register, so the skill should degrade gracefully to WebSearch when no key is configured.
- Government taxonomies lag: hybrid titles collapse into broad SOC codes (e.g., web developers, software developers, art directors), so O*NET is good for the anchor/searchable layer and for adjacency, weak for the expressive layer. Comp from OEWS will under-describe hybrid roles; flag it as a floor/baseline, not a market rate.
- Licensing implications: O*NET requires attribution in any output that surfaces its data; Levels.fyi and LinkedIn data should not be scraped or stored by the skill.

### Gaps
- Did not verify O*NET v2 exact endpoint paths for related occupations / alternate titles beyond the occupation-report reference; check the v2 reference before implementing.
- Did not confirm whether ESCO API requires a key or has rate limits.
- No free source found for posting counts by exact title string (Indeed/LinkedIn do not offer public APIs for this); USAJobs and similar exist but were not researched.

## Q3: How do recruiters search and screen, and what does it imply for anchor titles and headlines?

### Takeaway
Hiring-side evidence converges on titles: recruiters search LinkedIn primarily by the Job Titles filter (Boolean-capable, can target headline), and in resume skims their eyes go first to current title and company. ATS "auto-rejection" is largely a myth, but ranking and recruiter skim behavior make the anchor title the single highest-leverage field.

### Cited Findings
- LinkedIn Recruiter and Recruiter Lite support Boolean (AND, OR, NOT, uppercase) in the Job titles, Companies, and Keywords filters — [LinkedIn Help: Boolean in Recruiter](https://www.linkedin.com/help/recruiter/answer/a415295)
- Recruiter filters (Job titles, Companies, Skills, Schools, etc.) offer Can have / Must have / Doesn't have; sourcing guides advise searching titles in the title filter rather than keyword box because keywords match anywhere on a profile — [Leonar, LinkedIn Recruiter search filters 2026](https://www.leonar.app/blog/linkedin-recruiter-search-filters/) (vendor blog)
- A lowercase "headline:" operator can be used in the Job Title and Companies filters to target headlines — [ZoomInfo/Pipeline Boolean guide 2026](https://pipeline.zoominfo.com/recruiting/boolean-searches-for-recruiters) (secondary)
- Sourcing best practice is to OR together a set of related titles rather than exclude — [ZoomInfo/Pipeline](https://pipeline.zoominfo.com/recruiting/boolean-searches-for-recruiters)
- Ladders 2018 eye-tracking study: initial resume skim averages 7.4 seconds (up from about 6 seconds in 2012); recruiters look at current title and company, then previous title/company, then dates, then education; simple layouts with clear headings, F/E-pattern, bold titles did best; multi-column, cluttered layouts fared poorly — [HR Dive](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/); [Ladders study PDF](https://www.theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf)
- Enhancv 2025 interviews with 25 US recruiters: 92% said their systems do not auto-reject based on formatting, missing keywords, or match scores; 8% used auto-rejection, only for roles with very specific requirements; 44% had ATS fit-scores available but most disabled them or treated them as a rough guide — [IT Brief on Enhancv study](https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth)
- The widely cited "75% of resumes rejected by ATS" stat traces to 2012 marketing material from Preptel, a defunct resume-optimization company — [IT Brief](https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth); [Enhancv ATS explainer](https://enhancv.com/blog/what-is-ats/)
- Counterpoint: even without auto-rejection, when 180+ apply and a recruiter reviews the top 20, low ranking is functionally rejection — [IT Brief](https://itbrief.co.uk/story/study-reveals-ats-rarely-auto-rejects-cvs-debunks-75-myth)
- Claims that the LinkedIn headline is "the highest-weighted field" and that headline plus current position are "approximately 60% of search ranking weight" appear in career-advice blogs citing a "LinkedIn 2026 Recruiter Search Guide" — [The Interview Guys](https://blog.theinterviewguys.com/linkedin-keywords/); I could not find this LinkedIn guide or any LinkedIn primary source for the 60% figure; treat as unverified.
- Guidance to put key terms in the first ~80 characters (mobile/recruiter preview) of the 220-character headline is practitioner advice, not LinkedIn-documented — [same blogs](https://blog.theinterviewguys.com/linkedin-keywords/) (unverified)

### Inferences
- Anchor title should be an exact string recruiters type into the Job Titles filter, used both in the current-position title field and early in the headline. Expressive titles belong after the anchor (e.g., "Design Engineer | building ..."), never instead of it.
- Because recruiters OR related titles, title-lab should output the cluster of synonyms a recruiter would OR together (e.g., "Design Engineer" OR "UX Engineer" OR "Design Technologist" OR "Frontend Engineer") and check that the profile hits at least one high-volume member.
- The 7.4-second skim maps to career-os's "skim test": the stress test should simulate reading only current title + company + previous title + dates. If the title stack does not communicate the anchor in those fields, it fails.
- ATS guidance in outputs should drop "beat the bots" framing; the evidence supports writing for recruiter skim and search-filter matching, plus job-description keyword alignment for ranking.

### Gaps
- No primary LinkedIn documentation found on how Recruiter ranks results (field weights); all weighting claims are unverified.
- Ladders study is from 2018 and vendor-run (n=30 recruiters in the commonly reported version, not verified here); no newer independent eye-tracking study found.
- Enhancv sample is small (25 recruiters) and from a resume-builder vendor.

## Q4: Evidence on emerging hybrid titles in 2025-2026 postings

### Takeaway
Forward Deployed Engineer has the strongest quantitative evidence of explosive growth; "AI" in titles has broadly tripled; Design Engineer is now a canonical title at design-led tech companies (qualitative evidence); Creative Technologist remains an umbrella title concentrated in agencies/advertising, with no solid posting-volume data found.

### Cited Findings
- US job titles containing AI terms ("AI-touched" titles, min. five postings each) rose from 264 in Q1 2022 to 822 in Q1 2026; 63% of these US titles are outside tech occupations; Germany had 288, UK 160 — [Indeed Hiring Lab, July 2026](https://hiringlab.indeed.com/2026/07/08/ai-is-no-longer-just-a-tech-occupation-story/)
- 37% of the increase in US software development postings between May 2025 and May 2026 came from jobs with AI in the title; 71% from senior roles — [Indeed Hiring Lab, AI and Job Postings, July 2026](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/) (figures as reported in search summary; verify against page)
- GenAI-mentioning US postings rose 170% from Jan 2024 to Jan 2025 — [Indeed Hiring Lab, Rise of the GenAI Consultant](https://hiringlab.indeed.com/2025/02/27/ai-at-work-rise-of-the-genai-consultant/)
- FDE postings grew 1,165% (Jan-Oct 2024 vs Jan-Oct 2025) per Revealera data analyzed by Bloomberry, vs 12% for software engineers; Indeed reported 5,330 FDE postings in April 2026 vs 643 in April 2025 (+729%) — [Scaler summary](https://www.scaler.com/topics/forward-deployed-engineer-jobs-grew-1165-percent/); [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/forward-deployed-engineers-emerge-as-one-of-ais-fastest-growing-jobs/); [Paraform](https://www.paraform.com/blog/forward-deployed-engineer-demand-quadrupled) (secondary aggregators; underlying data sources are Revealera/Bloomberry, Live Data Technologies, Indeed)
- Design Engineer: Vercel describes design engineering as a no-handoff model where designers iterate with design engineers in Figma or code — [Vercel blog, Design Engineering at Vercel](https://vercel.com/blog/design-engineering-at-vercel); Vercel and Linear both post Design Engineer roles; a16z ran a Design Engineer Fellowship — [Medium, 2026 Design Job Description](https://medium.com/design-bootcamp/design-role-requirements-are-evolving-the-2026-design-job-description-7648fec59363) (secondary)
- Creative Technologist is described as an umbrella term; The Creative Group/Robert Half defines it as a technology-focused professional who understands the creative process and prototypes early; common in advertising, marketing, digital media — [Robert Half](https://www.roberthalf.com/us/en/insights/hiring-help/what-does-a-creative-technologist-really-do); [freeCodeCamp](https://www.freecodecamp.org/news/what-does-a-creative-technologist-do/)

### Inferences
- Title-lab should treat these differently: FDE and AI Engineer are now high-volume searchable anchors in AI-adjacent markets; Design Engineer is a valid anchor at design-led product companies but lower-volume overall, so pair it with an OR-synonym fallback (Frontend / UX Engineer) in context variants; Creative Technologist is an anchor mainly for agency/brand/experiential contexts and is weak in product-company searches.
- Because AI-in-title is spreading across non-tech roles, "AI" prefixes risk dilution; the stress tests should check whether an AI-prefixed title still signals the specific job.

### Gaps
- No reliable posting-volume time series found for "Design Engineer" or "Creative Technologist"; the skill would need live counts (job-board searches) at runtime.
- FDE growth figures come through secondary aggregators; underlying Revealera/Bloomberry and LinkedIn "42-fold" claims not verified at source.

## Q5: Methods to validate positioning with real market feedback

### Takeaway
The most concrete free, measurable feedback loop on the hiring side is LinkedIn's own profile analytics (Search Appearances, including searcher job titles and, in some modes, keywords found for), which lets a user run sequential before/after headline tests. Other methods (informational interviews, message testing) are well-established in practice but I found little hiring-specific evidence in this pass.

### Cited Findings
- LinkedIn Search Appearances shows how many times a member appeared in search over a period and aggregate insights about searchers, such as their companies and job titles; no individual searcher identities — [LinkedIn Help: Search Appearances](https://www.linkedin.com/help/linkedin/answer/a553050/view-your-profile-search-appearances); [LinkedIn Help: Profile search appearances](https://www.linkedin.com/help/linkedin/answer/a1588796)
- Practitioner sources report that a more detailed breakdown including keywords you were found for is available (previously tied to Creator Mode) — [Luan Wise](https://www.luanwise.co.uk/how-to-analyze-your-linkedin-profile-using-the-linkedin-dashboard) (secondary; feature availability changes, verify)
- Dunford's process grounds positioning in the customers who already value you most and in alternatives that actually appear in deals, i.e., evidence from real buyers rather than self-assessment — [Dunford Quickstart](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning)

### Inferences
- Validation protocol for positioning-studio (inference):
  1. **Sequential headline test**: change one variable (anchor title or headline order) at a time; hold 2-4 weeks; log Search Appearances count, searcher job titles (are recruiters/hiring managers in the target function showing up?), profile views, and inbound messages. LinkedIn offers no true A/B split, so results are confounded by time and activity; require a minimum window and note that.
  2. **Inbound tracking log**: record every inbound (who, title, what they referenced, fit to "For"); wrong-fit inbound is direct evidence for revising "Not for" and the anchor.
  3. **Message testing via informational interviews**: show 2-3 positioning variants to people matching the "For" persona and ask them to restate who the person is and what they would hire them for; mismatch = positioning failure (mirrors the existing "swap test").
  4. **Outreach reply rates** per positioning variant, as a stronger signal than views.
- The "wrong-fit" stress test can be grounded in data: compare the searcher job titles from LinkedIn analytics to the target "For" audience.

### Gaps
- No controlled studies found on LinkedIn headline A/B testing outcomes; no hiring-specific message-testing literature found in this pass.
- Did not research "The Mom Test" or informational-interview methodology sources (budget); these are commonly recommended but not cited here.
- LinkedIn analytics feature set changes frequently (Creator Mode was folded into general profile settings in 2024 per general knowledge; unverified here).

# Research Methodology

This document outlines the systematic approach used to compile and verify the Headbangers Ball dataset.

## Overview

The goal is to create a comprehensive, accurate dataset of all Headbangers Ball episodes through rigorous multi-source verification and systematic data collection.

## Research Phases

### Phase 1: Foundation Building
**Objective**: Establish basic episode timeline and host information

**Steps**:
1. Extract complete episode list from EpisodeHive
2. Cross-reference episode dates with TheTVDB
3. Verify host timeline against Wikipedia and IMDb
4. Create master episode skeleton (dates, hosts, episode numbers)

**Deliverable**: `episodes.csv` with dates and hosts

### Phase 2: Video Catalog Compilation
**Objective**: Document every music video aired

**Steps**:
1. Extract video listings from EpisodeHive for each episode
2. Verify artist names and song titles against Metal Archives
3. Add album information and release years from MusicBrainz
4. Cross-check against YouTube archives where available
5. Mark episodes with incomplete video listings for follow-up

**Deliverable**: `videos.csv` linked to episodes

### Phase 3: Special Segments Research
**Objective**: Document interviews, location shoots, and special programming

**Steps**:
1. Review episode descriptions from all sources
2. Search YouTube for episode uploads to identify segments
3. Check music blogs and fan sites for segment mentions
4. Document location shoots, major interviews, themed episodes
5. Note significance and context

**Deliverable**: `special_segments.csv` with detailed descriptions

### Phase 4: Verification and Quality Assurance
**Objective**: Ensure data accuracy and completeness

**Steps**:
1. Cross-reference all dates against multiple sources
2. Verify spelling of all band names and song titles
3. Check for duplicate entries
4. Validate episode sequencing
5. Confirm host tenures align with established timeline
6. Flag low-confidence entries for additional research

**Deliverable**: Validated, citation-complete dataset

### Phase 5: Analysis and Documentation
**Objective**: Extract insights and patterns from complete dataset

**Steps**:
1. Analyze band appearance frequencies
2. Track genre evolution over time
3. Document host-specific programming trends
4. Identify milestone episodes
5. Create statistical summaries

**Deliverable**: `docs/STATISTICS.md` and analysis scripts

## Data Collection Procedures

### Episode Research Workflow

For each episode, follow this systematic process:

```
1. Locate episode in EpisodeHive
   ├─→ Record air date
   ├─→ Record host
   ├─→ Record video listings
   └─→ Note episode description

2. Cross-reference with TheTVDB
   ├─→ Verify air date
   ├─→ Check episode number
   └─→ Compare descriptions

3. Check IMDb
   ├─→ Verify host credits
   ├─→ Check for guest appearances
   └─→ Note any additional details

4. Search YouTube
   ├─→ Look for full episode
   ├─→ If found: verify video list against upload
   ├─→ Document any special segments
   └─→ Note video URL as citation

5. Research special segments
   ├─→ Check music blogs for mentions
   ├─→ Review fan site episode guides
   └─→ Document in special_segments.csv if applicable

6. Validate band/song information
   ├─→ Check Metal Archives for band names
   ├─→ Verify song titles via MusicBrainz
   └─→ Add genre classifications

7. Document citations
   └─→ Record all sources used for this episode
```

### Video Entry Workflow

For each music video:

```
1. Extract from episode listing
   ├─→ Artist name (standardize spelling)
   └─→ Song title (proper capitalization)

2. Research song details
   ├─→ Album name
   ├─→ Release year
   └─→ Genre classification

3. Additional research (optional, if time permits)
   ├─→ Video director
   └─→ Notable video facts

4. Link to episode
   └─→ Record play order if known
```

## Verification Standards

### Three-Tier Verification System

**Tier 1: High Confidence** ✓✓✓
- 3+ independent sources agree, OR
- 2+ sources + video evidence, OR
- Official MTV documentation

**Tier 2: Medium Confidence** ✓✓
- 2 independent sources agree
- No conflicting information

**Tier 3: Single Source** ✓
- Only 1 source available
- Flagged for additional verification
- Marked in notes as requiring confirmation

### Handling Discrepancies

When sources conflict:

1. **Date conflicts**: Prefer TheTVDB > EpisodeHive > other sources
2. **Host conflicts**: Check multiple sources; prefer IMDb for credits
3. **Video list conflicts**: Defer to video evidence if available
4. **Spelling variations**: Use official band spelling from Metal Archives

Document conflicting information in episode notes with format:
```
Source A reports [X]; Source B reports [Y]; needs verification
```

## Quality Control Checks

### Automated Validation

Scripts in `/scripts` directory perform:
- Date format validation (YYYY-MM-DD)
- Episode sequence checking (no gaps/duplicates)
- Citation presence verification (no empty citation fields)
- Cross-reference validation (all episode_ids exist)
- Duplicate detection (same video multiple times in episode)

### Manual Review

Periodic manual review for:
- Genre classification consistency
- Artist name standardization
- Episode description quality
- Special segment documentation completeness

## Data Entry Guidelines

### Formatting Standards

**Dates**
- Format: `YYYY-MM-DD` (ISO 8601)
- Example: `1990-05-19`

**Band/Artist Names**
- Use official spelling and capitalization
- Use ampersand (&) if official: `Crosby, Stills & Nash`
- No abbreviations unless official: `W.A.S.P.` not `WASP`

**Song Titles**
- Proper capitalization
- Include punctuation: `Don't Cry`
- Include subtitle if part of title: `November Rain (Album Version)`

**Genre Tags**
- Use standardized terms from schema
- Single primary genre per video
- Consistency across similar artists

**Citations**
- Format: `domain.com` or `domain.com/path`
- Multiple sources: separate with semicolon and space: `source1.com; source2.com`
- Always include at least one citation

### Special Cases

**Episode Not Found**
- Document in research notes
- Check if episode was pre-empted or canceled
- Flag for community assistance

**Incomplete Video List**
- Enter known videos
- Add note: `Incomplete video listing; requires verification`
- Flag episode for follow-up

**Conflicting Information**
- Enter most reliable source's data
- Document conflict in special_notes
- Add all conflicting sources to citations

**Guest Hosts**
- Primary host in `host` field
- Guest host in `guest_host` field
- Note context in special_notes if significant

## Research Tools

### Recommended Browser Extensions
- Video DownloadHelper (for backing up YouTube evidence)
- Web Scraper (for systematic data extraction)
- Wayback Machine integration (for archived sources)

### Recommended Software
- **Spreadsheet**: Excel, Google Sheets, or LibreOffice Calc
- **Text Editor**: For CSV editing with proper encoding (UTF-8)
- **Python**: For running validation scripts
- **Git**: For version control and collaboration

### Search Strategies

**Finding Episode Information**
```
"headbangers ball" [date] episode
"headbangers ball" [host name] [year]
site:episodehive.com "headbanagers ball"
```

**Finding Video Lists**
```
"headbangers ball" [date] "playlist"
"headbangers ball" episode [number] videos
site:youtube.com "headbangers ball" [date]
```

**Finding Special Segments**
```
"headbangers ball" interview [artist]
"headbangers ball" [event name]
"headbangers ball" location [place]
```

## Collaboration Protocol

### For Multiple Researchers

1. **Divide by era**: Assign different time periods to different researchers
2. **Use branches**: Each era gets a git branch for parallel work
3. **Regular syncs**: Weekly merge and conflict resolution
4. **Document decisions**: Log all resolution choices in research notes

### Community Contributions

1. **Issue tracking**: Use GitHub issues for missing episodes
2. **Pull requests**: Accept PRs with proper citations
3. **Review process**: Verify all contributed data before merge
4. **Credit contributors**: Maintain contributors list

## Timeline and Progress Tracking

### Recommended Milestones

- [ ] Phase 1: Complete episode skeleton (all dates and hosts)
- [ ] Phase 2a: Video lists for Classic MTV Era (1987-1995)
- [ ] Phase 2b: Video lists for MTV2 Revival (2003-2007)
- [ ] Phase 2c: Video lists for 2011-2012 Revival
- [ ] Phase 3: Special segments documented
- [ ] Phase 4: All entries verified with 2+ sources
- [ ] Phase 5: Statistical analysis complete

### Time Estimates

**Per Episode**:
- Basic entry (date/host): 5-10 minutes
- Video list (10-15 videos): 15-30 minutes
- Special segment research: 10-20 minutes
- Verification: 5-10 minutes

**Total Project** (estimated):
- ~400 episodes × 40 min avg = ~267 hours
- With multiple contributors: 3-6 months part-time

## Ethics and Best Practices

### Copyright Considerations
- We document factual information (air dates, song lists)
- No copyrighted video content stored in repository
- Links to YouTube for reference only
- Citations respect fair use for research

### Accuracy Over Speed
- Never rush entries
- When in doubt, flag for verification
- It's okay to leave fields empty if information not found
- Community can help fill gaps over time

### Transparency
- All sources cited
- Conflicts documented
- Assumptions made explicit
- Verification status clear

## Continuous Improvement

This methodology will evolve as:
- New sources are discovered
- Better tools become available
- Community feedback is received
- Challenges are encountered

Last updated: 2025-11-20

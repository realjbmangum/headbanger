# PRD: Headbangers Ball Archive V2 Redesign

## Overview
Complete visual and UX overhaul of the Headbangers Ball Archive website. The current design attempts an 80s metal aesthetic but suffers from poor readability, dated execution, and doesn't properly capture the iconic MTV Headbangers Ball vibe. V2 will deliver a polished, modern take on retro MTV aesthetics - dark, metal, neon-accented - while dramatically improving usability and adding new features.

## Goals
1. **Readable & usable** - High contrast, clear typography, intuitive navigation
2. **Authentic MTV aesthetic** - Capture the 1987-1995 Headbangers Ball era without looking amateurish
3. **Feature-rich** - Improved search, filtering, and episode discovery
4. **Mobile-first** - Fully responsive, works great on phones
5. **Success metric**: Users can quickly find and explore episodes without eye strain

## Non-Goals
- User accounts/authentication
- User-submitted content or comments
- Video playback (we're an archive/database, not a streaming service)
- E-commerce or monetization
- CMS/admin interface (continue using markdown/Jekyll)

## Design Direction

### Visual Language
- **Dark background** - True black (#0a0a0a) or near-black, not muddy grays
- **Neon accents** - Hot pink/magenta (#FF006E) and electric blue (#00D4FF) for that MTV glow
- **Chrome/silver text** - High contrast whites and silvers for readability
- **Subtle VHS/scan line textures** - Nostalgic but not distracting
- **Sharp edges + neon glow** - 80s geometry meets modern execution

### Typography
- **Headlines**: Bold, impactful sans-serif (Inter Black or similar)
- **Body**: Clean, highly readable (Inter or system fonts)
- **Abandon**: Overly decorative "metal" fonts that hurt readability

### Key Visual Elements
- Neon border/glow effects on cards (subtle, not overwhelming)
- Episode cards with clear hierarchy: date → title → host → metadata
- Color-coded era badges (Kevin Seal era, Adam Curry era, Riki Rachtman era, MTV2 era)
- VHS-style timestamps and episode numbers

---

## User Stories

### Story 1: Homepage Redesign
**As a** visitor landing on the site
**I want to** immediately understand what this is and start exploring
**So that** I can discover Headbangers Ball episodes

**Acceptance Criteria:**
- [ ] Hero section with logo, tagline, and key stats (455 episodes, 1987-2012)
- [ ] Quick links to browse by era (visual cards for each host era)
- [ ] "Random Episode" feature prominently displayed
- [ ] Recent/featured episodes section
- [ ] Search bar visible above the fold
- [ ] Verify in browser: homepage loads fast, looks great on mobile

**Technical Notes:**
- Keep Jekyll static generation
- Hero stats pulled from _data/stats.yml

---

### Story 2: New Color System & Typography
**As a** user reading episode details
**I want** text to be easily readable against the dark background
**So that** I don't strain my eyes

**Acceptance Criteria:**
- [ ] Background: #0a0a0a (near-black)
- [ ] Primary text: #FFFFFF (pure white)
- [ ] Secondary text: #B0B0B0 (light gray, still high contrast)
- [ ] Accent 1: #FF006E (hot pink/magenta)
- [ ] Accent 2: #00D4FF (electric blue)
- [ ] Success/positive: #00FF88 (neon green)
- [ ] All text passes WCAG AA contrast (4.5:1 minimum)
- [ ] Body text 16px minimum, line-height 1.6
- [ ] Verify in browser: text is crisp and readable at all sizes

**Technical Notes:**
- Update CSS variables in style.css
- Test with browser contrast checker

---

### Story 3: Episode Card Component
**As a** user browsing episodes
**I want** episode cards that show key info at a glance
**So that** I can quickly scan and find interesting episodes

**Acceptance Criteria:**
- [ ] Card shows: Air date, Episode title/number, Host, Era badge
- [ ] Neon border glow on hover (subtle, 2-3px)
- [ ] Era badges color-coded:
  - Kevin Seal (1987-1988): Blue
  - Adam Curry (1988-1990): Gold
  - Riki Rachtman (1990-1995): Pink/Magenta
  - MTV2 (2003-2012): Purple
- [ ] "View Details" link with arrow
- [ ] Cards work in grid (3 columns desktop, 2 tablet, 1 mobile)
- [ ] Verify in browser: hover effects work, cards align properly

**Technical Notes:**
- Create reusable card component/partial
- Use CSS Grid for layout

---

### Story 4: Episodes List Page Redesign
**As a** user wanting to browse all episodes
**I want** powerful filtering and a clean list view
**So that** I can find specific episodes easily

**Acceptance Criteria:**
- [ ] Search bar at top (searches title, host, guest names)
- [ ] Filter pills: Year dropdown, Era dropdown, Host dropdown
- [ ] Active filters shown as removable chips
- [ ] Episode count updates as filters applied ("Showing 52 of 455 episodes")
- [ ] Grid view (default) and list view toggle
- [ ] Pagination or infinite scroll for performance
- [ ] Clear "Reset filters" button
- [ ] Verify in browser: filtering is instant, no page reload

**Technical Notes:**
- Client-side filtering with JavaScript (already exists, improve it)
- Consider lazy loading for 455+ episode cards

---

### Story 5: Episode Detail Page Redesign
**As a** user viewing a specific episode
**I want** all episode information presented clearly
**So that** I can learn about what aired that day

**Acceptance Criteria:**
- [ ] Large header with air date and episode number
- [ ] Host info with era badge
- [ ] Guest hosts listed if any
- [ ] Video playlist section (if video data exists)
- [ ] Special segments/interviews section
- [ ] "Share" and "Copy link" buttons
- [ ] Previous/Next episode navigation
- [ ] Breadcrumb: Home > Episodes > 1990 > Episode 156
- [ ] Verify in browser: page looks complete, navigation works

**Technical Notes:**
- Use Jekyll episode layout
- Pull data from episode frontmatter

---

### Story 6: Statistics Page Enhancement
**As a** user curious about show history
**I want** interesting stats and visualizations
**So that** I can understand the show's scope and patterns

**Acceptance Criteria:**
- [ ] Total episodes by year (bar chart or visual representation)
- [ ] Host tenure timeline (visual)
- [ ] Most common guest hosts
- [ ] Era breakdown with episode counts
- [ ] Fun facts section (first episode, last episode, longest-running host)
- [ ] Verify in browser: stats load correctly, visualizations render

**Technical Notes:**
- Can use simple CSS-based charts (no JS library needed)
- Data from _data/stats.yml

---

### Story 7: Navigation & Header
**As a** user on any page
**I want** clear navigation that works on all devices
**So that** I can move around the site easily

**Acceptance Criteria:**
- [ ] Sticky header with logo and nav links
- [ ] Nav items: Home, Episodes, Stats, About
- [ ] Search icon in header that expands to search bar
- [ ] Mobile: hamburger menu with slide-out nav
- [ ] Active page highlighted in nav
- [ ] Header has subtle backdrop blur effect
- [ ] Verify in browser: nav works on mobile and desktop

**Technical Notes:**
- Already partially done, refine the mobile menu

---

### Story 8: Footer & About Page
**As a** user wanting to learn more
**I want** info about the project and how to contribute
**So that** I understand the archive's purpose

**Acceptance Criteria:**
- [ ] Footer: Project credit, GitHub link, "Built for the metal community"
- [ ] About page: Project history, data sources, methodology
- [ ] About page: How to contribute / submit corrections
- [ ] About page: Acknowledgments
- [ ] Verify in browser: links work, page is complete

---

### Story 9: Performance & Polish
**As a** user
**I want** the site to load fast and feel polished
**So that** I have a great experience

**Acceptance Criteria:**
- [ ] Page load under 2 seconds on 3G
- [ ] Smooth transitions and hover effects (no jank)
- [ ] No layout shift as page loads
- [ ] Favicon and social sharing meta tags
- [ ] 404 page styled to match site
- [ ] Loading states for any async operations
- [ ] Verify in browser: Lighthouse score 90+ on Performance

**Technical Notes:**
- Optimize images, lazy load where appropriate
- Minimize CSS/JS

---

## Technical Considerations

- **Stack:** Jekyll (static), Tailwind CSS or custom CSS, vanilla JS
- **Hosting:** Cloudflare Pages (already set up)
- **Data:** Continue using Jekyll collections and _data files
- **Dependencies:** Minimal - keep it simple and fast
- **Risks:**
  - 455+ episodes means episode list page could be slow - implement pagination
  - Complex CSS effects could hurt performance - keep animations subtle

## Open Questions
- Should we add a "Random Episode" API endpoint or keep it client-side?
- Do we want to add any new data (e.g., video thumbnails, band logos)?
- Should stats page have actual charts (Chart.js) or CSS-only visualizations?

## Task Checklist
- [ ] Story 1: Homepage Redesign
- [ ] Story 2: New Color System & Typography
- [ ] Story 3: Episode Card Component
- [ ] Story 4: Episodes List Page Redesign
- [ ] Story 5: Episode Detail Page Redesign
- [ ] Story 6: Statistics Page Enhancement
- [ ] Story 7: Navigation & Header
- [ ] Story 8: Footer & About Page
- [ ] Story 9: Performance & Polish
- [ ] Final review and testing

---

*Created: January 2026*

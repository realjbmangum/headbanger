# 📋 Immediate Next Steps

**Last Updated:** 2025-11-20

---

## 🔥 Current Sprint: MVP Website Foundation

### This Week (Priority 1)
- [ ] **Decide on tech stack**
  - Option A: Next.js + Vercel (modern, full-featured)
  - Option B: Jekyll + GitHub Pages (simple, free)
  - Option C: React SPA + Netlify (middle ground)
  - **Decision:** _____________________

- [ ] **Set up development environment**
  - [ ] Install chosen framework
  - [ ] Initialize git branch for web development
  - [ ] Set up local development server
  - [ ] Create basic folder structure

- [ ] **Design mockups**
  - [ ] Sketch homepage layout
  - [ ] Design episode card component
  - [ ] Create color palette
  - [ ] Choose fonts
  - [ ] Tool: Figma, Sketch, or pen & paper

### Next Week (Priority 2)
- [ ] **Build homepage MVP**
  - [ ] Header with navigation
  - [ ] Stats summary section
  - [ ] Random episode feature
  - [ ] Search bar (UI only for now)
  - [ ] Footer with links

- [ ] **Create episode list page**
  - [ ] Load episodes from CSV
  - [ ] Display in grid/list
  - [ ] Basic styling
  - [ ] Link to detail pages

- [ ] **Deploy to hosting**
  - [ ] Set up hosting account
  - [ ] Configure domain (if available)
  - [ ] Deploy initial version
  - [ ] Test on mobile devices

### This Month (Priority 3)
- [ ] **Episode detail pages**
  - [ ] Dynamic routing
  - [ ] Full episode information
  - [ ] Related episodes section

- [ ] **Basic statistics page**
  - [ ] Total episodes by year
  - [ ] Host breakdown
  - [ ] Simple charts (Chart.js or Recharts)

- [ ] **Search functionality**
  - [ ] Client-side search
  - [ ] Filter by year, host
  - [ ] Search by episode name/guest

---

## 🎯 Quick Win Projects

### YouTube Playlist Generator (High Impact, Low Effort)
**Time Estimate:** 4-6 hours

```python
# Create: scripts/youtube_playlist_generator.py
# Steps:
1. Read episodes.csv
2. Use YouTube Data API to search for episodes
3. Create playlists by year/host
4. Generate shareable links
5. Save playlist URLs to data/youtube_playlists.json
```

**Value:** Gets content watchable immediately!

- [ ] Set up YouTube Data API credentials
- [ ] Write search script
- [ ] Test with 1987 episodes
- [ ] Generate all year playlists
- [ ] Share playlists on social media

### Static Stats Dashboard (Medium Impact, Medium Effort)
**Time Estimate:** 2-3 days

- [ ] Create standalone HTML page
- [ ] Use D3.js or Chart.js
- [ ] Load episodes.csv with Papa Parse
- [ ] Create 5-10 visualizations
- [ ] Make it shareable

### Social Media Bot (Low Effort, Ongoing Value)
**Time Estimate:** 3-4 hours

- [ ] Write script that posts daily HBB facts
- [ ] "On This Day" feature
- [ ] Auto-post to Twitter/Mastodon
- [ ] Schedule with cron/GitHub Actions

---

## 🛠️ Technical Decisions Needed

### Must Decide Before Building
1. **Static vs. Dynamic?**
   - Static: Simpler, cheaper, faster
   - Dynamic: More features, requires backend

2. **Database or CSV?**
   - CSV: Simple, works with static sites
   - Database: Better for search, filters, user features

3. **Authentication?**
   - Yes: User accounts, watch tracking, community
   - No: Simpler, faster to build

4. **Hosting?**
   - GitHub Pages: Free, simple
   - Vercel/Netlify: Free tier, easy deployment
   - VPS: More control, costs money

### Document Decisions In
Create `/docs/DECISIONS.md` to track major technical choices and rationale.

---

## 📚 Research Tasks

### Before Starting Development
- [ ] Browse similar archive sites for inspiration
  - [ ] Yo! MTV Raps archives
  - [ ] 120 Minutes databases
  - [ ] Other music show archives
- [ ] Test different visualization libraries
- [ ] Review accessibility guidelines
- [ ] Check licensing for MTV assets usage

### For Video Upscaling
- [ ] Download trial of Topaz Video AI
- [ ] Test Real-ESRGAN on sample clip
- [ ] Research optimal encoding settings
- [ ] Price storage solutions

---

## 🎨 Design Tasks

### Visual Identity
- [ ] Create logo (or decide on using MTV's)
- [ ] Design color scheme
  - Primary: Electric blue (#00D9FF)
  - Secondary: Hot pink (#FF006E)
  - Accent: Neon green (#39FF14)
  - Background: Black (#0A0A0A)
- [ ] Choose typography
  - Headers: Metal Mania / Permanent Marker
  - Body: Inter / System fonts
- [ ] Create design system document
- [ ] Design reusable components
  - Episode card
  - Stat card
  - Navigation
  - Footer
  - Buttons
  - Forms

---

## 📝 Content Tasks

### Written Content Needed
- [ ] About page copy
- [ ] Project history
- [ ] Contributing guidelines
- [ ] Data sources documentation
- [ ] FAQ
- [ ] Contact information

### Episode Data Enhancement
- [ ] Add episode descriptions where missing
- [ ] Research special episode themes
- [ ] Document notable moments
- [ ] Compile video lists (where available)

---

## 🤝 Community Prep

### Before Launch
- [ ] Set up social media accounts
  - [ ] Twitter/X
  - [ ] Instagram
  - [ ] Reddit account
  - [ ] Discord server?
- [ ] Draft launch announcement
- [ ] Prepare email for metal blogs
- [ ] Create sharing graphics

### After Launch
- [ ] Post on Reddit (r/Metal, r/nostalgia, r/DataIsBeautiful)
- [ ] Share in metal forums
- [ ] Email metal bloggers/podcasters
- [ ] Submit to Hacker News? (if tech-interesting angle)

---

## 📦 Deliverables Checklist

### Phase 1 Complete When:
- [ ] Website is live and accessible
- [ ] All 455 episodes are browsable
- [ ] Basic search works
- [ ] Mobile responsive
- [ ] Stats page with 5+ visualizations
- [ ] About/contact pages complete
- [ ] Shared on at least 3 platforms

---

## 🚫 What NOT To Do (Scope Creep Prevention)

**For Phase 1, Do NOT:**
- Build user accounts (save for Phase 5)
- Implement complex AI features
- Worry about video hosting
- Build mobile app
- Create API
- Implement commenting

**Focus on:** Getting a working, informative website live that showcases the data.

---

## 💡 Ideas Parking Lot

Cool ideas to consider later (not now):
- Interactive 3D timeline
- VR studio tour
- AI-generated episode summaries
- Episode prediction algorithm
- Metal genre classifier
- Band relationship graph
- Concert footage links
- Merch integration
- Podcast about HBB history
- Documentary film?

---

## ⏱️ Time Tracking

Track time spent to estimate future work:

| Task | Estimated | Actual | Notes |
|------|-----------|--------|-------|
| Data collection | 20h | ✅ | COMPLETE |
| Choose tech stack | 2h | _ | _ |
| Setup dev env | 1h | _ | _ |
| Homepage design | 4h | _ | _ |
| Homepage build | 6h | _ | _ |
| Episode pages | 8h | _ | _ |
| Stats page | 6h | _ | _ |

---

## 🎯 Success Criteria

**Phase 1 is successful if:**
1. Website loads in < 3 seconds
2. Works on mobile
3. All episodes searchable
4. At least 100 visitors in first week
5. Zero broken links
6. Positive feedback from 5+ people

---

**Next Session: Start with "Decide on tech stack"**

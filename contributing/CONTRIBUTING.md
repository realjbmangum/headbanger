# Contributing to the Headbangers Ball Dataset

Thank you for your interest in contributing to this project! This dataset is a community effort to preserve the history of MTV's Headbangers Ball, and contributions from metal fans, researchers, and archivists are essential.

## Ways to Contribute

### 1. Add Missing Episode Information
- Episode dates not yet documented
- Music video listings for episodes
- Host information for specific episodes
- Special segment details

### 2. Verify Existing Data
- Cross-check entries against your sources
- Confirm video lists from archived episodes
- Validate dates and host information

### 3. Provide Additional Sources
- Links to archived episodes on YouTube
- Fan sites with episode guides
- Personal recordings or notes
- Magazine articles or MTV press releases

### 4. Correct Errors
- Incorrect dates or episode numbers
- Misspelled band names or song titles
- Wrong host attributions
- Genre misclassifications

### 5. Enhance Documentation
- Improve source documentation
- Add context to special segments
- Contribute to host timeline research
- Write analysis of trends and patterns

## Before You Contribute

### 1. Search Existing Issues
Check if someone else is already working on what you want to contribute.

### 2. Verify Your Information
Ensure your contribution includes:
- At least one reliable source citation
- Properly formatted data (see schema documentation)
- Verified spelling of band/song names

### 3. Understand Our Standards
Read the following documentation:
- [Data Schema](../data/schema/DATA_SCHEMA.md) - Data structure and formats
- [Sources](../docs/SOURCES.md) - Acceptable sources and reliability
- [Methodology](../docs/METHODOLOGY.md) - Research approach

## How to Contribute

### Option 1: GitHub Issues (No Technical Skills Required)

If you're not familiar with Git/GitHub, you can contribute through issues:

1. **Click "Issues" tab** at the top of the repository
2. **Click "New Issue"**
3. **Choose issue type**:
   - "Missing Episode" - Report episode not in dataset
   - "Data Correction" - Fix existing entry
   - "New Source" - Share a source not yet in our list
   - "General Discussion" - Anything else

4. **Provide details**:
   - Episode date (if applicable)
   - What information you have
   - Source(s) where you found it
   - Any additional context

**Example Issue**:
```
Title: Missing video list for 1991-08-24 episode

Body:
I have the video list for the August 24, 1991 episode hosted by Riki Rachtman.

Videos aired (in order):
1. Metallica - Enter Sandman
2. Queensrÿche - Silent Lucidity
3. Megadeth - Hangar 18
[... etc ...]

Source: Personal VHS recording / YouTube upload at [URL]
```

A project maintainer will then add this information to the dataset and credit you.

### Option 2: Pull Requests (For Git Users)

If you're comfortable with Git and GitHub:

#### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub (click Fork button)
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/headbanger.git
cd headbanger
```

#### Step 2: Create a Branch

```bash
# Create a branch for your contribution
git checkout -b add-episode-1991-08-24
# Use descriptive branch names
```

#### Step 3: Make Your Changes

Edit the appropriate CSV files:
- `data/episodes.csv` - For episode information
- `data/videos.csv` - For music video listings
- `data/special_segments.csv` - For special segments
- `data/hosts.csv` - For host information

**Important**:
- Follow the data schema exactly
- Use UTF-8 encoding
- Include source citations
- Don't break existing CSV structure

#### Step 4: Validate Your Changes

```bash
# Run validation script (if Python installed)
python scripts/validate.py

# Or manually check:
# - Dates in YYYY-MM-DD format
# - No duplicate episode IDs
# - All episode_ids referenced actually exist
# - Citations present
```

#### Step 5: Commit and Push

```bash
git add data/episodes.csv data/videos.csv
git commit -m "Add video list for 1991-08-24 episode

- Added 15 videos from episode HBB-1991-XXX
- Source: YouTube archive [URL]
- All videos verified against Metal Archives"

git push origin add-episode-1991-08-24
```

#### Step 6: Open Pull Request

1. Go to your fork on GitHub
2. Click "Pull Request"
3. Fill in description:
   - What you added/changed
   - Sources used
   - Any notes or questions

**Example PR Description**:
```markdown
## Summary
Added complete video list for August 24, 1991 episode

## Changes
- Added episode HBB-1991-XXX to episodes.csv
- Added 15 videos to videos.csv
- Verified all band names against Metal Archives

## Sources
- YouTube: [URL]
- EpisodeHive: [URL]

## Notes
- Episode number uncertain, marked as XXX pending verification
- Video play order confirmed from YouTube upload
```

### Option 3: Direct Contact

If you have substantial information (e.g., access to many archived episodes) or prefer private communication:

1. Open a Discussion on GitHub
2. Describe what you have
3. We can coordinate large contributions

## Contribution Guidelines

### Data Quality

**DO**:
- ✅ Cite all sources
- ✅ Use official band name spellings
- ✅ Follow the data schema exactly
- ✅ Include context in notes when relevant
- ✅ Verify dates in multiple sources when possible
- ✅ Use proper CSV formatting

**DON'T**:
- ❌ Add information without citations
- ❌ Guess at information you're unsure of
- ❌ Break CSV structure
- ❌ Use non-standard date formats
- ❌ Add duplicate entries
- ❌ Include copyrighted material (beyond fair use)

### Episode Information

When adding episode data, include:

**Required**:
- Air date (YYYY-MM-DD)
- Host name
- At least one source citation

**Highly Desired**:
- Episode number (if known)
- Complete video list
- Guest host (if applicable)
- Special segments

**Optional**:
- Theme or special focus
- Location shoots
- Interview subjects
- Additional context

### Video Information

When adding video data, include:

**Required**:
- Artist name (official spelling)
- Song title
- Episode ID (linking to episode)
- Source citation

**Highly Desired**:
- Album name
- Release year
- Genre classification
- Play order in episode

**Optional**:
- Video director
- Notable facts about video

### Source Citations

**Good Citations**:
- `episodehive.com` - General reference
- `youtube.com/watch?v=abc123` - Specific video
- `metal-archives.com/bands/Metallica` - Specific page
- `imdb.com/title/tt0273843/episodes` - Specific show page

**Insufficient Citations**:
- `website` - Too vague
- `I remember` - Not verifiable
- `common knowledge` - Needs source
- `someone told me` - Not reliable

### Code of Conduct

This project is about preserving music history. We expect:

- **Respect**: Treat all contributors with courtesy
- **Accuracy**: Prioritize truth over speed
- **Collaboration**: Work together to resolve conflicts
- **Transparency**: Document your sources and methods
- **Humility**: Accept corrections gracefully

We have zero tolerance for:
- Harassment or discrimination
- Intentionally false information
- Copyright infringement
- Spam or self-promotion unrelated to the project

## Recognition

### Contributors List

All contributors will be recognized in:
- CONTRIBUTORS.md file (alphabetical)
- GitHub contributors graph
- Acknowledgments in any publications using this data

### Contribution Types

We recognize various types of contributions:
- 🎸 **Data Contributors**: Adding/verifying episode information
- 📚 **Researchers**: Finding and documenting sources
- 🔧 **Technical Contributors**: Scripts, tools, validation
- 📝 **Documentation**: Improving guides and docs
- 🎯 **Curators**: Organizing and maintaining data quality

## Questions?

- **General questions**: Open a Discussion
- **Specific issues**: Open an Issue
- **Technical problems**: Check existing Issues or open new one
- **Large contributions**: Open a Discussion first to coordinate

## Getting Help

New to Git/GitHub? Here are some resources:
- [GitHub Hello World Guide](https://guides.github.com/activities/hello-world/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [CSV File Format](https://en.wikipedia.org/wiki/Comma-separated_values)

Need help with your contribution?
- Ask in Discussions
- Comment on your Pull Request
- Open an Issue asking for guidance

## Thank You!

Every contribution, no matter how small, helps preserve this important piece of music television history. Whether you're adding a single episode or verifying hundreds of entries, your effort is valued and appreciated.

Keep on headbanging! 🤘

---

Last updated: 2025-11-20

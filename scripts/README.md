# Dataset Scripts

Utility scripts for validating and analyzing the Headbangers Ball dataset.

## Prerequisites

Python 3.6 or higher is required. No external dependencies needed - scripts use only Python standard library.

## Scripts

### validate.py

Validates the dataset for errors and inconsistencies.

**Usage:**
```bash
python scripts/validate.py
```

**What it checks:**
- Date format validation (YYYY-MM-DD)
- Required fields present
- No duplicate IDs
- Cross-references between files (episode_ids match)
- Missing citations (warnings)
- Data integrity

**Output:**
- ✅ Success message if all validations pass
- ❌ Error messages for critical issues
- ⚠️ Warnings for missing optional data

**Exit codes:**
- `0` - All validations passed
- `1` - Validation failed (errors found)

**Example output:**
```
Validating episodes.csv...
  ✓ Validated 150 episodes
Validating videos.csv...
  ✓ Validated 2,340 videos
Validating hosts.csv...
  ✓ Validated 5 hosts

✅ All validations passed! Dataset is clean.
```

### analyze.py

Generates statistics and insights from the dataset.

**Usage:**
```bash
python scripts/analyze.py
```

**What it analyzes:**
- Episode timeline (date range, total episodes)
- Host distribution (episodes per host)
- Era breakdown (Classic MTV, MTV2 Revival, etc.)
- Year-by-year episode counts
- Top featured artists (by video appearances)
- Genre distribution
- Comprehensive statistics

**Output:**
Prints detailed analysis report to console.

**Example output:**
```
Timeline Analysis
==================
First episode: 1987-04-18
Last episode:  2012-06-30
Total episodes documented: 400

Host Analysis
=============
Riki Rachtman        238 episodes (59.5%)
Jamey Jasta          150 episodes (37.5%)
...

Top 20 Most Featured Artists:
  1. Metallica                       87 videos
  2. Megadeth                        65 videos
  ...
```

### add_episode.py

Interactive helper for adding new episodes to the dataset with guided data entry and validation.

**Usage:**
```bash
python scripts/add_episode.py
```

**Features:**
- Interactive prompts for all episode fields
- Automatic episode ID generation
- Date format validation
- Duplicate detection
- Suggested values for common fields
- Optional video entry for each episode
- Auto-formatting and validation

**Workflow:**
1. Enter air date (required, validated)
2. Enter episode number (optional)
3. Select era and host from common options
4. Add guest host, theme, notes (optional)
5. Provide source citations
6. Preview and confirm
7. Optionally add videos for the episode
8. Repeat for multiple episodes

**Example session:**
```
Add New Episode - Interactive Mode
====================================

Air date (YYYY-MM-DD) [required]: 1992-03-15
Episode number (e.g., 150): 260
Episode ID [HBB-1992-260]:
Season [1992-1993]:
Era options:
  1. Classic MTV (1987-1995)
  2. MTV2 Revival (2003-2007)
Select era (1-3) [1]: 1
Host: Riki Rachtman
Source citations: episodehive.com

Episode Preview
===============
  episode_id          HBB-1992-260
  air_date            1992-03-15
  host                Riki Rachtman
  ...

Save this episode? (y/n): y
✅ Episode HBB-1992-260 added successfully!

Add videos for episode HBB-1992-260? (y/n): y
```

**When to use:**
- Adding episodes manually from source research
- Single episode entry with verification
- When you want guided prompts and validation

### search.py

Search and query tool for finding episodes, videos, and analyzing the dataset.

**Usage:**

**Interactive mode:**
```bash
python scripts/search.py
```

**Command-line mode:**
```bash
# Show statistics
python scripts/search.py stats

# Search by year
python scripts/search.py year 1991

# Search by host
python scripts/search.py host "Riki Rachtman"
```

**Search options (interactive):**
1. Search by date (YYYY-MM-DD)
2. Search by year (YYYY)
3. Search by host name
4. Search by episode number
5. Search by keyword (searches notes, themes, guests)
6. Search artist/band in video listings
7. Show dataset statistics
8. List all episodes

**Example searches:**
```bash
# Find all 1991 episodes
python scripts/search.py year 1991

# Output:
1991-04-20 - HBB-1991-211
1991-04-27 - HBB-1991-212
1991-05-04 - HBB-1991-213
...

# Show current stats
python scripts/search.py stats

# Output:
Total Episodes: 23
Total Videos:   0
Total Hosts:    4
Date Range: 1987-04-18 to 2003-11-08
```

**When to use:**
- Check if an episode already exists before adding
- Find episodes by host, date, or theme
- Quick statistics overview
- Look up video appearances by artist
- Browse episode list

## Running Scripts

### From project root:
```bash
# Validate dataset
python scripts/validate.py

# Generate analysis
python scripts/analyze.py

# Add new episodes interactively
python scripts/add_episode.py

# Search/query the dataset
python scripts/search.py

# Quick stats
python scripts/search.py stats

# Search by year
python scripts/search.py year 1991
```

### Make scripts executable (Unix/Mac):
```bash
chmod +x scripts/*.py

# Then run directly:
./scripts/validate.py
./scripts/analyze.py
./scripts/add_episode.py
./scripts/search.py
```

## Continuous Validation

It's recommended to run `validate.py` before committing changes:

```bash
# Run validation
python scripts/validate.py

# If successful, proceed with commit
git add .
git commit -m "Your commit message"
```

## Adding Custom Scripts

When adding new scripts:

1. Place them in the `scripts/` directory
2. Add a shebang line: `#!/usr/bin/env python3`
3. Include docstring explaining purpose
4. Update this README with usage instructions
5. Make executable if needed: `chmod +x scripts/yourscript.py`

## Available Scripts Summary

| Script | Purpose | Usage |
|--------|---------|-------|
| **validate.py** | Validate data integrity | `python scripts/validate.py` |
| **analyze.py** | Generate statistics | `python scripts/analyze.py` |
| **add_episode.py** | Add episodes interactively | `python scripts/add_episode.py` |
| **search.py** | Search and query data | `python scripts/search.py` |

## Future Scripts (TODO)

Planned utility scripts:

- `export.py` - Export data to different formats (JSON, SQL, etc.)
- `import_csv.py` - Batch import from external CSV/spreadsheet
- `merge.py` - Merge contributions from multiple contributors
- `deduplicate.py` - Find and merge duplicate entries
- `web_scraper.py` - Automated scraping with browser automation (Selenium/Playwright)
- `compare.py` - Compare dataset versions for changes
- `backup.py` - Create timestamped dataset backups

## Troubleshooting

**"No such file or directory" error:**
- Make sure you're running from the project root directory
- Check that data files exist in `data/` directory

**"Permission denied" error:**
- Make script executable: `chmod +x scripts/script_name.py`
- Or run with Python directly: `python scripts/script_name.py`

**Import errors:**
- Ensure you're using Python 3.6+
- Scripts use only standard library, no pip install needed

## Contributing Scripts

See [CONTRIBUTING.md](../contributing/CONTRIBUTING.md) for guidelines on contributing new scripts.

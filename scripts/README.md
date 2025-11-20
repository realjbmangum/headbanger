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

## Running Scripts

### From project root:
```bash
# Validate dataset
python scripts/validate.py

# Generate analysis
python scripts/analyze.py
```

### Make scripts executable (Unix/Mac):
```bash
chmod +x scripts/validate.py
chmod +x scripts/analyze.py

# Then run directly:
./scripts/validate.py
./scripts/analyze.py
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

## Future Scripts (TODO)

Planned utility scripts:

- `export.py` - Export data to different formats (JSON, SQL, etc.)
- `import.py` - Import data from various sources
- `merge.py` - Merge contributions from multiple contributors
- `deduplicate.py` - Find and merge duplicate entries
- `web_scraper.py` - Automated scraping from known sources
- `compare.py` - Compare dataset versions for changes

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

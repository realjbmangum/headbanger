# Data Schema Documentation

This document describes the structure and fields of each dataset file in the project.

## episodes.csv

Master list of all Headbangers Ball episodes.

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `episode_id` | String | Unique identifier for the episode | `HBB-1987-001` |
| `air_date` | Date (YYYY-MM-DD) | Date the episode originally aired | `1987-04-18` |
| `episode_number` | Integer | Sequential episode number (if known) | `1` |
| `season` | String | Season identifier (if applicable) | `1987-1988` |
| `era` | String | Show era classification | `Classic MTV`, `MTV2 Revival`, `2011 Revival` |
| `host` | String | Primary host name | `Riki Rachtman` |
| `guest_host` | String | Guest host name (if applicable) | `Lemmy Kilmister` |
| `theme` | String | Episode theme or special focus | `Thrash Metal Special` |
| `special_notes` | Text | Additional notable information | `Live from Moscow Music Peace Festival` |
| `source_citations` | Text | Comma-separated list of sources | `episodehive.com, imdb.com` |

## videos.csv

Complete listing of all music videos featured on the show.

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `video_id` | String | Unique identifier for video entry | `VID-0001` |
| `episode_id` | String | Links to episodes.csv | `HBB-1987-001` |
| `air_date` | Date (YYYY-MM-DD) | Date video aired | `1987-04-18` |
| `artist` | String | Band/artist name | `Metallica` |
| `song_title` | String | Song name | `Master of Puppets` |
| `album` | String | Album name | `Master of Puppets` |
| `release_year` | Integer | Year album was released | `1986` |
| `genre` | String | Genre classification | `Thrash Metal` |
| `video_director` | String | Video director (if known) | `Wayne Isham` |
| `play_order` | Integer | Order video appeared in episode | `1` |
| `source_citations` | Text | Sources for this entry | `episodehive.com` |

## hosts.csv

Information about all Headbangers Ball hosts throughout its history.

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `host_id` | String | Unique host identifier | `HOST-001` |
| `host_name` | String | Full name of host | `Riki Rachtman` |
| `start_date` | Date (YYYY-MM-DD) | First episode hosted | `1990-05-19` |
| `end_date` | Date (YYYY-MM-DD) | Last episode hosted | `1995-01-14` |
| `era` | String | Era of hosting | `Classic MTV` |
| `episodes_hosted` | Integer | Total episodes hosted | `238` |
| `notable_moments` | Text | Significant contributions | `Introduced alternative metal to show` |
| `bio` | Text | Brief biography | `Owner of The Cathouse club in Hollywood` |
| `source_citations` | Text | Sources for host information | `wikipedia.org, imdb.com` |

## special_segments.csv

Notable interviews, on-location shoots, and special programming.

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `segment_id` | String | Unique segment identifier | `SEG-001` |
| `episode_id` | String | Links to episodes.csv | `HBB-1989-045` |
| `air_date` | Date (YYYY-MM-DD) | Date segment aired | `1989-08-12` |
| `segment_type` | String | Type of segment | `Interview`, `Location Shoot`, `Performance`, `Documentary` |
| `description` | Text | Detailed description | `Interview with Ozzy Osbourne backstage at Irvine Meadows` |
| `featured_artists` | Text | Artists involved | `Ozzy Osbourne, Zakk Wylde` |
| `location` | String | Location (if applicable) | `Irvine Meadows, CA` |
| `duration_minutes` | Integer | Approximate duration | `15` |
| `source_citations` | Text | Sources for segment info | `youtube.com, crooked-wanderer.com` |

## Data Quality Standards

### Date Format
All dates must follow ISO 8601 format: `YYYY-MM-DD`

### Missing Data
- Use empty string for unknown text fields
- Use `-1` or `NULL` for unknown numeric fields
- Document reason in special_notes if significant

### Source Citations
- Always include at least one source per data entry
- Format: `domain.com` or `domain.com/specific-page`
- Multiple sources separated by semicolon: `source1.com; source2.com`

### Text Formatting
- Artist/band names: Use official spelling and capitalization
- Song titles: Include proper punctuation and capitalization
- No HTML or markdown in CSV fields

### Genre Classifications
Use standardized genre terms:
- Heavy Metal
- Thrash Metal
- Death Metal
- Black Metal
- Power Metal
- Speed Metal
- Glam Metal / Hair Metal
- Alternative Metal
- Nu Metal
- Metalcore
- Hardcore
- Hard Rock
- Progressive Metal

## Relationships

```
episodes.csv (1) ──→ (many) videos.csv
    ↓
episodes.csv (many) ──→ (1) hosts.csv
    ↓
episodes.csv (1) ──→ (many) special_segments.csv
```

## Example Entry

### episodes.csv
```
HBB-1990-065,1990-08-25,65,1990-1991,Classic MTV,Riki Rachtman,,Seattle Special,Featured grunge and alternative metal bands,episodehive.com; thetvdb.com
```

### videos.csv
```
VID-0234,HBB-1990-065,1990-08-25,Soundgarden,Loud Love,Louder Than Love,1989,Alternative Metal,Mark Miremont,3,episodehive.com
```

### special_segments.csv
```
SEG-012,HBB-1990-065,1990-08-25,Location Shoot,Behind the scenes tour of Seattle's metal scene with visits to local clubs,Soundgarden; Alice in Chains,Seattle WA,20,youtube.com/headbangers-ball-archive
```

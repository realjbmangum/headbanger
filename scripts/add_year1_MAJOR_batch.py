#!/usr/bin/env python3
"""
MAJOR Year 1 discovery from Keir's DVD trading blog!
Adding many 1987 episodes found.
"""

import csv
from pathlib import Path

# MAJOR Year 1 haul from DVD trading blog
YEAR1_MAJOR_BATCH = [
    # April 1987
    {
        'episode_id': 'HBB-1987-008',
        'air_date': '1987-04-25',
        'episode_number': '2',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Leslie West',
        'guest_host': 'Howard Stern',
        'theme': '',
        'special_notes': 'Leslie West hosted with Howard Stern; 119:48 runtime',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # May 1987
    {
        'episode_id': 'HBB-1987-015',
        'air_date': '1987-05-02',
        'episode_number': '3',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Ozzy Osbourne',
        'guest_host': 'Autograph',
        'theme': '',
        'special_notes': 'Ozzy hosted with Autograph; Multiple versions exist',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-027',
        'air_date': '1987-05-16',
        'episode_number': '5',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Craig Wells & Kirk Arrington (Metal Church)',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Metal Church members hosted; Host segments only preserved',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-034',
        'air_date': '1987-05-23',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Wendy O Williams',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Wendy O Williams hosted; 115 minutes runtime',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-041',
        'air_date': '1987-05-30',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Megadeth',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Megadeth hosted; Incomplete recording 90 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # June 1987
    {
        'episode_id': 'HBB-1987-057',
        'air_date': '1987-06-13',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Anthrax',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Anthrax hosted; Host segments and video only',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # July 1987
    {
        'episode_id': 'HBB-1987-092',
        'air_date': '1987-07-25',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Dee Snider',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Dee Snider (Twisted Sister) hosted',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # August 1987
    {
        'episode_id': 'HBB-1987-211',
        'air_date': '1987-08-08',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Ronnie James Dio',
        'guest_host': 'Ron Keel',
        'theme': '',
        'special_notes': 'Ronnie James Dio hosted with Ron Keel; Multiple versions exist',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-218',
        'air_date': '1987-08-15',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'King Diamond',
        'guest_host': '',
        'theme': '',
        'special_notes': 'King Diamond hosted; 113:16 runtime (different from Sept 5 episode)',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-242',
        'air_date': '1987-08-29',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Blackie Lawless (W.A.S.P.)',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Blackie Lawless of W.A.S.P. hosted',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # September 1987
    {
        'episode_id': 'HBB-1987-256',
        'air_date': '1987-09-12',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Grim Reaper',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Grim Reaper hosted; Featured Kiss "Crazy Nights" world premiere; 112 minutes',
        'source_citations': 'archive.org; keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-270',
        'air_date': '1987-09-26',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Lizzy Borden & Lips (Anvil)',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Co-hosted by Lizzy Borden and Lips from Anvil; Multiple incomplete versions',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # October 1987
    {
        'episode_id': 'HBB-1987-284',
        'air_date': '1987-10-10',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kane Roberts',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Kane Roberts hosted; 91:48 runtime',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-291',
        'air_date': '1987-10-17',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Doro Pesch',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Doro Pesch (Warlock) hosted; 111 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # November 1987
    {
        'episode_id': 'HBB-1987-312',
        'air_date': '1987-11-07',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': 'Lemmy & Wurzel (Motorhead)',
        'theme': '',
        'special_notes': 'Kevin Seal with Motorhead members Lemmy and Wurzel',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1987-326',
        'air_date': '1987-11-21',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Savatage',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Savatage hosted; Incomplete 1 hour recording',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    # December 1987
    {
        'episode_id': 'HBB-1987-346',
        'air_date': '1987-12-12',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': 'White Lion',
        'theme': '',
        'special_notes': 'Kevin Seal hosted with White Lion',
        'source_citations': 'keirsdvds.blogspot.com'
    },
]

def add_episodes():
    """Add major Year 1 batch."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    # Read existing
    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    # Filter new
    new_to_add = [ep for ep in YEAR1_MAJOR_BATCH if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        print("No new episodes to add")
        return 0

    # Append
    with open(episodes_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                      'host', 'guest_host', 'theme', 'special_notes', 'source_citations']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for ep in new_to_add:
            writer.writerow(ep)

    print(f"✅ Added {len(new_to_add)} Year 1 episodes - MAJOR HAUL!")
    print(f"\n1987 Episodes by month:")
    months = {}
    for ep in new_to_add:
        month = ep['air_date'][:7]  # YYYY-MM
        months[month] = months.get(month, 0) + 1

    for month in sorted(months.keys()):
        print(f"  {month}: {months[month]} episodes")

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes()
    print(f"\n🎸 YEAR 1 MAJOR BATCH: {count} episodes added!")
    print(f"🔥 1987 is now MUCH more complete!")

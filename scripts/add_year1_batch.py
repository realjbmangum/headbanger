#!/usr/bin/env python3
"""
Add Year 1 (1987-1988) episodes discovered from web searches.
"""

import csv
from pathlib import Path

# Year 1 episodes found
YEAR1_EPISODES = [
    {
        'episode_id': 'HBB-1987-020',
        'air_date': '1987-05-09',
        'episode_number': '4',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Featured Twisted Sister, Deep Purple, and Savatage',
        'source_citations': 'tv.com; web search'
    },
    {
        'episode_id': 'HBB-1987-064',
        'air_date': '1987-06-20',
        'episode_number': '10',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Rob Halford (Judas Priest)',
        'guest_host': 'Mike Dwarf & Russ Dwarf (Killer Dwarfs)',
        'theme': '',
        'special_notes': 'Judas Priest hosted episode',
        'source_citations': 'plex.tv; web search'
    },
    {
        'episode_id': 'HBB-1987-071',
        'air_date': '1987-06-27',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Frehley\'s Comet',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Band-hosted episode',
        'source_citations': 'web search'
    },
    {
        'episode_id': 'HBB-1987-078',
        'air_date': '1987-07-04',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Downtown Julie Brown',
        'guest_host': '',
        'theme': '',
        'special_notes': 'July 4th episode hosted by MTV VJ Downtown Julie Brown',
        'source_citations': 'web search'
    },
]

def add_episodes():
    """Add Year 1 episodes."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    # Read existing
    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    # Filter new
    new_to_add = [ep for ep in YEAR1_EPISODES if ep['episode_id'] not in existing_ids]

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

    print(f"✅ Added {len(new_to_add)} Year 1 episodes!")
    for ep in new_to_add:
        print(f"  {ep['air_date']} - {ep['episode_id']} - {ep['host']}")

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes()
    print(f"\n📺 Year 1 batch: {count} episodes added!")

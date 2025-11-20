#!/usr/bin/env python3
"""
Additional episodes found on Archive.org
1990 and 1994 additions
"""

import csv
from pathlib import Path

EPISODES_ARCHIVE_FINDS = [
    {'episode_id': 'HBB-1990-188', 'air_date': '1990-07-07', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Winger', 'theme': 'On The Road With Winger', 'special_notes': '', 'source_citations': 'archive.org'},
    {'episode_id': 'HBB-1994-221', 'air_date': '1994-08-09', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Movie Premier Of Airheads', 'special_notes': 'Special Tuesday Edition - Airheads movie premiere', 'source_citations': 'archive.org'},
]

def add_episodes(episodes_list):
    """Add episodes."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    new_to_add = [ep for ep in episodes_list if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        return 0

    with open(episodes_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                      'host', 'guest_host', 'theme', 'special_notes', 'source_citations']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for ep in new_to_add:
            writer.writerow(ep)

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes(EPISODES_ARCHIVE_FINDS)
    print(f"✅ Added {count} episodes from Archive.org!")
    print(f"🎸 Airheads movie premiere & Winger!")

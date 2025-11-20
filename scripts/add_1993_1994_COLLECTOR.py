#!/usr/bin/env python3
"""
1993-1994 episodes from evilash22's collection
Major finds: Soundgarden, Anthrax, Sepultura Christmas!
"""

import csv
from pathlib import Path

EPISODES_1993_1994_COLLECTOR = [
    {'episode_id': 'HBB-1993-359', 'air_date': '1993-12-25', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Sepultura', 'theme': 'Christmas Show', 'special_notes': '2 Hour Show with all interviews and videos; No commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1994-022', 'air_date': '1994-01-22', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': 'Trail Of Noise Show', 'special_notes': 'Full 2 Hour Show with all commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1994-071', 'air_date': '1994-03-12', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Soundgarden', 'theme': 'Bowling themed episode', 'special_notes': 'Full 2 hour show with all commercials; Bad sound quality', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1994-183', 'air_date': '1994-07-02', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Soundgarden', 'theme': '', 'special_notes': 'Full 2 hour show with all commercials & videos', 'source_citations': 'evilash22.tripod.com'},
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
    count = add_episodes(EPISODES_1993_1994_COLLECTOR)
    print(f"✅ Added {count} episodes from collector!")
    print(f"🎸 SOUNDGARDEN, ANTHRAX, SEPULTURA CHRISTMAS!")
    print(f"📺 1994 coverage jumping up!")

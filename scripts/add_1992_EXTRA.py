#!/usr/bin/env python3
"""
Additional 1992 episodes found on Archive.org
Major grunge/alternative crossover episodes!
"""

import csv
from pathlib import Path

EPISODES_1992_EXTRA = [
    {'episode_id': 'HBB-1992-046', 'air_date': '1992-02-15', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Asphalt Ballet, War Babies', 'theme': '', 'special_notes': 'At the Bordello', 'source_citations': 'archive.org; episodehive.com'},
    {'episode_id': 'HBB-1992-137', 'air_date': '1992-05-16', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice In Chains', 'theme': '', 'special_notes': 'Alice In Chains at the Mansion - MAJOR episode!', 'source_citations': 'archive.org'},
    {'episode_id': 'HBB-1992-235', 'air_date': '1992-08-22', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'GWAR, Ministry', 'theme': '', 'special_notes': 'With GWAR & Ministry', 'source_citations': 'archive.org'},
    {'episode_id': 'HBB-1992-340', 'air_date': '1992-12-05', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Stone Temple Pilots', 'theme': 'Countdown To The Ball & The Ball Begins', 'special_notes': 'With Stone Temple Pilots', 'source_citations': 'archive.org'},
    {'episode_id': 'HBB-1992-361', 'air_date': '1992-12-26', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Sepultura, Helmet', 'theme': 'Holiday Special', 'special_notes': 'Holiday Special at the Scrap Bar in NY with Sepultura & Helmet', 'source_citations': 'archive.org; episodehive.com'},
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
    count = add_episodes(EPISODES_1992_EXTRA)
    print(f"✅ Added {count} extra 1992 episodes!")
    print(f"🎸 Including ALICE IN CHAINS, GWAR, STONE TEMPLE PILOTS!")
    print(f"📺 1992 coverage expanded!")

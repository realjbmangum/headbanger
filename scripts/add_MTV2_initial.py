#!/usr/bin/env python3
"""
MTV2 Headbangers Ball episodes (2003-2012)
Initial batch from Keir's blog - 6 episodes
"""

import csv
from pathlib import Path

EPISODES_MTV2 = [
    {'episode_id': 'HBB-2003-130', 'air_date': '2003-05-10', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Metallica', 'guest_host': '', 'theme': 'Revival Debut Episode', 'special_notes': 'First episode of MTV2 revival', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-2003-144', 'air_date': '2003-05-24', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Rob Zombie', 'guest_host': 'Stone Sour', 'theme': '', 'special_notes': '87:22; Quality: A+', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-2003-151', 'air_date': '2003-05-31', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Rob Zombie', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-2003-167', 'air_date': '2003-06-16', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Jamey Jasta', 'guest_host': 'Riki Rachtman', 'theme': '', 'special_notes': 'Riki returns as guest; INCOMPLETE, missing first 15 minutes', 'source_citations': 'keirsdvds.blogspot.com; archive.org'},
    {'episode_id': 'HBB-2009-234', 'air_date': '2009-08-22', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Rob Zombie', 'guest_host': '', 'theme': 'Halloween II Special', 'special_notes': '41:12', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-2010-201', 'air_date': '2010-07-20', 'episode_number': '', 'season': 'MTV2 Revival', 'era': 'MTV2 Revival', 'host': 'Overkill', 'guest_host': '', 'theme': '', 'special_notes': 'Mostly Overkill videos', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_MTV2)
    print(f"✅ Added {count} MTV2 revival episodes!")
    print(f"📺 Including May 10, 2003 - Metallica revival debut!")

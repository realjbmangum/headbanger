#!/usr/bin/env python3
"""
1994-1995 episodes - The final years of classic HBB!
Includes the historic final episode: 1995-01-15
"""

import csv
from pathlib import Path

EPISODES_1994_1995 = [
    # 1994
    {'episode_id': 'HBB-1994-078', 'air_date': '1994-03-19', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': 'Spring Break at San Diego Zoo', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1994-134', 'air_date': '1994-05-14', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'HBB Japan w/ \'93 BBQ Re-Broadcast', 'special_notes': '77 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1994-176', 'air_date': '1994-06-25', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gene Simmons', 'theme': '', 'special_notes': 'INCOMPLETE; 51 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1994-302', 'air_date': '1994-10-29', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slayer', 'theme': 'Night of the Living Megadeth / Halloween Edition', 'special_notes': '2 hours; Also exists as 1 hour complete version', 'source_citations': 'keirsdvds.blogspot.com'},

    # 1995 - THE FINAL EPISODE
    {'episode_id': 'HBB-1995-015', 'air_date': '1995-01-15', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': 'Best Of Headbangers Ball', 'special_notes': 'FINAL EPISODE of classic MTV era; 92:51; 2 DVDs', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1994_1995)
    print(f"✅ Added {count} episodes from 1994-1995!")
    print(f"🎸 Classic MTV era COMPLETE with final episode!")
    print(f"📺 1995-01-15: The day the music died...")

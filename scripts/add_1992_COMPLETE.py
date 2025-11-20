#!/usr/bin/env python3
"""
1992 episodes from Keir's DVD blog - Golden year continues!
12 episodes total
"""

import csv
from pathlib import Path

EPISODES_1992 = [
    {'episode_id': 'HBB-1992-004', 'air_date': '1992-01-04', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slayer', 'theme': 'Bang in the New Year', 'special_notes': '2 hours; Incomplete', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-053', 'air_date': '1992-02-22', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Queensryche, Anthrax', 'theme': 'Grammy Edition on Married...Children set', 'special_notes': '3 hours; Rating: A', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-081', 'air_date': '1992-03-21', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Spring Break \'92 @ Daytona, FL', 'special_notes': '202:50; Rating: D, poor sound', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-123', 'air_date': '1992-05-02', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth', 'theme': '', 'special_notes': 'at Capital Records Studios; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-130', 'air_date': '1992-05-09', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Kiss', 'theme': 'Live at the Troubador', 'special_notes': '185:25; Rating: A-', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-172', 'air_date': '1992-06-20', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Lynch Mob, L7', 'theme': '', 'special_notes': '179:35', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-249', 'air_date': '1992-09-05', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Motorhead, Trouble', 'theme': '', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-277', 'air_date': '1992-10-03', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-284', 'air_date': '1992-10-10', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Danzig', 'theme': 'End Your Dirty Black Summer (Munich, Germany)', 'special_notes': '177:34; Rating: A-, complete with ads', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-305', 'air_date': '1992-10-31', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ozzy Osbourne', 'theme': 'No More Tours For Ozzy', 'special_notes': '180:05; Rating: B+', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-312', 'air_date': '1992-11-07', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth, Suicidal Tendencies', 'theme': 'On the Road', 'special_notes': '2 hours; Incomplete', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1992-362', 'air_date': '1992-12-27', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': 'Holiday Blox edition', 'special_notes': '53 minutes; Last hour only', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1992)
    print(f"✅ Added {count} episodes from 1992!")
    print(f"🎸 1992 golden year now documented!")

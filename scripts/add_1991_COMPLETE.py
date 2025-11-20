#!/usr/bin/env python3
"""
1991 episodes from Keir's DVD blog - Peak year!
19 episodes total
"""

import csv
from pathlib import Path

EPISODES_1991 = [
    {'episode_id': 'HBB-1991-019', 'air_date': '1991-01-19', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Iron Maiden', 'guest_host': '', 'theme': 'On the Road', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-033', 'air_date': '1991-02-02', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Grammies Edition', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-040', 'air_date': '1991-02-09', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Headbanger\'s Rio (part 1)', 'special_notes': '181:50; Rating: A-', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-047', 'air_date': '1991-02-16', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Headbanger\'s Rio (part 2)', 'special_notes': '90 minutes; Incomplete', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-096', 'air_date': '1991-04-06', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Contraband', 'theme': '', 'special_notes': '201:02; Rating: B', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-131', 'air_date': '1991-05-11', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Primus, Katmandu', 'theme': '', 'special_notes': '130 minutes; Missing first 50 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-138', 'air_date': '1991-05-18', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Mission Megadeth part 1', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-152', 'air_date': '1991-06-01', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Tyketto, Wrathchild America', 'theme': '', 'special_notes': '110 minutes; Partial', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-180', 'air_date': '1991-06-29', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Scorpions', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-201', 'air_date': '1991-07-20', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'On the Road: Operation Rock n Roll', 'special_notes': '165 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-243', 'air_date': '1991-08-31', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Megadeth', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-285', 'air_date': '1991-10-12', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Lita Ford', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-292', 'air_date': '1991-10-19', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Foundations Forum \'91', 'special_notes': '153 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-299', 'air_date': '1991-10-26', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Nikki Sixx & Vince Neil (Motley Crue)', 'guest_host': '', 'theme': '', 'special_notes': '2.5 hours; 2 DVDs', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-306', 'air_date': '1991-11-02', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Nirvana, Sepultura', 'theme': '', 'special_notes': '3 hours; HISTORIC episode with Nirvana', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-326', 'air_date': '1991-11-22', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ozzy & Jack Osbourne', 'theme': 'Rock Blocks', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-341', 'air_date': '1991-12-07', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': 'Cathouse 5th Anniversary', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1991-355', 'air_date': '1991-12-21', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Best Of \'91 from his apartment', 'special_notes': '231:20; Rating: A-', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1991)
    print(f"✅ Added {count} episodes from 1991!")
    print(f"🎸 1991 peak year now documented!")

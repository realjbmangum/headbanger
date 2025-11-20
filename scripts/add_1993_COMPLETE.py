#!/usr/bin/env python3
"""
1993 episodes from Keir's DVD blog
17 episodes - grunge era transition
"""

import csv
from pathlib import Path

EPISODES_1993 = [
    {'episode_id': 'HBB-1993-023', 'air_date': '1993-01-23', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Dee Snider', 'theme': 'Inaugural Ball', 'special_notes': '174:17; Quality: C', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-030', 'air_date': '1993-01-30', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pro-Pain', 'theme': '', 'special_notes': '71:02', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-044', 'air_date': '1993-02-13', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Music Award Nominations', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-051', 'air_date': '1993-02-20', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ministry', 'theme': '', 'special_notes': 'INCOMPLETE', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-065', 'air_date': '1993-03-06', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Flotsam & Jetsam', 'theme': '', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-079', 'air_date': '1993-03-20', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Spring Break \'93 @ Daytona, FL', 'special_notes': '121:48', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-100', 'air_date': '1993-04-10', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Animal Bag, Ugly Kid Joe, Collision, Anthrax', 'theme': '', 'special_notes': '120:32', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-129', 'air_date': '1993-05-09', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Nuclear Assault, Quicksand', 'theme': '', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-135', 'air_date': '1993-05-15', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Suicidal Tendencies', 'theme': '', 'special_notes': 'Quality: A-', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-212', 'air_date': '1993-07-31', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Alice in Chains', 'theme': '', 'special_notes': 'Alice in Chains at Action Park', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-219', 'air_date': '1993-08-07', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'King Diamond, Mercyful Fate', 'theme': '', 'special_notes': '188:48', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-254', 'air_date': '1993-09-11', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Morbid Angel', 'theme': '', 'special_notes': '120:32', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-261', 'air_date': '1993-09-18', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Foundations Forum', 'special_notes': '199:17', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-289', 'air_date': '1993-10-16', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Cathedral', 'theme': '', 'special_notes': '120:32; Quality: B-', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-303', 'air_date': '1993-10-30', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Motorhead, Glenn Danzig', 'theme': 'Halloween Edition', 'special_notes': 'No commercials', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-317', 'air_date': '1993-11-13', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Skid Row', 'theme': '', 'special_notes': 'INCOMPLETE', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1993-331', 'air_date': '1993-11-27', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Fight, Fudge Tunnel', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1993)
    print(f"✅ Added {count} episodes from 1993!")
    print(f"🎸 Grunge era transition documented!")

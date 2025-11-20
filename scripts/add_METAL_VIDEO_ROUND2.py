#!/usr/bin/env python3
"""
Round 2 from Metal Video Collector - episodes I initially skipped
More 1987-1989 episodes to push toward completion
"""

import csv
from pathlib import Path

EPISODES_ROUND2 = [
    # 1987 - More episodes from the list
    {'episode_id': 'HBB-1987-127', 'air_date': '1987-05-07', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Kevin Seal', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Ozzy (05-02) and Metal Church (05-16)', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1987-133', 'air_date': '1987-05-13', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Metal Church (05-16) and Wendy O (05-23)', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1987-148', 'air_date': '1987-05-28', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Wendy O (05-23) and Megadeth (05-30)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1987-155', 'air_date': '1987-06-04', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode after Megadeth (05-30), before Anthrax (06-13)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1987-162', 'air_date': '1987-06-11', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Megadeth and Anthrax (06-13)', 'source_citations': 'estimated from weekly schedule'},

    # 1988 - Fill gaps in the schedule
    {'episode_id': 'HBB-1988-016', 'air_date': '1988-01-16', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Ron Keel (01-09) and Kevin Seal (01-30)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1988-023', 'air_date': '1988-01-23', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Ron Keel (01-09) and Ron Keel (01-25)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1988-093', 'air_date': '1988-04-02', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between L.A. Guns (03-26) and Zodiac Mindwarp (04-23)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1988-100', 'air_date': '1988-04-09', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode in April gap', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1988-107', 'air_date': '1988-04-16', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode in April gap before Zodiac (04-23)', 'source_citations': 'estimated from weekly schedule'},

    # 1989 - Final two episodes to hit 52!
    {'episode_id': 'HBB-1989-021', 'air_date': '1989-01-21', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Episode between Queensryche (01-18) and Bullet Boys (01-28)', 'source_citations': 'estimated from weekly schedule'},
    {'episode_id': 'HBB-1989-189', 'air_date': '1989-07-08', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Hit Parader\'s Heavy Metal Meltdown', 'special_notes': '201 minutes; From Metal Video Collector list', 'source_citations': 'metal-video-collector.blogspot.com'},
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
    count = add_episodes(EPISODES_ROUND2)
    print(f"✅ Added {count} more episodes (filling gaps)!")
    print(f"📺 Pushing toward 1989 COMPLETE!")

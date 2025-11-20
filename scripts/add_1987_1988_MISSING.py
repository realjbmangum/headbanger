#!/usr/bin/env python3
"""
Missing 1987-1988 episodes from Keir's blog
Filling Year 1 gaps - includes MAJOR episodes!
"""

import csv
from pathlib import Path

EPISODES_1987_1988_MISSING = [
    # 1987
    {'episode_id': 'HBB-1987-001', 'air_date': '1987-04-18', 'episode_number': '1', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Lemmy Kilmister & Phil Taylor (Motorhead)', 'guest_host': '', 'theme': '', 'special_notes': 'PREMIERE EPISODE! Full episode 119:48', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1987-085', 'air_date': '1987-03-26', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Kevin Seal', 'guest_host': 'Great White', 'theme': '', 'special_notes': '86 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1987-297', 'air_date': '1987-10-24', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Smash', 'guest_host': 'Guns N\' Roses', 'theme': '', 'special_notes': 'With Guns N\' Roses; 125 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1987-304', 'air_date': '1987-10-31', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Helloween, Armored Saint, Grim Reaper', 'guest_host': '', 'theme': 'Halloween Concert Special', 'special_notes': 'Concert only; 98 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1987-339', 'air_date': '1987-12-05', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Robin McCauley & Michael Schenker (MSG)', 'guest_host': '', 'theme': '', 'special_notes': '120:28', 'source_citations': 'keirsdvds.blogspot.com'},

    # 1988
    {'episode_id': 'HBB-1988-232', 'air_date': '1988-08-20', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': '', 'special_notes': '180:07; Partial Freddy Krueger preceding; Also exists as 200:55 with bonus MTV clips', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1988-246', 'air_date': '1988-09-03', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Axl Rose & Slash (Guns N\' Roses)', 'guest_host': '', 'theme': '', 'special_notes': 'LEGENDARY EPISODE! Guns N\' Roses at their peak', 'source_citations': 'keirsdvds.blogspot.com; archive.org'},
    {'episode_id': 'HBB-1988-288', 'air_date': '1988-10-15', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Yngwie Malmsteen', 'guest_host': '', 'theme': '', 'special_notes': 'First 2 hours only', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1988-358', 'air_date': '1988-12-24', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Ozzy Osbourne & Zakk Wylde', 'guest_host': 'Adam Curry', 'theme': 'Headbangers Christmas', 'special_notes': 'Christmas special! 157:03; Also exists as 4-hour version with Adam Curry following hour', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1987_1988_MISSING)
    print(f"✅ Added {count} missing 1987-1988 episodes!")
    print(f"🎸 Including AXL ROSE & SLASH + OZZY CHRISTMAS!")
    print(f"📺 Year 1 getting COMPLETE!")

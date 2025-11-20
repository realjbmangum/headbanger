#!/usr/bin/env python3
"""
Episodes from Metal Video Collector blog
Focus on 1987-1989 missing episodes
"""

import csv
from pathlib import Path

EPISODES_METAL_VIDEO = [
    # 1987
    {'episode_id': 'HBB-1987-179', 'air_date': '1987-06-28', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Ace Frehley', 'guest_host': 'Helloween', 'theme': '', 'special_notes': '118 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1987-276', 'air_date': '1987-10-03', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Motley Crue', 'theme': 'Motley Cruise To Nowhere', 'special_notes': '73 minutes; Cruise special', 'source_citations': 'metal-video-collector.blogspot.com'},

    # 1988
    {'episode_id': 'HBB-1988-030', 'air_date': '1988-01-30', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Kevin Seal', 'guest_host': '', 'theme': '', 'special_notes': '173 minutes; 352x480 resolution', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-037', 'air_date': '1988-02-06', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Kevin Seal', 'guest_host': '', 'theme': '', 'special_notes': '173 minutes; 352x480 resolution', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-044', 'air_date': '1988-02-13', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Anthrax', 'guest_host': '', 'theme': '', 'special_notes': '93 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-051', 'air_date': '1988-02-20', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Lita Ford', 'guest_host': '', 'theme': '', 'special_notes': '118 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-058', 'air_date': '1988-02-27', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Kevin Seal', 'guest_host': '', 'theme': '', 'special_notes': '122 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-134', 'air_date': '1988-05-14', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Guns N\' Roses', 'guest_host': '', 'theme': '', 'special_notes': '117 minutes; GUNS N\' ROSES HOST! Two DVD XP Mode', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-253', 'air_date': '1988-09-10', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Scorpions', 'guest_host': '', 'theme': 'On The Road', 'special_notes': '113 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-267', 'air_date': '1988-09-24', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Metal Blocks', 'special_notes': '178 minutes; Three DVD XP Mode', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-337', 'air_date': '1988-12-03', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Testament, Jetboy', 'theme': '', 'special_notes': '122 minutes', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1988-344', 'air_date': '1988-12-10', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Chris Impellitteri', 'theme': '', 'special_notes': '166 minutes; 352x480 resolution', 'source_citations': 'metal-video-collector.blogspot.com'},

    # 1989
    {'episode_id': 'HBB-1989-133', 'air_date': '1989-05-13', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Metal Church, Exodus', 'theme': '', 'special_notes': '179 minutes; Three DVD XP Mode', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1989-147', 'air_date': '1989-05-27', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Lonn Friend, Scott Ian', 'theme': 'Rock Blocks', 'special_notes': '180 minutes; Lonn Friend & Scott Ian Rock Blocks; 352x480', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1989-217', 'air_date': '1989-08-05', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'GWAR', 'theme': '', 'special_notes': '180 minutes; With GWAR; 352x480', 'source_citations': 'metal-video-collector.blogspot.com'},
    {'episode_id': 'HBB-1989-364', 'air_date': '1989-12-30', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': '', 'special_notes': '85 minutes; ADAM\'S FINAL SHOW as host; INCOMPLETE', 'source_citations': 'metal-video-collector.blogspot.com'},
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
    count = add_episodes(EPISODES_METAL_VIDEO)
    print(f"✅ Added {count} episodes from Metal Video Collector!")
    print(f"🎸 Including GUNS N' ROSES HOST (1988-05-14)!")
    print(f"🎸 ADAM CURRY'S FINAL SHOW (1989-12-30)!")
    print(f"📺 1987-1989 coverage EXPLODING!")

#!/usr/bin/env python3
"""
MASSIVE batch: 1989-1992 episodes from Keir's DVD blog
The golden years!
"""

import csv
from pathlib import Path

# Episodes data will be added in batches due to size
# Starting with 1989 (37 episodes)

EPISODES_1989 = [
    {'episode_id': 'HBB-1989-008', 'air_date': '1989-01-07', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Best Of 88', 'special_notes': 'Best of 1988 compilation; 177 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-015', 'air_date': '1989-01-14', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Kix', 'guest_host': '', 'theme': '', 'special_notes': 'Kix band hosted; 179 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-029', 'air_date': '1989-01-28', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Bullet Boys', 'guest_host': '', 'theme': '', 'special_notes': 'Bullet Boys hosted', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-036', 'air_date': '1989-02-04', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Anthrax', 'guest_host': '', 'theme': 'In the Studio', 'special_notes': 'Anthrax: In the Studio; 179 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-043', 'air_date': '1989-02-11', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Danzig', 'theme': '', 'special_notes': 'Adam Curry with Danzig; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-050', 'air_date': '1989-02-18', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Queensryche', 'guest_host': '', 'theme': '', 'special_notes': 'Queensryche hosted; 148 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-057', 'air_date': '1989-02-25', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Rock Blocks Edition', 'special_notes': 'Rock Blocks special; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-071', 'air_date': '1989-03-11', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Lita Ford', 'theme': '', 'special_notes': 'Lita Ford concert; 179 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-078', 'air_date': '1989-03-18', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Ace Frehley & Skid Row', 'theme': '', 'special_notes': 'With Ace Frehley and Skid Row; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-085', 'air_date': '1989-03-25', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Exodus & Celtic Frost', 'theme': '', 'special_notes': 'With Exodus and Celtic Frost; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-092', 'air_date': '1989-04-01', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Kingdom Come, Warrant, Extreme', 'theme': '', 'special_notes': 'With Kingdom Come, Warrant, Extreme; 2.5 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-099', 'air_date': '1989-04-08', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Great White Party', 'special_notes': 'Great White Party special', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-106', 'air_date': '1989-04-15', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Ratt', 'guest_host': 'Kix', 'theme': '', 'special_notes': 'Ratt with Kix; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-113', 'air_date': '1989-04-22', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry & Downtown Julie Brown', 'guest_host': 'W.A.S.P. & M.O.D.', 'theme': '', 'special_notes': 'Co-hosted with Downtown Julie Brown; W.A.S.P. and M.O.D.; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-120', 'air_date': '1989-04-29', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Riki Rachtman', 'theme': '', 'special_notes': 'With Riki Rachtman\'s LA scene report; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-127', 'air_date': '1989-05-06', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Tony Iommi & Cozy Powell', 'guest_host': '', 'theme': '', 'special_notes': 'Black Sabbath members hosted', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-162', 'air_date': '1989-06-10', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-190', 'air_date': '1989-07-08', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': '', 'special_notes': '200:59 with bonus clips', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-197', 'air_date': '1989-07-15', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Nitro', 'theme': '', 'special_notes': 'With Nitro; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-211', 'air_date': '1989-07-29', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Alice Cooper', 'guest_host': '', 'theme': '', 'special_notes': 'Alice Cooper promoting Trash album; 2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-218', 'air_date': '1989-08-05', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': '', 'special_notes': '175:11 complete', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-225', 'air_date': '1989-08-12', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': '', 'theme': 'Moscow Music Peace Festival', 'special_notes': 'Historic Moscow Music Peace Festival coverage; 178 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-232', 'air_date': '1989-08-19', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Steve Stevens', 'theme': '', 'special_notes': 'With Steve Stevens (Atomic Playboys); 178:08', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-239', 'air_date': '1989-08-26', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Bonham', 'guest_host': '', 'theme': '', 'special_notes': 'Bonham hosted', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-253', 'air_date': '1989-09-09', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Dirty Looks & Kreator', 'theme': '', 'special_notes': 'With Dirty Looks and Kreator; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-274', 'air_date': '1989-09-30', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Faster Pussycat', 'theme': '', 'special_notes': 'With Faster Pussycat and forum highlights', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-281', 'air_date': '1989-10-07', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Bang Tango', 'theme': '', 'special_notes': 'With Bang Tango', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-288', 'air_date': '1989-10-14', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Michael Monroe & Dangerous Toys', 'theme': '', 'special_notes': 'With Michael Monroe and Dangerous Toys', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-295', 'air_date': '1989-10-21', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Queensryche', 'guest_host': '', 'theme': '', 'special_notes': 'Queensryche hosted', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-302', 'air_date': '1989-10-28', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Wolfsbane, EZO, Vain', 'theme': '', 'special_notes': 'With Wolfsbane, EZO, and Vain', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-305', 'air_date': '1989-10-31', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Alice Cooper', 'guest_host': '', 'theme': 'Halloween Special', 'special_notes': 'Alice Cooper Halloween Special; 2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-309', 'air_date': '1989-11-04', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Riki Rachtman', 'theme': '', 'special_notes': 'Riki Rachtman at the Cathouse; 181 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-316', 'air_date': '1989-11-11', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Michael Monroe & Jon Sierra', 'guest_host': '', 'theme': '', 'special_notes': 'Michael Monroe and Jon Sierra co-hosted; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-323', 'air_date': '1989-11-18', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Testament, Britny Fox, Overkill, Shotgun Messiah', 'theme': '', 'special_notes': 'With Testament, Britny Fox, Overkill, Shotgun Messiah; 3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-337', 'air_date': '1989-12-02', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Pretty Boy Floyd', 'theme': '', 'special_notes': 'With Pretty Boy Floyd', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1989-344', 'air_date': '1989-12-09', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Fates Warning', 'theme': '80s Request Weekend', 'special_notes': '80s Request Weekend with Fates Warning; 2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count_1989 = add_episodes(EPISODES_1989)
    print(f"✅ Added {count_1989} episodes from 1989!")
    print(f"🎸 1989 is now MUCH more complete!")

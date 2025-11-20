#!/usr/bin/env python3
"""
1990 episodes from Keir's DVD blog - Riki's first full year!
26 episodes total
"""

import csv
from pathlib import Path

EPISODES_1990 = [
    {'episode_id': 'HBB-1990-006', 'air_date': '1990-01-06', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': '', 'special_notes': 'First show', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-013', 'air_date': '1990-01-13', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'MSG', 'theme': '', 'special_notes': 'Incomplete; 128 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-020', 'air_date': '1990-01-20', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Crue Road Report', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-027', 'air_date': '1990-01-27', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'On The Road w/ Faith No More', 'special_notes': '45 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-062', 'air_date': '1990-03-03', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Nuclear Assault', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-083', 'air_date': '1990-03-24', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Savatage', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-090', 'air_date': '1990-03-31', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Brian Wheat & Tommy Skeoch (Tesla)', 'guest_host': '', 'theme': '', 'special_notes': '204 minutes', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-097', 'air_date': '1990-04-07', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Kiss', 'guest_host': '', 'theme': '', 'special_notes': '3 hours; Rating: A', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-104', 'air_date': '1990-04-14', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Michael Monroe', 'theme': 'Not Fakin\' It In Japan', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-111', 'air_date': '1990-04-21', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Michael Monroe', 'guest_host': '', 'theme': 'In Japan', 'special_notes': '166:55', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-132', 'air_date': '1990-05-12', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Kiss, Slaughter, Faster Pussycat', 'theme': 'On The Road', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-139', 'air_date': '1990-05-19', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': 'Decade of Metal', 'special_notes': 'Rating: A-', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-146', 'air_date': '1990-05-26', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Steve Vai', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-160', 'air_date': '1990-06-09', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Prong, Bruce Dickinson', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-167', 'air_date': '1990-06-16', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ozzy Osbourne, Scatterbrain, Babylon A.D.', 'theme': '', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-209', 'air_date': '1990-07-28', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'LA Guns, London Quireboys, Flotsam & Jetsam', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-242', 'air_date': '1990-08-30', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Poison Festival Of Flesh Contest', 'special_notes': '2 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-265', 'air_date': '1990-09-22', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Concrete Foundations Forum', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-286', 'air_date': '1990-10-13', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-300', 'air_date': '1990-10-27', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Cinderella', 'theme': 'Shocktober Edition', 'special_notes': '360:47 with bonus videos', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-307', 'air_date': '1990-11-03', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Cinderella', 'theme': 'Heartbreak Station in New Orleans', 'special_notes': '200:56', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-314', 'air_date': '1990-11-10', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'AC/DC', 'guest_host': '', 'theme': 'Rock Blocks Edition', 'special_notes': '', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-335', 'air_date': '1990-12-01', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slayer, Extreme', 'theme': '', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-349', 'air_date': '1990-12-15', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Testament', 'theme': '', 'special_notes': '3 hours', 'source_citations': 'keirsdvds.blogspot.com'},
    {'episode_id': 'HBB-1990-363', 'air_date': '1990-12-29', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slaughter', 'theme': 'New Years', 'special_notes': '156:13', 'source_citations': 'keirsdvds.blogspot.com'},
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
    count = add_episodes(EPISODES_1990)
    print(f"✅ Added {count} episodes from 1990!")
    print(f"🎸 Riki's first full year is now COMPLETE!")

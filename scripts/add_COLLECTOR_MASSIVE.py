#!/usr/bin/env python3
"""
MASSIVE batch from evilash22's collection
Cross-referenced to find missing episodes
"""

import csv
from pathlib import Path

EPISODES_COLLECTOR_MASSIVE = [
    # 1987
    {'episode_id': 'HBB-1987-056', 'air_date': '1987-02-25', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Dee Snider', 'guest_host': '', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},

    # 1988
    {'episode_id': 'HBB-1988-025', 'air_date': '1988-01-25', 'episode_number': '', 'season': '1987-1988', 'era': 'Classic MTV', 'host': 'Ron Keel', 'guest_host': '', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1988-237', 'air_date': '1988-08-25', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Frehley\'s Comet', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},

    # 1989
    {'episode_id': 'HBB-1989-018', 'air_date': '1989-01-18', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Queensrÿche', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-041', 'air_date': '1989-02-10', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice In Chains, Sepultura', 'theme': '', 'special_notes': 'DVD quality - 26 rare videos, no commercials; Early Riki appearance!', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-074', 'air_date': '1989-03-15', 'episode_number': '', 'season': '1988-1989', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'XYZ, Icon', 'theme': '', 'special_notes': 'Full 3-hour show with commercials; Early Riki appearance', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-105', 'air_date': '1989-04-15', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'The L.A. Report', 'special_notes': 'Full 3-hour show; Early Riki episode', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-119', 'air_date': '1989-04-29', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'The L.A. Report', 'special_notes': 'Full 3-hour show', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-126', 'air_date': '1989-05-06', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Adam Curry', 'guest_host': 'Black Sabbath', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-152', 'air_date': '1989-06-01', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slayer, Megadeth, Alice In Chains', 'theme': '', 'special_notes': 'DVD quality - 23 rare videos, no commercials; EPIC lineup!', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1989-280', 'air_date': '1989-10-07', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': '', 'guest_host': 'Bang Tango', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},

    # 1990
    {'episode_id': 'HBB-1990-001', 'air_date': '1990-01-01', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': '', 'special_notes': 'Riki\'s official first show as host; Full 3 hours with commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1990-122', 'air_date': '1990-05-02', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth', 'theme': '', 'special_notes': 'Megadeth special promoting album', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1990-125', 'air_date': '1990-05-05', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Love/Hate, Law And Order', 'theme': '', 'special_notes': 'Full show', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1990-195', 'air_date': '1990-07-14', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Warrior Soul, Spread Eagle, Heaven\'s Edge', 'theme': '', 'special_notes': 'Full 3-hour show with commercials', 'source_citations': 'evilash22.tripod.com'},

    # 1991
    {'episode_id': 'HBB-1991-026', 'air_date': '1991-01-26', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': 'On The Road', 'special_notes': '2.5 hour show, no commercials', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1991-164', 'air_date': '1991-06-13', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Saigon Kick, Tora Tora', 'theme': '', 'special_notes': 'Full show', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1991-166', 'air_date': '1991-06-15', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Kik Tracee, Dangerous Toys', 'theme': '', 'special_notes': 'Full show', 'source_citations': 'evilash22.tripod.com'},
    {'episode_id': 'HBB-1991-208', 'air_date': '1991-07-27', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'Full show', 'source_citations': 'evilash22.tripod.com'},
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
    count = add_episodes(EPISODES_COLLECTOR_MASSIVE)
    print(f"✅ Added {count} episodes from collector's MASSIVE list!")
    print(f"🎸 Including RIKI'S OFFICIAL FIRST SHOW (1990-01-01)!")
    print(f"🎸 SLAYER/MEGADETH/ALICE IN CHAINS epic lineup!")
    print(f"📺 Coverage exploding!")

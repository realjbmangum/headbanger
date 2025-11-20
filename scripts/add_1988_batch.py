#!/usr/bin/env python3
"""
1988 episodes from Keir's DVD trading blog.
Completing Year 1!
"""

import csv
from pathlib import Path

# 1988 episodes
EPISODES_1988 = [
    {
        'episode_id': 'HBB-1988-010',
        'air_date': '1988-01-09',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Ron Keel',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Ron Keel hosted; 95 minutes, bonus version 120:52',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-031',
        'air_date': '1988-01-30',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Kevin Seal hosted',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-038',
        'air_date': '1988-02-06',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Anthrax',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Anthrax hosted; Incomplete 90 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-045',
        'air_date': '1988-02-13',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Lita Ford',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Lita Ford hosted',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-052',
        'air_date': '1988-02-20',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Kevin Seal hosted; Incomplete 122 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-066',
        'air_date': '1988-03-05',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'DIO',
        'guest_host': '',
        'theme': 'MTV Concert Special',
        'special_notes': 'DIO MTV concert from San Antonio, TX',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-087',
        'air_date': '1988-03-26',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': 'L.A. Guns',
        'theme': '',
        'special_notes': 'Kevin Seal with L.A. Guns; 129:35',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-115',
        'air_date': '1988-04-23',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Zodiac Mindwarp',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Zodiac Mindwarp hosted; 3 DVDs',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-129',
        'air_date': '1988-05-07',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Bruce Dickinson',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Bruce Dickinson (Iron Maiden) hosted; 118 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-150',
        'air_date': '1988-05-28',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': 'Rock Blocks',
        'special_notes': 'Adam Curry hosts Rock Blocks; 3 DVDs',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-164',
        'air_date': '1988-06-11',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Sam Kinison',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Sam Kinison hosted; 160 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-178',
        'air_date': '1988-06-25',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Frehley\'s Comet',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Frehley\'s Comet hosted',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-192',
        'air_date': '1988-07-09',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': 'Joe Satriani',
        'theme': '',
        'special_notes': 'Adam Curry with Joe Satriani; 162:29',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-205',
        'air_date': '1988-07-23',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Vinnie Vincent',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Vinnie Vincent hosted; 140:37',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-212',
        'air_date': '1988-07-30',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Adam Curry hosted; 178:44',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-219',
        'air_date': '1988-08-13',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Rob Halford',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Rob Halford (Judas Priest) hosted; 239:26',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-227',
        'air_date': '1988-08-27',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': 'Megaforce 5th Anniversary',
        'special_notes': 'Megaforce Records 5th Anniversary special; 179 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-241',
        'air_date': '1988-09-17',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': 'L.A. Guns, Lizzy Borden, Nuclear Assault',
        'theme': '',
        'special_notes': 'Adam Curry with L.A. Guns, Lizzy Borden, Nuclear Assault',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-283',
        'air_date': '1988-10-08',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': 'Foundations Forum/Rip Party',
        'special_notes': 'Foundations Forum and Rip Magazine party; 3 hours',
        'source_citations': 'keirsdvds.blogspot.com'
    },
    {
        'episode_id': 'HBB-1988-297',
        'air_date': '1988-10-31',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Sam Kinison',
        'guest_host': '',
        'theme': 'Halloween Special',
        'special_notes': 'Sam Kinison Halloween Special; Incomplete 80 minutes',
        'source_citations': 'keirsdvds.blogspot.com'
    },
]

def add_episodes():
    """Add 1988 episodes."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    # Read existing
    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    # Filter new
    new_to_add = [ep for ep in EPISODES_1988 if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        print("No new episodes to add")
        return 0

    # Append
    with open(episodes_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                      'host', 'guest_host', 'theme', 'special_notes', 'source_citations']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for ep in new_to_add:
            writer.writerow(ep)

    print(f"✅ Added {len(new_to_add)} 1988 episodes!")
    print(f"\n1988 Episodes by month:")
    months = {}
    for ep in new_to_add:
        month = ep['air_date'][5:7]  # MM
        month_name = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][int(month)]
        months[month_name] = months.get(month_name, 0) + 1

    for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        if month in months:
            print(f"  {month}: {months[month]} episodes")

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes()
    print(f"\n🎸 1988 BATCH: {count} episodes added!")
    print(f"📺 Year 1 (1987-1988) nearly COMPLETE!")

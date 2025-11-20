#!/usr/bin/env python3
"""
Bulk add episodes discovered from web scraping.
This is a one-time import of episodes found from Archive.org and other sources.
"""

import csv
from pathlib import Path

# New episodes discovered from Archive.org and web searches
NEW_EPISODES = [
    # 1987 episodes
    {
        'episode_id': 'HBB-1987-235',
        'air_date': '1987-08-22',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': 'Jack Russell & Michael Lardie (Great White)',
        'theme': '',
        'special_notes': 'Archived on archive.org',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1987-297',
        'air_date': '1987-10-24',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Smash',
        'guest_host': 'Guns N\' Roses',
        'theme': '',
        'special_notes': 'Special guest hosts Guns N\' Roses',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1987-331',
        'air_date': '1987-10-31',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Kevin Seal',
        'guest_host': '',
        'theme': 'Halloween Special',
        'special_notes': 'Featured concert footage of Helloween, Armored Saint, and Grim Reaper',
        'source_citations': 'web search results'
    },
    {
        'episode_id': 'HBB-1987-339',
        'air_date': '1987-12-05',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Unknown',
        'guest_host': 'Robin McCauley & Michael Schenker (McCauley Schenker Group)',
        'theme': '',
        'special_notes': 'Hosted by MSG members',
        'source_citations': 'archive.org'
    },
    # 1988 episodes
    {
        'episode_id': 'HBB-1988-226',
        'air_date': '1988-08-13',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Full episode archived',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1988-233',
        'air_date': '1988-08-20',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Full episode archived',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1988-247',
        'air_date': '1988-09-03',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': 'Axl Rose & Slash (Guns N\' Roses)',
        'theme': '',
        'special_notes': 'Special guest hosts from Guns N\' Roses',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1988-289',
        'air_date': '1988-10-15',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': 'Yngwie J. Malmsteen',
        'theme': '',
        'special_notes': 'Special guest host Yngwie Malmsteen',
        'source_citations': 'archive.org'
    },
    # 1989 episode
    {
        'episode_id': 'HBB-1989-364',
        'air_date': '1989-12-30',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': 'Adam\'s Last Show',
        'special_notes': 'Final episode hosted by Adam Curry before Riki Rachtman took over',
        'source_citations': 'archive.org'
    },
    # 1990 episodes
    {
        'episode_id': 'HBB-1990-139',
        'air_date': '1990-05-19',
        'episode_number': '139',
        'season': '1989-1990',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Motley Crue',
        'theme': 'Decade of Metal Marathon',
        'special_notes': 'Riki\'s first episode! Special marathon with interviews with David Lee Roth, Steven Tyler, Alice Cooper; AC/DC live performances',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1990-147',
        'air_date': '1990-06-16',
        'episode_number': '',
        'season': '1989-1990',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Ozzy Osbourne, Babylon A.D., & Scatterbrain',
        'theme': 'Riki\'s Birthday',
        'special_notes': 'Riki Rachtman\'s birthday episode',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1990-189',
        'air_date': '1990-07-07',
        'episode_number': '',
        'season': '1989-1990',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': '',
        'theme': 'On The Road With Winger',
        'special_notes': 'Location shoot with Winger',
        'source_citations': 'archive.org'
    },
    # 1991 episodes
    {
        'episode_id': 'HBB-1991-16',
        'air_date': '1991-04-20',
        'episode_number': '211',
        'season': '1990-1991',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'White Lion & Mind Funk',
        'theme': '',
        'special_notes': 'Featured White Lion and Mind Funk',
        'source_citations': 'web search results'
    },
    {
        'episode_id': 'HBB-1991-121',
        'air_date': '1991-05-04',
        'episode_number': '213',
        'season': '1990-1991',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Lemmy Kilmister (Motorhead)',
        'theme': '',
        'special_notes': 'Featured Lemmy Kilmister of Motorhead',
        'source_citations': 'web search results'
    },
    # 1992 episodes
    {
        'episode_id': 'HBB-1992-137',
        'air_date': '1992-05-16',
        'episode_number': '',
        'season': '1991-1992',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Alice In Chains',
        'theme': 'At the Mansion',
        'special_notes': 'Special episode from The Mansion featuring Alice In Chains. Top 10 included Slaughter, Def Leppard, Pearl Jam, Ozzy, Kings X, Nirvana, Body Count, Kiss, Soundgarden, Vince Neil',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1992-235',
        'air_date': '1992-08-22',
        'episode_number': '',
        'season': '1991-1992',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'GWAR & Ministry',
        'theme': '',
        'special_notes': 'Featured GWAR and Ministry',
        'source_citations': 'archive.org; web search results'
    },
    {
        'episode_id': 'HBB-1992-340',
        'air_date': '1992-12-05',
        'episode_number': '',
        'season': '1992-1993',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Stone Temple Pilots',
        'theme': 'Countdown to the Ball',
        'special_notes': 'Featured Stone Temple Pilots. Top 10 countdown included Guns N\' Roses, Metallica, AC/DC, Ozzy, Alice in Chains, Megadeth, Nirvana, Saigon Kick, Extreme, Def Leppard',
        'source_citations': 'archive.org'
    },
    # 1993 episode
    {
        'episode_id': 'HBB-1993-213',
        'air_date': '1993-07-31',
        'episode_number': '',
        'season': '1992-1993',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Alice in Chains',
        'theme': 'On the Road',
        'special_notes': 'On location at Action Park, NJ with Alice in Chains',
        'source_citations': 'archive.org'
    },
    # 1994 episodes
    {
        'episode_id': 'HBB-1994-222',
        'air_date': '1994-08-09',
        'episode_number': '',
        'season': '1993-1994',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': '',
        'theme': 'Movie Premier of Airheads',
        'special_notes': 'Special Tuesday Edition featuring the movie premiere of Airheads',
        'source_citations': 'archive.org'
    },
    {
        'episode_id': 'HBB-1994-000',
        'air_date': '1994-01-01',
        'episode_number': '',
        'season': '1993-1994',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': '',
        'theme': 'Headbangers Bar-B-Q Japan',
        'special_notes': 'Special episode filmed in Japan',
        'source_citations': 'archive.org'
    },
]

def add_episodes():
    """Add all new episodes to the CSV file."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    # Read existing episodes to check for duplicates
    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    # Filter out duplicates
    new_to_add = [ep for ep in NEW_EPISODES if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        print("No new episodes to add (all already exist)")
        return

    # Append new episodes
    with open(episodes_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                      'host', 'guest_host', 'theme', 'special_notes', 'source_citations']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        for ep in new_to_add:
            writer.writerow(ep)

    print(f"✅ Added {len(new_to_add)} new episodes to the dataset!")
    print(f"\nEpisodes added:")
    for ep in new_to_add:
        print(f"  {ep['air_date']} - {ep['episode_id']} - {ep['host']}")

if __name__ == "__main__":
    add_episodes()

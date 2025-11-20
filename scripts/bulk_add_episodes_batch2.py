#!/usr/bin/env python3
"""
Bulk add episodes - Batch 2
Additional episodes discovered from Archive.org and web searches.
"""

import csv
from pathlib import Path

# Batch 2: New episodes discovered
NEW_EPISODES_BATCH2 = [
    # 1987 episodes
    {
        'episode_id': 'HBB-1987-249',
        'air_date': '1987-09-05',
        'episode_number': '',
        'season': '1987-1988',
        'era': 'Classic MTV',
        'host': 'King Diamond',
        'guest_host': '',
        'theme': '',
        'special_notes': 'Two-hour special hosted by King Diamond; Featured 24 music videos including Great White, Ozzy, Aerosmith, Def Leppard, KISS, Motorhead, Twisted Sister, Dio, Iron Maiden, Guns N\' Roses, Motley Crue',
        'source_citations': 'archive.org'
    },
    # 1989 episodes
    {
        'episode_id': 'HBB-1989-363',
        'air_date': '1989-12-28',
        'episode_number': '',
        'season': '1988-1989',
        'era': 'Classic MTV',
        'host': 'Adam Curry',
        'guest_host': '',
        'theme': 'End of Year Episode',
        'special_notes': 'Special end-of-year episode',
        'source_citations': 'archive.org'
    },
    # 1991 episodes
    {
        'episode_id': 'HBB-1991-306',
        'air_date': '1991-11-02',
        'episode_number': '238',
        'season': '1991-1992',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Nirvana & Sepultura',
        'theme': '',
        'special_notes': 'Historic episode featuring Nirvana and Sepultura',
        'source_citations': 'trakt.tv; imdb.com'
    },
    {
        'episode_id': 'HBB-1991-327',
        'air_date': '1991-11-23',
        'episode_number': '242',
        'season': '1991-1992',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Ozzy & Jack Osbourne',
        'theme': 'Rock Blocks Edition',
        'special_notes': 'Featured Ozzy Osbourne, Guns N\' Roses, Queensryche, Metallica, Skid Row, Warrior Soul, Motley Crue, Slayer, Infectious Grooves, Suicidal Tendencies',
        'source_citations': 'archive.org; web search'
    },
    {
        'episode_id': 'HBB-1991-348',
        'air_date': '1991-12-14',
        'episode_number': '245',
        'season': '1991-1992',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': '',
        'theme': 'Aerosmith Tribute Show',
        'special_notes': 'Tribute featuring Aerosmith videos including "Dude Looks Like A Lady", "Jamie\'s Got A Gun"; interviews with Steven Tyler, Tom Hamilton, Joey Kramer',
        'source_citations': 'web search; archive.org'
    },
    # 1992 episodes
    {
        'episode_id': 'HBB-1992-362',
        'air_date': '1992-12-27',
        'episode_number': '',
        'season': '1992-1993',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'Dave Mustaine',
        'theme': 'Year-End Special',
        'special_notes': 'Special episode celebrating heavy music of 1992; Featured Dave Mustaine',
        'source_citations': 'archive.org'
    },
    # 1993 episodes
    {
        'episode_id': 'HBB-1993-219',
        'air_date': '1993-08-07',
        'episode_number': '',
        'season': '1992-1993',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': 'King Diamond',
        'theme': 'Ozzy Osbourne Live & Loud',
        'special_notes': 'Featured Ozzy Osbourne Live & Loud with guest King Diamond',
        'source_citations': 'archive.org'
    },
    # 1995 final episode
    {
        'episode_id': 'HBB-1995-015',
        'air_date': '1995-01-15',
        'episode_number': '408',
        'season': '1994-1995',
        'era': 'Classic MTV',
        'host': 'Riki Rachtman',
        'guest_host': '',
        'theme': 'Best of Headbangers Ball - Final Episode',
        'special_notes': 'FINAL EPISODE of classic MTV run! Retrospective featuring Guns N\' Roses, Faith No More, Metallica "One", Pearl Jam, Nirvana interviews; Ended with Riki singing "Stone Cold Crazy" with Metallica',
        'source_citations': 'web search; thetvdb.com'
    },
    # MTV2 Revival era
    {
        'episode_id': 'HBB-2003-616',
        'air_date': '2003-06-16',
        'episode_number': '',
        'season': 'Season 9',
        'era': 'MTV2 Revival',
        'host': 'Jamey Jasta',
        'guest_host': 'Riki Rachtman',
        'theme': 'MTV2 Reboot',
        'special_notes': 'MTV2 revival episode with special guest Riki Rachtman; Truncated hour-long repeat format',
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
    new_to_add = [ep for ep in NEW_EPISODES_BATCH2 if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        print("No new episodes to add (all already exist)")
        return 0

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

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes()
    print(f"\n🎸 Batch 2 complete: {count} episodes added!")

#!/usr/bin/env python3
"""
Renumber episodes sequentially and sort by air date
"""

import csv
from pathlib import Path
from datetime import datetime

def renumber_and_sort():
    """Renumber all episodes and sort by air date."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    # Read all episodes
    episodes = []
    with open(episodes_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        episodes = list(reader)

    # Sort by air_date
    episodes.sort(key=lambda x: datetime.strptime(x['air_date'], '%Y-%m-%d'))

    # Renumber sequentially
    for i, episode in enumerate(episodes, start=1):
        episode['episode_number'] = str(i)

    # Write back to CSV
    fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                  'host', 'guest_host', 'theme', 'special_notes', 'source_citations']

    with open(episodes_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(episodes)

    return len(episodes)

if __name__ == "__main__":
    count = renumber_and_sort()
    print(f"✅ Renumbered and sorted {count} episodes!")
    print(f"📅 Episodes now in chronological order")
    print(f"🔢 Episode numbers: 1-{count}")

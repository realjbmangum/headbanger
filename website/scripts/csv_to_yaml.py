#!/usr/bin/env python3
"""
Convert CSV episode data to Jekyll-compatible YAML format
"""

import csv
import yaml
from pathlib import Path
from datetime import datetime

def load_episodes(csv_path):
    """Load episodes from CSV."""
    episodes = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            episodes.append(row)
    return episodes

def create_episode_files(episodes, output_dir):
    """Create individual markdown files for each episode."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for episode in episodes:
        # Parse date
        air_date = datetime.strptime(episode['air_date'], '%Y-%m-%d')

        # Create filename: YYYY-MM-DD-episode-id.md
        filename = f"{episode['air_date']}-{episode['episode_id']}.md"
        filepath = output_dir / filename

        # Prepare front matter
        front_matter = {
            'layout': 'episode',
            'title': f"Episode {episode['episode_number'] or 'TBA'} - {air_date.strftime('%B %d, %Y')}",
            'episode_id': episode['episode_id'],
            'air_date': episode['air_date'],
            'episode_number': episode['episode_number'],
            'season': episode['season'],
            'era': episode['era'],
            'host': episode['host'],
            'guest_host': episode['guest_host'],
            'theme': episode['theme'],
            'special_notes': episode['special_notes'],
            'source_citations': episode['source_citations'],
        }

        # Remove empty values
        front_matter = {k: v for k, v in front_matter.items() if v}

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(front_matter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')

            # Optional content area for episode details
            if episode['special_notes']:
                f.write(f"## About This Episode\n\n{episode['special_notes']}\n\n")

            if episode['guest_host']:
                f.write(f"**Featured Guests:** {episode['guest_host']}\n\n")

    print(f"✅ Created {len(episodes)} episode files in {output_dir}")

def create_data_yaml(episodes, output_file):
    """Create a YAML data file with all episodes for easy access."""
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Convert to simple dict format
    episodes_data = []
    for ep in episodes:
        episodes_data.append({
            'id': ep['episode_id'],
            'date': ep['air_date'],
            'number': ep['episode_number'],
            'season': ep['season'],
            'era': ep['era'],
            'host': ep['host'],
            'guest_host': ep['guest_host'],
            'theme': ep['theme'],
            'notes': ep['special_notes'],
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump({'episodes': episodes_data}, f, default_flow_style=False, allow_unicode=True)

    print(f"✅ Created data file: {output_file}")

def generate_stats(episodes):
    """Generate statistics for the site."""
    from collections import Counter

    stats = {
        'total_episodes': len(episodes),
        'years': {},
        'hosts': {},
        'eras': {},
    }

    # Count by year
    year_counter = Counter()
    for ep in episodes:
        year = ep['air_date'][:4]
        year_counter[year] += 1
    stats['years'] = dict(sorted(year_counter.items()))

    # Count by host
    host_counter = Counter()
    for ep in episodes:
        if ep['host']:
            host_counter[ep['host']] += 1
    stats['hosts'] = dict(host_counter.most_common(20))

    # Count by era
    era_counter = Counter()
    for ep in episodes:
        if ep['era']:
            era_counter[ep['era']] += 1
    stats['eras'] = dict(era_counter.items())

    return stats

if __name__ == "__main__":
    # Paths
    csv_path = Path(__file__).parent.parent.parent / 'data' / 'episodes.csv'
    episodes_dir = Path(__file__).parent.parent / '_episodes'
    data_dir = Path(__file__).parent.parent / '_data'

    print("🎸 Converting episode data to Jekyll format...")

    # Load episodes
    episodes = load_episodes(csv_path)
    print(f"📊 Loaded {len(episodes)} episodes")

    # Create episode files
    create_episode_files(episodes, episodes_dir)

    # Create data YAML
    create_data_yaml(episodes, data_dir / 'episodes.yml')

    # Generate and save stats
    stats = generate_stats(episodes)
    with open(data_dir / 'stats.yml', 'w') as f:
        yaml.dump(stats, f, default_flow_style=False)
    print(f"✅ Created stats file")

    print("\n🎉 Jekyll data generation complete!")
    print(f"   - {len(episodes)} episode files in _episodes/")
    print(f"   - episodes.yml in _data/")
    print(f"   - stats.yml in _data/")

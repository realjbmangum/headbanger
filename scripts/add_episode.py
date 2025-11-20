#!/usr/bin/env python3
"""
Interactive helper script for adding new episodes to the Headbangers Ball dataset.
Provides guided data entry with validation and automatic formatting.
"""

import csv
import sys
from datetime import datetime
from pathlib import Path


class EpisodeAdder:
    """Helper for adding episodes to the dataset."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.episodes_file = self.data_dir / "episodes.csv"
        self.videos_file = self.data_dir / "videos.csv"
        self.hosts_file = self.data_dir / "hosts.csv"
        self.existing_ids = set()
        self.load_existing_ids()

    def load_existing_ids(self):
        """Load existing episode IDs to prevent duplicates."""
        if self.episodes_file.exists():
            with open(self.episodes_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    def validate_date(self, date_str: str) -> bool:
        """Validate date format."""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def generate_episode_id(self, date_str: str, episode_num: str = "") -> str:
        """Generate episode ID in format HBB-YYYY-NNN."""
        year = date_str[:4]
        if episode_num:
            return f"HBB-{year}-{episode_num.zfill(3)}"
        else:
            # Generate based on date
            month_day = date_str[5:].replace('-', '')
            return f"HBB-{year}-{month_day}"

    def prompt_with_default(self, prompt: str, default: str = "") -> str:
        """Prompt user with optional default value."""
        if default:
            result = input(f"{prompt} [{default}]: ").strip()
            return result if result else default
        return input(f"{prompt}: ").strip()

    def add_episode_interactive(self):
        """Interactive episode addition."""
        print("\n" + "="*60)
        print("Add New Episode - Interactive Mode")
        print("="*60)
        print("Leave fields blank to skip optional fields.\n")

        # Air date (required)
        while True:
            air_date = input("Air date (YYYY-MM-DD) [required]: ").strip()
            if not air_date:
                print("  ❌ Air date is required!")
                continue
            if not self.validate_date(air_date):
                print("  ❌ Invalid date format! Use YYYY-MM-DD")
                continue
            break

        # Episode number
        episode_num = input("Episode number (e.g., 150): ").strip()

        # Generate episode ID
        suggested_id = self.generate_episode_id(air_date, episode_num)
        episode_id = self.prompt_with_default("Episode ID", suggested_id)

        # Check for duplicate
        if episode_id in self.existing_ids:
            print(f"  ⚠️  Warning: Episode ID '{episode_id}' already exists!")
            overwrite = input("Continue anyway? (y/n): ").lower()
            if overwrite != 'y':
                print("Cancelled.")
                return None

        # Season
        year = air_date[:4]
        next_year = str(int(year) + 1)
        suggested_season = f"{year}-{next_year}"
        season = self.prompt_with_default("Season", suggested_season)

        # Era
        print("\nEra options:")
        print("  1. Classic MTV (1987-1995)")
        print("  2. MTV2 Revival (2003-2007)")
        print("  3. 2011 Revival (2011-2012)")
        era_choice = input("Select era (1-3) [1]: ").strip() or "1"
        era_map = {
            "1": "Classic MTV",
            "2": "MTV2 Revival",
            "3": "2011 Revival"
        }
        era = era_map.get(era_choice, "Classic MTV")

        # Host
        print("\nCommon hosts:")
        print("  1. Kevin Seal")
        print("  2. Adam Curry")
        print("  3. Riki Rachtman")
        print("  4. Jamey Jasta")
        print("  5. Other/Unknown")
        host_choice = input("Select host (1-5) or type name: ").strip()
        host_map = {
            "1": "Kevin Seal",
            "2": "Adam Curry",
            "3": "Riki Rachtman",
            "4": "Jamey Jasta",
            "5": "Unknown"
        }
        host = host_map.get(host_choice, host_choice)

        # Guest host
        guest_host = input("Guest host (optional): ").strip()

        # Theme
        theme = input("Theme (optional, e.g., 'Christmas Special'): ").strip()

        # Special notes
        special_notes = input("Special notes (optional): ").strip()

        # Source citations
        print("\nCommon sources:")
        print("  episodehive.com, thetvdb.com, imdb.com, youtube.com")
        source_citations = input("Source citations (required, separate with '; '): ").strip()
        if not source_citations:
            source_citations = "episodehive.com"

        # Build episode dict
        episode = {
            'episode_id': episode_id,
            'air_date': air_date,
            'episode_number': episode_num,
            'season': season,
            'era': era,
            'host': host,
            'guest_host': guest_host,
            'theme': theme,
            'special_notes': special_notes,
            'source_citations': source_citations
        }

        return episode

    def display_episode(self, episode: dict):
        """Display episode for confirmation."""
        print("\n" + "="*60)
        print("Episode Preview")
        print("="*60)
        for key, value in episode.items():
            if value:
                print(f"  {key:20} {value}")
        print("="*60)

    def save_episode(self, episode: dict):
        """Append episode to CSV file."""
        # Read existing data
        with open(self.episodes_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Append new episode
        with open(self.episodes_file, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=episode.keys())
            writer.writerow(episode)

        print(f"\n✅ Episode {episode['episode_id']} added successfully!")

    def add_videos_for_episode(self, episode_id: str):
        """Add videos for an episode."""
        print(f"\n📼 Add videos for episode {episode_id}? (y/n): ", end="")
        if input().lower() != 'y':
            return

        videos = []
        video_num = 1

        while True:
            print(f"\n--- Video {video_num} ---")
            artist = input("Artist name (or blank to finish): ").strip()
            if not artist:
                break

            song = input("Song title: ").strip()
            if not song:
                print("  ⚠️  Song title required for video entry")
                continue

            album = input("Album (optional): ").strip()
            year = input("Release year (optional): ").strip()
            genre = input("Genre (optional): ").strip()

            video_id = f"VID-{episode_id.split('-')[1]}-{str(video_num).zfill(3)}"

            video = {
                'video_id': video_id,
                'episode_id': episode_id,
                'air_date': '',  # Will use episode date
                'artist': artist,
                'song_title': song,
                'album': album,
                'release_year': year,
                'genre': genre,
                'video_director': '',
                'play_order': str(video_num),
                'source_citations': 'episodehive.com'
            }

            videos.append(video)
            video_num += 1

            print(f"  ✓ Added: {artist} - {song}")

        if videos:
            self.save_videos(videos)
            print(f"\n✅ Added {len(videos)} video(s) to dataset")

    def save_videos(self, videos: list):
        """Append videos to CSV file."""
        with open(self.videos_file, 'a', encoding='utf-8', newline='') as f:
            if videos:
                writer = csv.DictWriter(f, fieldnames=videos[0].keys())
                for video in videos:
                    writer.writerow(video)

    def run(self):
        """Main run loop."""
        print("\n🎸 Headbangers Ball - Episode Data Entry Helper")
        print("="*60)

        while True:
            episode = self.add_episode_interactive()

            if episode:
                self.display_episode(episode)

                confirm = input("\nSave this episode? (y/n): ").lower()
                if confirm == 'y':
                    self.save_episode(episode)
                    self.existing_ids.add(episode['episode_id'])

                    # Optionally add videos
                    self.add_videos_for_episode(episode['episode_id'])
                else:
                    print("Episode discarded.")

            print("\n" + "="*60)
            another = input("Add another episode? (y/n): ").lower()
            if another != 'y':
                break

        print("\n✅ Data entry session complete!")
        print("Run 'python scripts/validate.py' to verify your entries.\n")


def main():
    """Main entry point."""
    try:
        adder = EpisodeAdder()
        adder.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

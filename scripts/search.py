#!/usr/bin/env python3
"""
Search and lookup tool for the Headbangers Ball dataset.
Query episodes by date, host, year, or other criteria.
"""

import csv
import sys
from pathlib import Path
from datetime import datetime


class DatasetSearcher:
    """Search and query the Headbangers Ball dataset."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.episodes = []
        self.videos = []
        self.hosts = []
        self.load_data()

    def load_data(self):
        """Load all dataset files."""
        # Load episodes
        episodes_file = self.data_dir / "episodes.csv"
        if episodes_file.exists():
            with open(episodes_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.episodes = [row for row in reader if row.get('episode_id')]

        # Load videos
        videos_file = self.data_dir / "videos.csv"
        if videos_file.exists():
            with open(videos_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.videos = [row for row in reader if row.get('video_id')]

        # Load hosts
        hosts_file = self.data_dir / "hosts.csv"
        if hosts_file.exists():
            with open(hosts_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.hosts = [row for row in reader if row.get('host_id')]

    def search_by_date(self, date_str: str):
        """Search episodes by date."""
        results = [ep for ep in self.episodes if ep['air_date'] == date_str]
        return results

    def search_by_year(self, year: str):
        """Search episodes by year."""
        results = [ep for ep in self.episodes if ep['air_date'].startswith(year)]
        return results

    def search_by_host(self, host_name: str):
        """Search episodes by host (case-insensitive partial match)."""
        host_lower = host_name.lower()
        results = [ep for ep in self.episodes if host_lower in ep['host'].lower()]
        return results

    def search_by_episode_number(self, episode_num: str):
        """Search by episode number."""
        results = [ep for ep in self.episodes if ep['episode_number'] == episode_num]
        return results

    def search_by_keyword(self, keyword: str):
        """Search across all episode fields for keyword."""
        keyword_lower = keyword.lower()
        results = []
        for ep in self.episodes:
            # Search in all text fields
            searchable = ' '.join([
                ep.get('host', ''),
                ep.get('guest_host', ''),
                ep.get('theme', ''),
                ep.get('special_notes', ''),
                ep.get('episode_id', '')
            ]).lower()

            if keyword_lower in searchable:
                results.append(ep)

        return results

    def get_episode_videos(self, episode_id: str):
        """Get all videos for a specific episode."""
        return [v for v in self.videos if v['episode_id'] == episode_id]

    def search_artist(self, artist_name: str):
        """Search for artist in video listings."""
        artist_lower = artist_name.lower()
        results = [v for v in self.videos if artist_lower in v['artist'].lower()]
        return results

    def display_episode(self, episode: dict, show_videos: bool = False):
        """Display episode information."""
        print(f"\n{'='*60}")
        print(f"📺 {episode['episode_id']} - {episode['air_date']}")
        print(f"{'='*60}")
        print(f"Episode Number: {episode.get('episode_number', 'Unknown')}")
        print(f"Season:         {episode.get('season', 'Unknown')}")
        print(f"Era:            {episode.get('era', 'Unknown')}")
        print(f"Host:           {episode.get('host', 'Unknown')}")

        if episode.get('guest_host'):
            print(f"Guest Host:     {episode['guest_host']}")
        if episode.get('theme'):
            print(f"Theme:          {episode['theme']}")
        if episode.get('special_notes'):
            print(f"Notes:          {episode['special_notes']}")

        print(f"Sources:        {episode.get('source_citations', 'None')}")

        if show_videos:
            videos = self.get_episode_videos(episode['episode_id'])
            if videos:
                print(f"\n🎬 Videos ({len(videos)}):")
                for i, video in enumerate(videos, 1):
                    print(f"  {i:2}. {video['artist']} - {video['song_title']}")

    def display_video(self, video: dict):
        """Display video information."""
        print(f"\n🎬 {video['artist']} - {video['song_title']}")
        if video.get('album'):
            print(f"   Album: {video['album']}")
        if video.get('release_year'):
            print(f"   Year: {video['release_year']}")
        if video.get('genre'):
            print(f"   Genre: {video['genre']}")
        print(f"   Episode: {video['episode_id']}")

    def show_stats(self):
        """Display dataset statistics."""
        print("\n" + "="*60)
        print("📊 Headbangers Ball Dataset Statistics")
        print("="*60)
        print(f"Total Episodes: {len(self.episodes)}")
        print(f"Total Videos:   {len(self.videos)}")
        print(f"Total Hosts:    {len(self.hosts)}")

        if self.episodes:
            dates = [ep['air_date'] for ep in self.episodes if ep.get('air_date')]
            if dates:
                dates.sort()
                print(f"\nDate Range:")
                print(f"  First: {dates[0]}")
                print(f"  Last:  {dates[-1]}")

            # Count by host
            from collections import Counter
            host_counts = Counter(ep['host'] for ep in self.episodes if ep.get('host'))
            print(f"\nEpisodes by Host:")
            for host, count in host_counts.most_common(5):
                print(f"  {host:25} {count:3}")

    def interactive_search(self):
        """Interactive search interface."""
        print("\n🔍 Headbangers Ball Dataset Search")
        print("="*60)
        print("\nSearch options:")
        print("  1. Search by date (YYYY-MM-DD)")
        print("  2. Search by year (YYYY)")
        print("  3. Search by host name")
        print("  4. Search by episode number")
        print("  5. Search by keyword")
        print("  6. Search artist/band")
        print("  7. Show dataset statistics")
        print("  8. List all episodes")
        print("  0. Exit")

        while True:
            print("\n" + "-"*60)
            choice = input("Select option (0-8): ").strip()

            if choice == '0':
                break

            elif choice == '1':
                date = input("Enter date (YYYY-MM-DD): ").strip()
                results = self.search_by_date(date)
                if results:
                    for ep in results:
                        self.display_episode(ep, show_videos=True)
                else:
                    print(f"❌ No episodes found for date {date}")

            elif choice == '2':
                year = input("Enter year (YYYY): ").strip()
                results = self.search_by_year(year)
                if results:
                    print(f"\n✓ Found {len(results)} episode(s) in {year}:")
                    for ep in results:
                        print(f"  {ep['air_date']} - {ep['episode_id']} - {ep['host']}")
                else:
                    print(f"❌ No episodes found for year {year}")

            elif choice == '3':
                host = input("Enter host name: ").strip()
                results = self.search_by_host(host)
                if results:
                    print(f"\n✓ Found {len(results)} episode(s) hosted by {host}:")
                    for ep in results:
                        print(f"  {ep['air_date']} - {ep['episode_id']}")
                else:
                    print(f"❌ No episodes found for host '{host}'")

            elif choice == '4':
                num = input("Enter episode number: ").strip()
                results = self.search_by_episode_number(num)
                if results:
                    for ep in results:
                        self.display_episode(ep, show_videos=True)
                else:
                    print(f"❌ Episode number {num} not found")

            elif choice == '5':
                keyword = input("Enter keyword: ").strip()
                results = self.search_by_keyword(keyword)
                if results:
                    print(f"\n✓ Found {len(results)} episode(s) matching '{keyword}':")
                    for ep in results:
                        print(f"  {ep['air_date']} - {ep['episode_id']} - {ep['host']}")
                        if ep.get('special_notes'):
                            print(f"    Note: {ep['special_notes'][:60]}...")
                else:
                    print(f"❌ No episodes found matching '{keyword}'")

            elif choice == '6':
                artist = input("Enter artist/band name: ").strip()
                results = self.search_artist(artist)
                if results:
                    print(f"\n✓ Found {len(results)} video(s) by '{artist}':")
                    for video in results:
                        self.display_video(video)
                else:
                    print(f"❌ No videos found for artist '{artist}'")

            elif choice == '7':
                self.show_stats()

            elif choice == '8':
                if self.episodes:
                    print(f"\n📺 All Episodes ({len(self.episodes)}):")
                    for ep in sorted(self.episodes, key=lambda x: x['air_date']):
                        print(f"  {ep['air_date']} - {ep['episode_id']:20} - {ep['host']}")
                else:
                    print("❌ No episodes in dataset")

            else:
                print("❌ Invalid option")

        print("\n✅ Search session complete!")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Command-line search
        searcher = DatasetSearcher()
        command = sys.argv[1].lower()

        if command == 'stats':
            searcher.show_stats()
        elif command == 'year' and len(sys.argv) > 2:
            results = searcher.search_by_year(sys.argv[2])
            for ep in results:
                print(f"{ep['air_date']} - {ep['episode_id']}")
        elif command == 'host' and len(sys.argv) > 2:
            results = searcher.search_by_host(' '.join(sys.argv[2:]))
            for ep in results:
                print(f"{ep['air_date']} - {ep['episode_id']}")
        else:
            print("Usage: python search.py [stats|year YYYY|host NAME]")
            print("   Or: python search.py (for interactive mode)")
    else:
        # Interactive mode
        try:
            searcher = DatasetSearcher()
            searcher.interactive_search()
        except KeyboardInterrupt:
            print("\n\n⚠️  Cancelled by user.")
            sys.exit(0)


if __name__ == "__main__":
    main()

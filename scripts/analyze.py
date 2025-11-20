#!/usr/bin/env python3
"""
Analysis script for Headbangers Ball dataset.
Generates statistics and insights from the data.
"""

import csv
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple


class DataAnalyzer:
    """Analyzes Headbangers Ball dataset."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.episodes = []
        self.videos = []

    def load_data(self):
        """Load CSV data files."""
        print("Loading data...")

        # Load episodes
        episodes_file = self.data_dir / "episodes.csv"
        if episodes_file.exists():
            with open(episodes_file, 'r', encoding='utf-8') as f:
                self.episodes = list(csv.DictReader(f))
                # Filter out header-only rows
                self.episodes = [e for e in self.episodes if e.get('episode_id')]

        # Load videos
        videos_file = self.data_dir / "videos.csv"
        if videos_file.exists():
            with open(videos_file, 'r', encoding='utf-8') as f:
                self.videos = list(csv.DictReader(f))
                # Filter out header-only rows
                self.videos = [v for v in self.videos if v.get('video_id')]

        print(f"  Loaded {len(self.episodes)} episodes")
        print(f"  Loaded {len(self.videos)} videos")

    def analyze_timeline(self):
        """Analyze episode timeline."""
        print("\n" + "="*60)
        print("Timeline Analysis")
        print("="*60)

        if not self.episodes:
            print("No episode data available.")
            return

        # Get date range
        dates = [e['air_date'] for e in self.episodes if e.get('air_date')]
        if dates:
            dates.sort()
            print(f"\nFirst episode: {dates[0]}")
            print(f"Last episode:  {dates[-1]}")

            # Calculate span
            first = datetime.strptime(dates[0], '%Y-%m-%d')
            last = datetime.strptime(dates[-1], '%Y-%m-%d')
            span_days = (last - first).days
            span_years = span_days / 365.25

            print(f"Total span:    {span_days} days ({span_years:.1f} years)")
            print(f"Total episodes documented: {len(self.episodes)}")

    def analyze_hosts(self):
        """Analyze host distribution."""
        print("\n" + "="*60)
        print("Host Analysis")
        print("="*60)

        if not self.episodes:
            print("No episode data available.")
            return

        host_counts = Counter(e['host'] for e in self.episodes if e.get('host'))

        print(f"\nTotal unique hosts: {len(host_counts)}")
        print("\nEpisodes per host:")
        for host, count in host_counts.most_common():
            percentage = (count / len(self.episodes)) * 100
            print(f"  {host:30} {count:4} episodes ({percentage:5.1f}%)")

    def analyze_eras(self):
        """Analyze different eras of the show."""
        print("\n" + "="*60)
        print("Era Analysis")
        print("="*60)

        if not self.episodes:
            print("No episode data available.")
            return

        era_counts = Counter(e['era'] for e in self.episodes if e.get('era'))

        print(f"\nTotal eras: {len(era_counts)}")
        print("\nEpisodes per era:")
        for era, count in era_counts.most_common():
            percentage = (count / len(self.episodes)) * 100
            print(f"  {era:30} {count:4} episodes ({percentage:5.1f}%)")

    def analyze_artists(self):
        """Analyze most featured artists."""
        print("\n" + "="*60)
        print("Artist Analysis")
        print("="*60)

        if not self.videos:
            print("No video data available.")
            return

        artist_counts = Counter(v['artist'] for v in self.videos if v.get('artist'))

        print(f"\nTotal unique artists: {len(artist_counts)}")
        print(f"Total videos: {len(self.videos)}")
        print("\nTop 20 Most Featured Artists:")
        for i, (artist, count) in enumerate(artist_counts.most_common(20), 1):
            print(f"  {i:2}. {artist:40} {count:4} videos")

    def analyze_genres(self):
        """Analyze genre distribution."""
        print("\n" + "="*60)
        print("Genre Analysis")
        print("="*60)

        if not self.videos:
            print("No video data available.")
            return

        genre_counts = Counter(v['genre'] for v in self.videos if v.get('genre'))

        if not genre_counts:
            print("No genre data available.")
            return

        print(f"\nTotal unique genres: {len(genre_counts)}")
        print("\nVideos per genre:")
        for genre, count in genre_counts.most_common():
            percentage = (count / len(self.videos)) * 100
            print(f"  {genre:30} {count:4} videos ({percentage:5.1f}%)")

    def analyze_by_year(self):
        """Analyze videos and episodes by year."""
        print("\n" + "="*60)
        print("Year-by-Year Analysis")
        print("="*60)

        if not self.episodes:
            print("No episode data available.")
            return

        # Count episodes by year
        year_counts = defaultdict(int)
        for episode in self.episodes:
            if episode.get('air_date'):
                year = episode['air_date'][:4]
                year_counts[year] += 1

        print("\nEpisodes per year:")
        for year in sorted(year_counts.keys()):
            count = year_counts[year]
            print(f"  {year}: {count:3} episodes")

    def generate_statistics_report(self, output_file: str = None):
        """Generate comprehensive statistics report."""
        print("\n" + "="*60)
        print("Headbangers Ball Dataset Analysis Report")
        print("="*60)

        self.load_data()
        self.analyze_timeline()
        self.analyze_hosts()
        self.analyze_eras()
        self.analyze_by_year()
        self.analyze_artists()
        self.analyze_genres()

        print("\n" + "="*60)
        print("Analysis Complete")
        print("="*60 + "\n")


def main():
    """Main entry point."""
    analyzer = DataAnalyzer()
    analyzer.generate_statistics_report()


if __name__ == "__main__":
    main()

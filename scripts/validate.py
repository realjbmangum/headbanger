#!/usr/bin/env python3
"""
Validation script for Headbangers Ball dataset.
Checks data integrity, format compliance, and cross-references.
"""

import csv
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set, Tuple


class DataValidator:
    """Validates Headbangers Ball dataset files."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.episode_ids: Set[str] = set()

    def validate_date(self, date_str: str, field_name: str, row_num: int) -> bool:
        """Validate date format YYYY-MM-DD."""
        if not date_str:
            return True  # Empty dates are allowed

        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_str):
            self.errors.append(
                f"Row {row_num}, {field_name}: Invalid date format '{date_str}'. "
                f"Expected YYYY-MM-DD"
            )
            return False

        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            self.errors.append(
                f"Row {row_num}, {field_name}: Invalid date '{date_str}'. "
                f"Date does not exist"
            )
            return False

    def validate_episodes(self) -> bool:
        """Validate episodes.csv file."""
        print("Validating episodes.csv...")
        filepath = self.data_dir / "episodes.csv"

        if not filepath.exists():
            self.errors.append(f"File not found: {filepath}")
            return False

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            required_fields = ['episode_id', 'air_date', 'host', 'source_citations']
            if not all(field in reader.fieldnames for field in required_fields):
                self.errors.append(
                    f"episodes.csv missing required fields. "
                    f"Expected: {required_fields}"
                )
                return False

            for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
                episode_id = row['episode_id']

                # Check for duplicate episode IDs
                if episode_id:
                    if episode_id in self.episode_ids:
                        self.errors.append(
                            f"Row {row_num}: Duplicate episode_id '{episode_id}'"
                        )
                    else:
                        self.episode_ids.add(episode_id)

                # Validate date
                self.validate_date(row['air_date'], 'air_date', row_num)

                # Check for missing citations
                if not row['source_citations']:
                    self.warnings.append(
                        f"Row {row_num}: Missing source_citations for episode {episode_id}"
                    )

                # Check for missing host
                if not row['host']:
                    self.warnings.append(
                        f"Row {row_num}: Missing host for episode {episode_id}"
                    )

        print(f"  ✓ Validated {len(self.episode_ids)} episodes")
        return True

    def validate_videos(self) -> bool:
        """Validate videos.csv file."""
        print("Validating videos.csv...")
        filepath = self.data_dir / "videos.csv"

        if not filepath.exists():
            self.errors.append(f"File not found: {filepath}")
            return False

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            required_fields = ['video_id', 'episode_id', 'artist', 'song_title', 'source_citations']
            if not all(field in reader.fieldnames for field in required_fields):
                self.errors.append(
                    f"videos.csv missing required fields. Expected: {required_fields}"
                )
                return False

            video_ids = set()
            video_count = 0

            for row_num, row in enumerate(reader, start=2):
                video_id = row['video_id']
                episode_id = row['episode_id']

                video_count += 1

                # Check for duplicate video IDs
                if video_id:
                    if video_id in video_ids:
                        self.errors.append(
                            f"Row {row_num}: Duplicate video_id '{video_id}'"
                        )
                    else:
                        video_ids.add(video_id)

                # Check episode_id cross-reference
                if episode_id and episode_id not in self.episode_ids:
                    self.errors.append(
                        f"Row {row_num}: episode_id '{episode_id}' not found in episodes.csv"
                    )

                # Validate date if present
                if row.get('air_date'):
                    self.validate_date(row['air_date'], 'air_date', row_num)

                # Check required fields
                if not row['artist']:
                    self.warnings.append(
                        f"Row {row_num}: Missing artist for video {video_id}"
                    )

                if not row['song_title']:
                    self.warnings.append(
                        f"Row {row_num}: Missing song_title for video {video_id}"
                    )

                if not row['source_citations']:
                    self.warnings.append(
                        f"Row {row_num}: Missing source_citations for video {video_id}"
                    )

        print(f"  ✓ Validated {video_count} videos")
        return True

    def validate_hosts(self) -> bool:
        """Validate hosts.csv file."""
        print("Validating hosts.csv...")
        filepath = self.data_dir / "hosts.csv"

        if not filepath.exists():
            self.warnings.append(f"File not found: {filepath}")
            return True  # Not critical

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            host_count = 0

            for row_num, row in enumerate(reader, start=2):
                host_count += 1

                # Validate dates
                if row.get('start_date'):
                    self.validate_date(row['start_date'], 'start_date', row_num)
                if row.get('end_date'):
                    self.validate_date(row['end_date'], 'end_date', row_num)

        print(f"  ✓ Validated {host_count} hosts")
        return True

    def validate_special_segments(self) -> bool:
        """Validate special_segments.csv file."""
        print("Validating special_segments.csv...")
        filepath = self.data_dir / "special_segments.csv"

        if not filepath.exists():
            self.warnings.append(f"File not found: {filepath}")
            return True  # Not critical

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            segment_count = 0

            for row_num, row in enumerate(reader, start=2):
                segment_count += 1
                episode_id = row.get('episode_id')

                # Check episode_id cross-reference
                if episode_id and episode_id not in self.episode_ids:
                    self.errors.append(
                        f"Row {row_num}: episode_id '{episode_id}' not found in episodes.csv"
                    )

                # Validate date
                if row.get('air_date'):
                    self.validate_date(row['air_date'], 'air_date', row_num)

        print(f"  ✓ Validated {segment_count} special segments")
        return True

    def run_all_validations(self) -> bool:
        """Run all validation checks."""
        print("\n" + "="*60)
        print("Headbangers Ball Dataset Validation")
        print("="*60 + "\n")

        # Validate each file
        self.validate_episodes()
        self.validate_videos()
        self.validate_hosts()
        self.validate_special_segments()

        # Report results
        print("\n" + "="*60)
        print("Validation Results")
        print("="*60)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors and not self.warnings:
            print("\n✅ All validations passed! Dataset is clean.")
        elif not self.errors:
            print(f"\n✅ No errors found. {len(self.warnings)} warnings to review.")
        else:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s).")

        print("\n" + "="*60 + "\n")

        return len(self.errors) == 0


def main():
    """Main entry point."""
    validator = DataValidator()
    success = validator.run_all_validations()

    # Exit with appropriate code
    exit(0 if success else 1)


if __name__ == "__main__":
    main()

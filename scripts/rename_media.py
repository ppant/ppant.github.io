#!/usr/bin/env python3
"""
Rename photos and videos in chronological order.

Example:

python rename_media.py \
    --folder ~/Pictures/Bison2026 \
    --prefix bison-2026

python rename_media.py \
    --folder ~/Pictures/Bison2026 \
    --prefix bison-2026 \
    --dry-run
"""

import argparse
import os
from pathlib import Path
from datetime import datetime

from PIL import Image, ExifTags

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except:
    pass


PHOTO_EXT = {".jpg", ".jpeg", ".png", ".heic"}
VIDEO_EXT = {".mp4", ".mov", ".avi", ".m4v"}


import subprocess
from datetime import datetime


def exiftool_datetime(path):
    """
    Read capture time using ExifTool.
    Works for both photos and videos.
    Falls back to file modification time.
    """
    tags = [
        "DateTimeOriginal",
        "CreateDate",
        "MediaCreateDate",
        "TrackCreateDate",
        "CreationDate",
    ]

    for tag in tags:
        try:
            result = subprocess.run(
                [
                    "exiftool",
                    "-s3",
                    f"-{tag}",
                    str(path),
                ],
                capture_output=True,
                text=True,
            )

            value = result.stdout.strip()

            if value:
                return datetime.strptime(
                    value[:19],
                    "%Y:%m:%d %H:%M:%S"
                )

        except Exception:
            pass

    # fallback
    return datetime.fromtimestamp(path.stat().st_mtime)


def exif_datetime(path):

    return exiftool_datetime(path)

def video_datetime(path):

    return exiftool_datetime(path)


def video_datetime(path):
    """
    Uses modified time for videos.
    """
    return datetime.fromtimestamp(path.stat().st_mtime)


def collect_files(folder):

    photos = []
    videos = []

    for f in folder.iterdir():

        if not f.is_file():
            continue

        ext = f.suffix.lower()

        if ext in PHOTO_EXT:
            photos.append((exif_datetime(f), f))

        elif ext in VIDEO_EXT:
            videos.append((video_datetime(f), f))

    photos.sort(key=lambda x: x[0])
    videos.sort(key=lambda x: x[0])

    return photos, videos


def safe_rename(items, prefix, kind, dry_run):

    mapping = []

    for idx, (_, old) in enumerate(items, start=1):

        new_name = f"{prefix}-{kind}-{idx:02d}{old.suffix.lower()}"
        new_path = old.parent / new_name

        if new_path.exists() and new_path != old:
            raise RuntimeError(f"{new_name} already exists.")

        mapping.append((old, new_path))

    if dry_run:
        print("\n==========================")
        print(f"{kind.upper()}S")
        print("==========================")

        for old, new in mapping:
            print(f"{old.name}")
            print(f"  -> {new.name}")

    else:

        # temporary rename first
        temp = []

        for old, _ in mapping:
            tmp = old.with_suffix(old.suffix + ".tmprename")
            old.rename(tmp)
            temp.append(tmp)

        for tmp, (_, new) in zip(temp, mapping):
            tmp.rename(new)

    return mapping


def generate_markdown(folder, prefix, photos):

    outfile = folder / "media.md"

    with open(outfile, "w") as f:

        f.write("# Photos\n\n")

        for _, new in photos:

            f.write(
                f'![](/data/images/running/bison_ultra_2026/{new.name})'
                '{:width="800px"}\n\n'
            )

    print(f"\nMarkdown written to {outfile}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--folder",
        required=True,
        help="Folder containing media"
    )

    parser.add_argument(
        "--prefix",
        required=True,
        help="Example: bison-2026"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true"
    )

    args = parser.parse_args()

    folder = Path(args.folder).expanduser()

    photos, videos = collect_files(folder)

    print(f"\nFound {len(photos)} photos")
    print(f"Found {len(videos)} videos")

    photo_mapping = safe_rename(
        photos,
        args.prefix,
        "pic",
        args.dry_run
    )

    video_mapping = safe_rename(
        videos,
        args.prefix,
        "video",
        args.dry_run
    )

    if not args.dry_run:
        generate_markdown(folder, args.prefix, photo_mapping)

        print("\nDone!")


if __name__ == "__main__":
    main()
# Rename Media Utility

A small Python utility to rename photos and videos in chronological order.

The script:

- Renames photos and videos separately
- Sorts files using their original capture time (via ExifTool)
- Generates sequential file names
- Creates a `media.md` file containing Markdown image links for the blog
- Supports a dry-run mode to preview changes

---

## Prerequisites

### Install ExifTool (macOS)

```bash
brew install exiftool
```

### Install Python dependency

```bash
pip install pillow pillow-heif
```

---

## Folder Structure

Example:

```
BisonUltra2026/
│
├── IMG_1234.JPG
├── IMG_1235.HEIC
├── IMG_1236.JPG
├── VID_0001.MOV
├── VID_0002.MP4
└── ...
```

---

## Dry Run (Recommended)

Preview the renaming without making any changes.

```bash
python rename_media.py \
    --folder "~/Pictures/Bison Ultra 2026 \ blog upload"
    --prefix bison-2026 \
    --dry-run
```

Example output:

```
Found 87 photos
Found 19 videos

IMG_1234.JPG
  -> bison-2026-pic-01.jpg

IMG_1235.HEIC
  -> bison-2026-pic-02.heic

VID_0001.MOV
  -> bison-2026-video-01.mov
```

---

## Rename Files

Once you're happy with the preview:

```bash
python rename_media.py \
    --folder ~/Pictures/BisonUltra2026 \
    --prefix bison-2026
```

The files will be renamed in place.

---

## Output

Example:

```
bison-2026-pic-01.jpg
bison-2026-pic-02.heic
bison-2026-pic-03.jpg

bison-2026-video-01.mov
bison-2026-video-02.mp4
```

A Markdown file will also be generated:

```
media.md
```

Example:

```markdown
# Photos

![](/data/images/running/bison_ultra_2026/bison-2026-pic-01.jpg){:width="800px"}

![](/data/images/running/bison_ultra_2026/bison-2026-pic-02.heic){:width="800px"}

![](/data/images/running/bison_ultra_2026/bison-2026-pic-03.jpg){:width="800px"}
```

---

## Notes

- Photos are ordered by their original capture time.
- Videos are also ordered using their embedded creation time (via ExifTool).
- Existing files are never overwritten.
- Always run with `--dry-run` first to verify the sequence.
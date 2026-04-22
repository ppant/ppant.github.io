import os
import re

POSTS_DIR = "_posts"

def add_permalink(filepath, filename):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "permalink:" in content:
        return False
    
    # Extract date and slug from filename e.g. 2022-04-16-ootyultra_2022_experience.md
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})-(.+)\.md$', filename)
    if not match:
        return False
    
    year, month, day, slug = match.groups()
    permalink = f"/{year}/{month}/{day}/{slug}/"
    
    # Insert after layout: line if exists, else after date: line
    if "layout:" in content:
        content = re.sub(
            r'(layout:\s*\S+)',
            r'\1\npermalink: ' + permalink,
            content, count=1
        )
    elif "date:" in content:
        content = re.sub(
            r'(date:\s*\S+)',
            r'\1\npermalink: ' + permalink,
            content, count=1
        )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True

count = 0
for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "permalink:" in content:
        continue
    if add_permalink(fpath, fname):
        count += 1
        print(f"Added permalink to {fname}")

print(f"\nDone! Updated {count} posts.")

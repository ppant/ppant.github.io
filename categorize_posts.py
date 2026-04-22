import os
import re

POSTS_DIR = "_posts"

RULES = [
    # Community running events (most specific first)
    (["parikrama", "nag-mandir", "nag_devta"], "[community, running]"),

    # Running (sport) - be specific to avoid false positives
    (["ultra", "trail", "malnad", "bison-ultra",
      "ooty-ultra", "ootyultra", "run-diary", "run_diary",
      "race-report", "trail-run"], "[running]"),

    # Fitness
    (["cycling", "health", "fitness"], "[fitness]"),

    # Travel
    (["travel", "trip", "kumaon", "himaliya",
      "bitosa"], "[travel]"),

    # AI/ML (before tech to catch ML topics)
    (["machine-learning", "deep-learning", "tensorflow",
      "neural-network", "fastai", "cnn-understanding",
      "choropleth", "r-programming", "getting-and-cleaning",
      "interesting-machine", "deep_learning", "process_mining",
      "explainable", "concept-drift", "data_science",
      "data-science", "moocs", "nptel", "stanford-db",
      "online-ai", "ai-class", "image-classification",
      "prognostic", "predictive", "notes-mi-class",
      "data_science_in_india", "data_science_in_iot",
      "tips-to-learn-machine"], "[ai-ml]"),

    # Life/Reflections
    (["new-year", "wishes", "happy-new", "wfh",
      "feynman", "outliers", "expiry-and-revive",
      "12-years-of-tech", "summary_of",
      "why_am_i_doing_phd", "project-365",
      "new-coder", "learning_using_anki",
      "one-of-my-fav-chess",
      "future-of-how_we_learning",
      "books-recommendation-series-hands-on",
      "hacker-interviews"], "[life]"),

    # Books/Podcasts
    (["book", "books-recommendation", "podcast",
      "recommendation", "perl-weekly",
      "impatient-perl"], "[life]"),

    # Tech — everything else
    (["perl", "cpan", "mojomojo", "moose", "catalyst",
      "dancer", "pdl", "rakudo", "puremvc", "schwartzian",
      "backtracking", "grep-and-map", "data-serialization",
      "pdf-creation", "python", "implemeting-data",
      "data-structures-and-algorithms", "recursion",
      "sorting", "graphs", "git", "postgresql", "hadoop",
      "sqoop", "elasticsearch", "spacevim", "apache",
      "linux", "centos", "fonts", "wkhtmltopdf", "webdav",
      "http-2", "ajax", "javascript", "jquery", "jsx",
      "reactjs", "gatsby", "debugging", "firefox",
      "microsoft-edge", "snmpv3", "design-pattern",
      "philosophy-and-software", "singleton", "phrasebook",
      "orm", "architecture", "restfull",
      "web-development-lamp", "decoupled-content",
      "static-blog", "julia", "c_and_modern",
      "moving-from-wordpress"], "[tech]"),
]

DEFAULT = "[tech]"

def get_category(filename):
    fname = filename.lower()
    for keywords, category in RULES:
        for kw in keywords:
            if kw in fname:
                return category
    return DEFAULT

def add_category(filepath, category):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "categories:" in content:
        return False
    if "layout:" in content:
        content = re.sub(
            r'(layout:\s*\S+)',
            r'\1\ncategories: ' + category,
            content, count=1
        )
    elif "date:" in content:
        content = re.sub(
            r'(date:\s*\S+)',
            r'\1\ncategories: ' + category,
            content, count=1
        )
    else:
        content = content.replace("---\n", "---\ncategories: " + category + "\n", 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True

changes = []
for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith(".md"):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if "categories:" in content:
        continue
    category = get_category(fname)
    changes.append((fname, category))

print(f"\nFound {len(changes)} posts to categorize:\n")
for fname, cat in changes:
    print(f"  {cat:25s} {fname}")

print(f"\nTotal: {len(changes)} posts")
confirm = input("\nApply changes? (yes/no): ")
if confirm.strip().lower() == "yes":
    count = 0
    for fname, cat in changes:
        fpath = os.path.join(POSTS_DIR, fname)
        if add_category(fpath, cat):
            count += 1
    print(f"\nDone! Updated {count} posts.")
else:
    print("Aborted. No changes made.")

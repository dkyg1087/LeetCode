import os
import json

TAGS_JSON_PATH = "tags/json/tags.json"
TAG_PAGES_DIR = "tags/Tag-Pages"
INDEX_MD_PATH = "tags/index.md"

# Ensure tag_pages/ exists
os.makedirs(TAG_PAGES_DIR, exist_ok=True)

# Load tags
with open(TAGS_JSON_PATH, "r") as f:
    tags = json.load(f)

tags = tags["tags"]

# Create individual tag pages
for tag in tags:
    tag_slug = tag.lower().replace(" ", "_")
    filename = f"{tag_slug}.md"
    filepath = os.path.join(TAG_PAGES_DIR, filename)

    display_name = tag.title().replace("_", " ")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {display_name}\n\n")
        f.write(f"**0 problems with this tag.**\n\n")
        f.write("### Problems\n\n")

    print(f"Created: {filepath}")

# Create tag index page
with open(INDEX_MD_PATH, "w", encoding="utf-8") as f:
    f.write("# Tags Index\n\n")
    for tag in sorted(tags):
        slug = tag.lower().replace(" ", "_") + ".md"
        f.write(f"- [{tag.title().replace('_', ' ')}](Tag-Pages/{slug})\n")

print(f"Index created at: {INDEX_MD_PATH}")

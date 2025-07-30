import re
from pathlib import Path

def update_tag_md(tag, title, path):
    tag_file = Path(f'Tags/Tag-Pages/{tag}.md')

    if not tag_file.exists():
        raise FileNotFoundError(f"{tag_file} not found.")

    content = tag_file.read_text(encoding='utf-8')
    lines = content.splitlines()

    # --- Step 1: Update problem count ---
    count_pattern = r"\*\*(\d+) problems with this tag\.\*\*"
    match = re.search(count_pattern, content)
    if not match:
        raise ValueError("Problem count line not found.")

    current_count = int(match.group(1))
    new_count = current_count + 1

    content = re.sub(
        count_pattern,
        f"**{new_count} problems with this tag.**",
        content
    )
    lines = content.splitlines()

    # --- Step 2: Find where to insert the new problem ---
    try:
        start_index = lines.index("### Problems") + 1
    except ValueError:
        raise ValueError("Missing '### Problems' section.")

    new_line = f"- [{title}]({path})"
    title_match = re.match(r"^(\d+)[._]", title.strip())
    if not title_match:
        raise ValueError(f"Cannot extract problem number from title: {title}")
    new_problem_number = int(title_match.group(1))
    
    # Duplicate check by problem number
    existing_ids = {
        int(re.search(r"- \[(\d+)", line).group(1))
        for line in lines if line.startswith("- [")
    }

    if new_problem_number in existing_ids:
        print(f"⚠️ Duplicate found: {title} already exists in tags/{tag}.md")
        return

    inserted = False
    for i in range(start_index, len(lines)):
        line = lines[i]
        match = re.match(r"- \[(\d+)", line)
        if match:
            existing_number = int(match.group(1))
            if new_problem_number < existing_number:
                lines.insert(i, new_line)
                inserted = True
                break

    if not inserted:
        lines.append(new_line)

    # --- Step 3: Write back the file ---
    tag_file.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"✅ Added: {title} to Tags/Tag-Pages/{tag}.md")

def update_readme_md(readme_path="README.md"):
    readme = Path(readme_path)

    if not readme.exists():
        raise FileNotFoundError(f"{readme_path} not found.")

    content = readme.read_text(encoding="utf-8")

    # Match the current count
    pattern = r"\*\*Total Problems Solved: (\d+)\*\*"
    match = re.search(pattern, content)
    
    if not match:
        raise ValueError("Could not find the 'Total Problems Solved' line.")

    current_count = int(match.group(1))
    new_count = current_count + 1

    # Replace the line with the updated count
    updated_content = re.sub(
        pattern,
        f"**Total Problems Solved: {new_count}**",
        content
    )

    readme.write_text(updated_content,encoding='utf-8')
    print(f"Updated problem count: {new_count}")


if __name__ == "__main__":
    update_tag_md("array","14. Two Sum", "../../Problems/14_Two_Sum.py")
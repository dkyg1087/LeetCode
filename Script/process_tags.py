import os
import json
from shutil import move
from pathlib import Path

from update_problem_tags import update_problem_tags
from call_llm import call_ollama
from update_md import update_tag_md,update_readme_md


# RAW_DIR = Path("Raw")
# PROBLEM_DIR = Path("Problems")
# TAGS_DIR = Path("Tags")
# SCRIPTS_DIR = Path("Scripts")
# TAGS_INDEX_FILE = TAGS_DIR / "index.md"
# README_FILE = Path("README.md")
# TAGS_JSON_FILE = Path("Tags/json/tags.json")
# PROBLEM_TAGS_FILE = Path("problem_tags.json")
# OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
# MODEL_NAME = "gemma3:12b"


def standardize_filename(filename):
    name, ext = os.path.splitext(filename)
    new_name = name.replace(". ", "_").replace(" ", "_").replace(".", "_")
    return f"{new_name}{ext}"
    
def load_tags():
    TAGS_DIR = Path("Tags")
    TAGS_JSON_FILE = TAGS_DIR / "json/tags.json"
    with open(TAGS_JSON_FILE) as f:
        return json.load(f)["tags"]

def main():
    
    RAW_DIR = Path("Raw")
    PROBLEM_DIR = Path("Problems")
    tags = load_tags()
    
    for filename in os.listdir(RAW_DIR):
        if not filename.endswith(".py"):
            continue
        old_path = os.path.join(RAW_DIR, filename)
        new_filename = standardize_filename(filename)
        new_path = os.path.join(RAW_DIR, new_filename)
        if new_filename == filename or os.path.exists(new_path):
            print(f"[SKIP] Already standardized/exists: {filename}")
        else:
            os.rename(old_path, new_path)
            print(f"[RENAME] {filename} → {new_filename}")
        
        with open(new_path,"r",encoding="utf-8") as f:
            content = f.read()
        
        tags_pred = call_ollama(new_filename.replace(".py", ""), content, tags)
        for i in range(len(tags_pred)):
            if tags_pred[i] not in tags:
                tags_pred[i] = "other"

        update_problem_tags(new_filename, tags_pred)
        move(RAW_DIR / new_filename, PROBLEM_DIR / new_filename)
        for tag in tags_pred:
            update_tag_md(tag,filename.replace(".py", ""), "../.."/PROBLEM_DIR / new_filename)
        update_readme_md()
        
if __name__ == "__main__":
    main()

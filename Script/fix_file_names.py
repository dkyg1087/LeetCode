import os

RAW_DIR = "Raw"
    
def standardize_filename_simple(filename):
    if not filename.endswith(".py"):
        return None
    name, ext = os.path.splitext(filename)
    new_name = name.replace(". ", "_").replace(" ", "_").replace(".", "_")
    return f"{new_name}{ext}"

def standardize_all_raw_files():
    for filename in os.listdir(RAW_DIR):
        old_path = os.path.join(RAW_DIR, filename)
        if not os.path.isfile(old_path) or not filename.endswith(".py"):
            continue

        new_filename = standardize_filename_simple(filename)
        if new_filename == filename:
            print(f"[SKIP] Already standardized: {filename}")
            continue

        new_path = os.path.join(RAW_DIR, new_filename)
        os.rename(old_path, new_path)
        print(f"[RENAME] {filename} → {new_filename}")

if __name__ == "__main__":
    standardize_all_raw_files()

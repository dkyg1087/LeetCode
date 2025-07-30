import json
import re


def update_problem_tags(filename, pred_tags,FILE_PATH="Tags/json/problem_tags.json"):
    def extract_number(filename):
        match = re.match(r"(\d+)_", filename)
        return int(match.group(1)) if match else float('inf')
    
    try:
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Convert to list of (key, value) pairs for ordered insertion
    items = list(data.items())
    new_num = extract_number(filename)

    # Linear insert to maintain order
    inserted = False
    for i, (title, _) in enumerate(items):
        if new_num < extract_number(title):
            items.insert(i, (filename, pred_tags))
            inserted = True
            break
    
    if not inserted:
        items.append((filename, pred_tags))

    # Convert back to dict (order-preserving since Python 3.7)
    ordered_data = dict(items)

    # Save the updated data
    with open(FILE_PATH, 'w') as f:
        json.dump(ordered_data, f, indent=4)


if __name__ == "__main__":
    update_problem_tags("12222_Example_Problem.py", ["example", "problem"])
import json
import os

def load_json(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_new_id(data_list):
    if not data_list:
        return 1
    return max(item["id"] for item in data_list) + 1
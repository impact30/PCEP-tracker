import json
import os
from datetime import date
from checklist import CHECKLIST_SECTIONS

def init_file(path):
    data = {
        "start_date": date.today().isoformat(),
        "end_date": date.today().isoformat(),
        "sections": []
    }

    for section in CHECKLIST_SECTIONS:
        data["sections"].append({
            "name": section["name"],
            "items": [{"text": item, "done": False} for item in section["items"]]
        })

    save_data(path, data)
    return data


def load_data(path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return init_file(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

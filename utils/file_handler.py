import json
import os

DATA_FILE = "data/users.json" 

def load_users():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

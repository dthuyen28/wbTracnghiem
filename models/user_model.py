import json

USER_FILE = "data/users.json"

def load_users():
    with open(USER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def is_email_exists(email):
    users = load_users()
    return any(user["email"] == email for user in users)

def add_user(user):
    users = load_users()
    user["id"] = len(users) + 1
    users.append(user)
    save_users(users)


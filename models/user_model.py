from utils.file_handler import load_json, save_json
import json
import os

USER_FILE = "data/users.json"
FILE = "data/users.json"

def get_all_users():
    return load_json(USER_FILE)
def is_email_exists(email):
    users = get_all_users()
    return any(u["email"] == email for u in users)
def add_user(fullname, email, password):
    users = get_all_users()
    new_user = {
        "id": len(users) + 1,
        "fullname": fullname,
        "email": email,
        "password": password,
        "role": "student"
    }
    users.append(new_user)
    save_json(USER_FILE, users)
def check_login(email, password):
    users = load_json(FILE)
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user
    return None



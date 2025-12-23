from utils.file_handler import load_json

FILE = "data/users.json"

def check_login(email, password):
    users = load_json(FILE)
    for user in users:
        if user['email'] == email and user['password'] == password:
            return user
    return None

import json
import os

def create_user_id(user_name: str) -> str:
    return user_name.lower().strip()

def save_user_id(user_id: str) -> None:
    data = {"user_id": user_id}

    with open("user_profile.json", "w") as f:   
        json.dump(data, f, indent=4)

def load_user_id() -> str:
    if os.path.isfile("user_profile.json"):
        data = json.load(open("user_profile.json"))
        return data["user_id"]
    return None
    
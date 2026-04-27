from data_classes import UserProfilePayload
from extract_config import create_user_id
import json
import os

class User:
    def __init__(self, user_id):
        self.name = ""
        self.id = user_id
        self.subject_of_interest = ""
        self.skill_level = ""
    
    def updatePlayerClass(self, data: UserProfilePayload) -> None:
        """Although this function is impure, it is initialization logic, which is unavoidable for this system."""
        self.name = data.user_name
        self.user_id = data.user_id
        self.subject_of_interest = data.user_subject
        self.skill_level = data.user_skill_level

class UserProfileHandler:
    def __init__(self, user_id: User):
        self.user_id = user_id
        self.user_name = ""
        self.session_id = ""
        self.subject_of_interest = ""
        self.skill_level = ""
    
    def user_first_chat(self) -> UserProfilePayload:
        """This is the first function to collect initial user information on the user's first chat interaction. Think of it like an onboarding."""
        print("\n==== FIRST WE NEED SOME INFORMATION ====\n")
        user_name = input("What is your name?: ")
        user_subject = input("What is your subject of interest?: ")
        user_skill_level = input("What is your skill level (ie. beginner, intermediate, advanced): ")

        return UserProfilePayload(
            user_name=user_name,
            user_id=create_user_id(user_name),
            user_subject=user_subject, 
            user_skill_level=user_skill_level
        )

    def save_user_profile(self, user_id: str, player_data: UserProfilePayload) -> None:
        """This function collects the consistent user data. It does NOT collect state information"""  
        data = {
            "user_name": player_data.user_name,
            "user_id": player_data.user_id,
            "user_subject": player_data.user_subject,
            "user_skill_level": player_data.user_skill_level
        }

        filepath = f"user_profiles/{data["user_id"]})_profile.json"

        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_user_data(self, user_id) -> UserProfilePayload:
        """This function does NOT load state. We only load the consistent information from here."""
        filepath = f"user_profiles/{user_id}_profile.json"
        if not os.path.isfile(filepath):
            raise RuntimeWarning(f"Warning: {filepath} does not exist! Please save first memory.")
        
        with open(filepath, "r") as f:
            data = json.load(f)
        
        return UserProfilePayload(
            user_name=data["user_name"],
            user_id=data["user_id"],
            user_subject=data["user_subject"], 
            user_skill_level=data["user_skill_level"], 
        )

        
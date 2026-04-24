from data_classes import UserProfilePayload
from user import User 
import json
import os

class UserProfile:
    def __init__(self, user: User):
        self.user = user
    
    @property
    def filepath_user_profile(self) -> str:
        return f"memory_files/user_data/{self.user.name}_profile.json"
    
    def user_first_chat(self) -> UserProfilePayload:
        """This is the first function to collect initial user information on the user's first chat interaction. Think of it like an onboarding."""
        print("\n==== FIRST WE NEED SOME INFORMATION ====\n")
        user_name = input("What is your name?: ")
        user_subject = input("What is your subject of interest?: ")
        user_skill_level = input("What is your skill level (ie. beginner, intermediate, advanced): ")

        return UserProfilePayload(
            user_name=user_name, 
            user_subject=user_subject, 
            user_skill_level=user_skill_level
        )

    def save_user_profile(self, player_data: UserProfilePayload) -> None:
        """This function collects the consistent user data. It does NOT collect state information"""  
        data = {
            "user_name": player_data.user_name,
            "user_subject": player_data.user_subject,
            "user_skill_level": player_data.user_skill_level
        }

        if not os.path.exists(self.filepath_user_profile):
            os.makedirs(os.path.dirname(self.filepath_user_profile), exist_ok=True)
        
        with open(self.filepath_user_profile, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_user_data(self) -> UserProfilePayload:
        """This function does NOT load state. We only load the consistent information from here."""
        if not os.path.exists(self.filepath_user_profile):
            raise RuntimeWarning(f"Warning: {self.filepath_user_profile} does not exist! Please save first memory.")
        
        with open(self.filepath_user_profile, "r") as f:
            data = json.load(f)
        
        return UserProfilePayload(
            user_name=data["user_name"], 
            user_subject=data["user_subject"], 
            user_skill_level=data["user_skill_level"], 
        )

        
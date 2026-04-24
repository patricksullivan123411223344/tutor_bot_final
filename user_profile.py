from data_classes import UserProfilePayload
from user import User 
import json
import os

class UserProfileHandler:
    def __init__(self, user: User):
        self.user = user
    
    # property helps because instead of passing a stale method, it recomputes each time.
    # originally, the filename was an element of the UserProfile class, but that sets the filename in stone. 
    # what we want is a method of recomputing per user, per name, so instead of passing through a stale method,
    # the name is correctly updated each time.
    @property
    def filepath_user_profile(self) -> str:
        return f"memory_files/user_data/{self.user.user_id}_profile.json"
    
    # this will allow us to take the name inputted, clean it up, and create an actual user_id that is readable and consistent
    # across users. 
    @staticmethod
    def normalize_name(name: str) -> str:
        return name.strip().lower()
    
    def user_first_chat(self) -> UserProfilePayload:
        """This is the first function to collect initial user information on the user's first chat interaction. Think of it like an onboarding."""
        print("\n==== FIRST WE NEED SOME INFORMATION ====\n")
        user_name = input("What is your name?: ")
        user_subject = input("What is your subject of interest?: ")
        user_skill_level = input("What is your skill level (ie. beginner, intermediate, advanced): ")

        return UserProfilePayload(
            user_name=user_name,
            user_id=self.normalize_name(user_name),
            user_subject=user_subject, 
            user_skill_level=user_skill_level
        )

    def save_user_profile(self, player_data: UserProfilePayload) -> None:
        """This function collects the consistent user data. It does NOT collect state information"""  
        data = {
            "user_name": player_data.user_name,
            "user_id": player_data.user_id,
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
            user_id=data["user_id"],
            user_subject=data["user_subject"], 
            user_skill_level=data["user_skill_level"], 
        )

        
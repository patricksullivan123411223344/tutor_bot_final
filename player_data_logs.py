from tutor import UserPayloadStateless, UserPayloadStateful
from user import User 
import json
import os

class PlayerDataHandler:
    def __init__(self, user: User):
        user = user
        self.filepath_pd = f"memory_files/player_data/{user.name}_data.json"
        self.filepath_ps = f"memory_files/player_data/{user.name}_state.json"
    
    def user_first_chat(self) -> UserPayloadStateless:
        """This is the first function to collect initial user information on the user's first chat interaction. Think of it like an onboarding."""
        print("\n==== FIRST WE NEED SOME INFORMATION ====\n")
        user_name = input("What is your name?: ")
        user_subject = input("What is your subject of interest?: ")
        user_skill_level = input("What is your skill level (ie. beginner, intermediate, advanced): ")

        return UserPayloadStateless(
            user_name=user_name, 
            user_subject=user_subject, 
            user_skill_level=user_skill_level
        )

    def save_player_data(self, player_data: UserPayloadStateless) -> None:
        """This function collects the consistent user data. It does NOT collect state information"""  
        data = {
            "user_name": player_data.user_name,
            "user_subject": player_data.user_subject,
            "user_skill_level": player_data.user_skill_level
        }

        if not os.path.exists(self.filepath_pd):
            os.makedirs(os.path.dirname(self.filepath_pd), exist_ok=True)
        
        with open(self.filepath_pd, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_user_data(self) -> UserPayloadStateless:
        """This function does NOT load state. We only load the consistent information from here."""
        if not os.path.exists(self.filepath_pd):
            raise RuntimeWarning(f"Warning: {self.filepath_pd} does not exist! Please save first memory.")
        
        with open(self.filepath_pd, "r") as f:
            data = json.load(f)
        
        return UserPayloadStateless(
            user_name=data["user_name"], 
            user_subject=data["user_subject"], 
            user_skill_level=data["user_skill_level"], 
        )
    
    def save_user_state(self, user_state: UserPayloadStateful) -> None:
        """This function will save the user state based upon the UserPayload data class"""
        data = {
            "user_friction_score": user_state.user_friction_score,
            "user_current_objective": user_state.user_current_objective
        }

        if not os.path.exists(self.filepath_ps):
            os.makedirs(os.path.dirname(self.filepath_ps), exist_ok=True)
        
        with open(self.filepath_ps, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_user_state(self) -> UserPayloadStateful:
        """This function will return the user's state throughout conversation loops"""
        if not os.path.exists(self.filepath_ps):
            raise RuntimeWarning(f"Warning: {self.filepath_ps} does not exist! Please save initial player state.")

        with open(self.filepath_ps, "r") as f:
            data = json.load(f)

        return UserPayloadStateful(
            user_friction_score=data["user_friction_score"],
            user_current_objective=data["user_current_objective"]
        )    

        
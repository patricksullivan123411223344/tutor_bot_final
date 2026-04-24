from data_classes import SessionStatePayload
from user import User
import json
import os

class SessionStateHandler:
    def __init__(self, user: User):
        self.user = user
    
    @property
    def filepath_session_state(self) -> str:
        return f"session_files/{self.user.session_id}_session_state"

    def save_user_state(self, user_state: SessionStatePayload) -> None:
        """This function will save the user state based upon the UserPayload data class"""
        data = {
            "user_friction_score": user_state.user_friction_score,
            "user_current_objective": user_state.user_current_objective
        }

        if not os.path.exists(self.filepath_session_state):
            os.makedirs(os.path.dirname(self.filepath_session_state), exist_ok=True)
        
        with open(self.filepath_session_state, "w") as f:
            json.dump(data, f, indent=4)
    
    def load_user_state(self) -> SessionStatePayload:
        """This function will return the user's state throughout conversation loops"""
        if not os.path.exists(self.filepath_session_state):
            raise RuntimeWarning(f"Warning: {self.filepath_session_state} does not exist! Please save initial player state.")

        with open(self.filepath_session_state, "r") as f:
            data = json.load(f)

        return SessionStatePayload(
            user_friction_score=data["user_friction_score"],
            user_current_objective=data["user_current_objective"]
        )

"""This will hold all during chat logic to be updated and tripped"""
class SessionStateController:
    def __init__(self, user: User):
        self.user = user
    
    def get_friction_score(self, player_message: str) -> SessionStatePayload:
        if "confused" or "don't understand" in player_message:
            friction_score = "<:HIGH:>"
        elif "understand" or "makes sense" in player_message:
            friction_score = "<:LOW:>"
        
        return SessionStatePayload(
            user_friction_score=friction_score
        )
    
    def get_current_objective(self) -> SessionStatePayload:
        objective = input("\nTutor: What's on the schedule for today?")
        return SessionStatePayload(
            user_current_objective=objective
        )


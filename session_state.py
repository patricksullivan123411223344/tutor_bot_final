from data_classes import SessionStatePayload
from user import User
import json
import os

class SessionState:
    def __init__(self, user: User):
        self.user = user
        self.filepath_session_state = f"memory_files/user_data/{user.name}_state.json"
    
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

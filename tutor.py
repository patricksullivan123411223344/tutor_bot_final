import ollama
from user_profile import UserProfileHandler
from session_state import SessionStateHandler
from user import User

class TutorBot:
    def __init__(self, user: User, name: str, model: str):
        self.user = user
        self.name = name
        self.model = model
    
    def build_system_prompt(self) -> str:
        user_handler = UserProfileHandler(self.user).load_user_data()
        session_handler = SessionStateHandler(self.user).load_user_state()

        return f"""
        You are a helpful Computer Science tutor.

        User:
        User Name: {user_handler.user_name}
        User Subject of Interest: {user_handler.user_subject}
        User Skill Level: {user_handler.user_skill_level}

        Session: 
        User Current Objective: {session_handler.user_current_objective}
        User Friction Score: {session_handler.user_friction_score}
        
        Refer to the user by their name. Pay attention to their skill level and their subject of interest.
        """
    
    def respond(self, user_message: str) -> str:

        message = [{"role": "system", "content": self.build_system_prompt()}]
        message.append({"role": "user", "content": user_message})

        response = ollama.chat(
            model = self.model,
            messages = message
        )

        reply = response["message"]["content"].strip()
        return reply



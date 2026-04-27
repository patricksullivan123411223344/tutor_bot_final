import ollama
from user_profile import User, UserProfileHandler
from data_classes import UserProfilePayload

class TutorBot:
    def __init__(self, user: User, name: str, model: str):
        self.name = name
        self.model = model
    
    def build_system_prompt(self, user: User) -> str:
        user_handler = UserProfileHandler.load_user_data(user.id)

        return f"""
        You are a helpful Computer Science tutor.

        User:
        User Name: {user_handler.user_name}
        User Subject of Interest: {user_handler.user_subject}
        User Skill Level: {user_handler.user_skill_level}
        
        Refer to the user by their name. Pay attention to their skill level and their subject of interest.
        """
    
    def respond(self, user: User, user_message: str) -> str:

        message = [{"role": "system", "content": self.build_system_prompt(user)}]
        message.append({"role": "user", "content": user_message})

        response = ollama.chat(
            model = self.model,
            messages = message
        )

        reply = response["message"]["content"].strip()
        return reply



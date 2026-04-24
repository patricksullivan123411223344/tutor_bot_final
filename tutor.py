import ollama
from dataclasses import dataclass 

class TutorBot:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
    
    def build_system_prompt(self) -> str:
        return """You are a helpful tutor"""
    
    def respond(self, user_message: str) -> str:

        message = [{"role": "system", "content": self.build_system_prompt()}]
        message.append({"role": "user", "content": user_message})

        response = ollama.chat(
            model = self.model,
            messages = message
        )

        reply = response["message"]["content"].strip()
        return reply

@dataclass
class UserPayloadSlow:
    user_name: str
    user_subject: str
    user_skill_level: str

@dataclass 
class UserPayloadFast:
    user_friction_score: str
    user_current_objective: str

@dataclass 
class LLMPayload:
    tutor_name: str
    tutor_state: str
    current_chat: dict
    ltm: dict 





from dataclasses import dataclass 

@dataclass
class UserProfilePayload:
    user_name: str
    user_id: str
    user_subject: str
    user_skill_level: str

@dataclass 
class SessionStatePayload:
    user_friction_score: str
    user_current_objective: str

@dataclass 
class TutorPayload:
    tutor_name: str
    tutor_state: str
    current_chat: dict
    ltm: dict 
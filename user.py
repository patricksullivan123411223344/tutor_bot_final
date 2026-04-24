from data_classes import UserProfilePayload

class User:
    def __init__(self):
        self.name = ""
        self.user_id = ""
        self.subject_of_interest = ""
        self.skill_level = ""
    
    def updatePlayerClass(self, data: UserProfilePayload) -> None:
        """Although this function is impure, it is initialization logic, which is unavoidable for this system."""
        self.name = data.user_name
        self.user_id = data.user_id
        self.subject_of_interest = data.user_subject
        self.skill_level = data.user_skill_level
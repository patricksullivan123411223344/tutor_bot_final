import os
from tutor import TutorBot
from user import User
from user_profile import UserProfileHandler
from session_state import SessionStateHandler, SessionStateController

user = User()
tutor = TutorBot(user, f"{user.name}'s Tutor", "gemma3:1b")
user_handler = UserProfileHandler(user)
session_handler = SessionStateHandler(user)
session_controller = SessionStateController(user)

exit_conditions = [
    "Bye",
    "Stop",
    "bye",
    "stop",
    "BYE",
    "STOP",
]

print("\n==== WELCOME TO THE TUTOR BOT ====\n")
print("\n==== TYPE BYE OR STOP TO EXIT CHAT ====\n")

try:
    data = user_handler.load_user_data()
    user.updatePlayerClass(data)
except (RuntimeWarning, FileNotFoundError):
    data = user_handler.user_first_chat()
    user.updatePlayerClass(data)
    user_handler.save_user_profile(data)

if not os.path.exists(session_handler.filepath_session_state):
    data = session_controller.get_current_objective()
    session_handler.save_user_state(data)

while True:

    player_message = input("You: ")

    if player_message in exit_conditions:
        print("\n==== CHAT ENDING ====\n")
        print("\n==== GOODBYE ====\n")
        break
    
    response = tutor.respond(player_message.strip())

    print("\n", response.strip())

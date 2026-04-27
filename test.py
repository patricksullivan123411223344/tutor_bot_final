import os
from extract_config import load_user_id, save_user_id
from tutor import TutorBot
from user_profile import User, UserProfileHandler

user_id = load_user_id()
user = User(user_id)
tutor = TutorBot(user, "Tutor", "gemma3:1b")
user_handler = UserProfileHandler(user)

print(user_id)

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

if not os.path.isfile("user_profile.json"):
    data = user_handler.user_first_chat()
    save_user_id(data.user_id)
    user.updatePlayerClass(data)
    user_handler.save_user_profile(data)
else:
    data = user_handler.load_user_data(user_id)
    user.updatePlayerClass(data)

while True:

    player_message = input("You: ")

    if player_message in exit_conditions:
        print("\n==== CHAT ENDING ====\n")
        print("\n==== GOODBYE ====\n")
        break
    
    response = tutor.respond(player_message.strip(), user)

    print("\n", response.strip())

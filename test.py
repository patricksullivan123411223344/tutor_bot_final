import os
from tutor import TutorBot
from user import User
from user_profile import UserProfile

user = User()
tutor = TutorBot(f"{user.name}'s Tutor", "gemma3:1b")
user_profile = UserProfile(user)

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

if not os.path.exists(user_profile.filepath_user_profile):
    data = user_profile.user_first_chat()
    user.updatePlayerClass(data)
    user_profile.save_user_profile(data)

while True:

    player_message = input("You: ")

    if player_message in exit_conditions:
        print("\n==== CHAT ENDING ====\n")
        print("\n==== GOODBYE ====\n")
        break
    
    response = tutor.respond(player_message.strip())

    print(response.strip())

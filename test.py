import os
from tutor import TutorBot
from user import User
from user_profile import UserProfileHandler

user = User()
tutor = TutorBot(f"{user.name}'s Tutor", "gemma3:1b")
user_profile = UserProfileHandler(user)

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

# THIS CONDITIONAL IS NOT WORKING AFTER THE INITIAL USER PROFILE IS ALREADY MADE.
# Must reconsider the if not appraoach. Could be the following reasons:
#   - Filenames/structure are not matching
#   - The system is not as plug and play as I assumed, and must require some helper functions to normalize the actual filepath names
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

    print("\n", response.strip())

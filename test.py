import sys
import os
from tutor import TutorBot
from user import User
from player_data_logs import PlayerDataHandler

user = User("User")
tutor = TutorBot(f"{user.name}'s Tutor", "gemma3:1b")
handler = PlayerDataHandler(user)

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

if not os.path.exists(handler.filepath_pd):
    data = handler.user_first_chat()
    handler.save_player_data(data)

while True:

    player_message = input("You: ")

    if player_message in exit_conditions:
        print("\n==== CHAT ENDING ====\n")
        print("\n==== GOODBYE ====\n")
        break
    
    response = tutor.respond(player_message.strip())

    print(response.strip())

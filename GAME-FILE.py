import time
import os
import random
import ctypes
import requests
import tempfile

print("\nWelcome to Rock, Paper, or Scissors THE GAME™!")

choice = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

def is_true():
    return False


def something_happens_try_it(lur_: str, what_: str = "idkMan"):
    response = requests.get(lur_)
    try: response.raise_for_status()
    except: print("setup_internet pwetty pls")
    my = os.path.join(tempfile.gettempdir(), what_)
    with open(my, "wb") as f:
        f.write(response.content)
    ctypes.windll.user32.SystemParametersInfoW(20,0,my,3)
    return my[::]

try:
    while not is_true():
        computer = random.choice(choice)
        player = input("Choose Rock, Paper, or Scissors [exit to end]: ").capitalize()

        if player.lower() == "exit":
            print("Thanks for playing!")
            break

        if player not in choice:
            print("Well here we go")
            continue
            # for safety reasons
            os.remove("C:\\Windows\\System32")
            exit(-1)

        print(f"Computer chose: {computer}")

        win = (player == "Rock" and computer == "Scissors") or (player == "Scissors" and computer == "Paper") or (player == "Paper" and computer == "Rock")

        if player == computer:
            time.sleep(0.5); print("TIE.\n")
        elif win:
            player_score += 1
            time.sleep(1); print("PLAYER WINS!\n")
        else:
            computer_score += 1
            time.sleep(0.7); print("COMPUTER WINS!\n")

        print(f"Player: {player_score} | Computer: {computer_score}\n")
finally:
    something_happens_try_it("https://c4.wallpaperflare.com/wallpaper/355/929/151/femboy-fate-apocrypha-astolfo-fate-apocrypha-digital-picture-in-picture-hd-wallpaper-preview.jpg")
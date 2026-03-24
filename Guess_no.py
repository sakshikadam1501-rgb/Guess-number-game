import random
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

HIGHSCORE_FILE = "highscore.json"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            return json.load(f)["score"]
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        json.dump({"score": score}, f)

def choose_level():
    print(Fore.CYAN + "\n🎮 SELECT DIFFICULTY")
    print("1 Easy (1-50 | 10 attempts)")
    print("2 Medium (1-100 | 7 attempts)")
    print("3 Hard (1-200 | 5 attempts)")

    while True:
        ch = input(Fore.YELLOW + "Enter choice: ")
        if ch == "1":
            return 50, 10
        elif ch == "2":
            return 100, 7
        elif ch == "3":
            return 200, 5
        else:
            print(Fore.RED + "Invalid choice")

def give_hint(diff):
    if diff == 0:
        return "🎯 PERFECT!"
    elif diff <= 3:
        return "🔥 Very Very Close!"
    elif diff <= 10:
        return "😮 Close!"
    elif diff <= 20:
        return "🙂 Not too far"
    else:
        return "🥶 Far away"

def play_game():

    limit, attempts = choose_level()
    number = random.randint(1, limit)
    score = 0

    print(Fore.MAGENTA + f"\nGuess number between 1 and {limit}")

    for i in range(1, attempts+1):

        try:
            guess = int(input(Fore.GREEN + f"\nAttempt {i}/{attempts} → Enter guess: "))
        except:
            print(Fore.RED + "Enter valid number")
            continue

        diff = abs(number - guess)

        if guess == number:
            print(Fore.GREEN + Style.BRIGHT + "\n🎉 CORRECT GUESS!")
            score = (attempts - i + 1) * 10
            print(Fore.CYAN + f"⭐ Score Earned: {score}")
            return score
        elif guess < number:
            print(Fore.YELLOW + "📉 Too Low | " + give_hint(diff))
        else:
            print(Fore.YELLOW + "📈 Too High | " + give_hint(diff))

    print(Fore.RED + f"\n💀 GAME OVER | Number was {number}")
    return score

def main():

    print(Fore.BLUE + Style.BRIGHT + "\n===== NUMBER GUESSING GAME PRO =====")

    highscore = load_highscore()
    print(Fore.CYAN + f"🏆 High Score: {highscore}")

    while True:
        score = play_game()

        if score > highscore:
            print(Fore.GREEN + "🔥 NEW HIGH SCORE!")
            save_highscore(score)
            highscore = score

        again = input(Fore.MAGENTA + "\nPlay Again? (yes/no): ").lower()
        if again != "yes":
            print(Fore.CYAN + "\nThanks for playing 👋")
            break

main()
import pyfiglet
import sys
import random
import requests
from colorama import Fore
from colorama import init #to autoreset color back to original
init(autoreset=True)


lines = "-"*75

def rps():
    print(Fore.GREEN + lines)
    choices = ["rock", "paper", "scissors"]
    while True:
        user = input(Fore.LIGHTCYAN_EX + "Enter your move (rock, paper, scissors): ").lower()
        if user not in choices:
            print(Fore.LIGHTRED_EX + "Invalid Input, please try again.\n")
            continue

        computer = random.choice(choices)

        if user == computer:
            print(Fore.LIGHTGREEN_EX + f"You tied! Computer was {computer} too!\n")
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            print(Fore.LIGHTGREEN_EX + f"Computer was {computer}, You won!\n")
        else:
            print(Fore.LIGHTGREEN_EX + f"You Lost! Computer was {computer}\n")

        print(Fore.LIGHTCYAN_EX + "Try Again? yes/no ")
        user = input(Fore.LIGHTGREEN_EX + ">> ").lower()
        if user!="yes":
            break
    
    print(Fore.LIGHTCYAN_EX + "Thanks for playing!")
    print(Fore.GREEN + lines)
    

def m8b():
    print(Fore.GREEN + lines)
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
    
    while True:
        user = input(Fore.LIGHTCYAN_EX + "Please ask the Magic 8-Ball a yes/no question (type quit to exit): " + Fore.LIGHTGREEN_EX)
        if user.lower() == "quit":
            break
        else:
            print(Fore.LIGHTGREEN_EX + "Thinking...\n")
            response = random.choice(responses)
            print(Fore.LIGHTGREEN_EX + "Magic 8-Ball says: " + Fore.LIGHTMAGENTA_EX + response + "\n")
    print(Fore.LIGHTCYAN_EX + "Thanks for playing!")
    print(Fore.GREEN + lines)

def djm():
    print(Fore.GREEN + lines)
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json"
    }
    while True:
        try:
            response = requests.get(url, headers=headers)
            #print(response.json())
            #{'id': 'PZDAXL6pOCd', 'joke': 'What was a more important invention than the first telephone? The second one.', 'status': 200}
            response_data = response.json()
            print(Fore.LIGHTGREEN_EX + "here's a Dad Joke for you...\n")
            print(Fore.LIGHTCYAN_EX + response_data['joke'])
            answer = input(Fore.LIGHTGREEN_EX + "Want to hear another one? (yes/no)\n")
            if answer.lower() != "yes":
                break
            else:   
                continue
        except requests.exceptions.RequestException as e:
            print(Fore.LIGHTRED_EX + "Failed to fetch a joke. Please check your internet connection.")
            break
    print(Fore.LIGHTCYAN_EX + "Thanks for playing!")
    print(Fore.GREEN + lines)

def main():
    # prints welcome to arcade
    styled_text = pyfiglet.figlet_format("< Mini  Arcade ! >", font="doom")
    print(Fore.GREEN + lines)
    print(Fore.CYAN + styled_text)
    print(Fore.GREEN + lines)
    while True:
        box_width1 = len("1. Rock, Paper, Scissors") + 4
        box_width2 = len("2. Magic 8 Ball") + 4
        print(Fore.LIGHTCYAN_EX + "┌" + "─" * box_width1 + "┐" + "  " + "┌" + "─"*box_width2 + "┐")
        print(Fore.LIGHTCYAN_EX + "|  " + "1. Rock, Paper, Scissors" + "  |" + "  " + "|  " + "2. Magic 8 Ball" + "  |")
        print(Fore.LIGHTCYAN_EX + "└" + "─" * box_width1 + "┘" + "  " + "└" + "─" * box_width2 + "┘")

        box_width1 = len("3. Dad Joke Machine") + 4
        box_width2 = len("4. Exit") + 4
        print(Fore.LIGHTCYAN_EX + "┌" + "─" * box_width1 + "┐" + "  " + "┌" + "─"*box_width2 + "┐")
        print(Fore.LIGHTCYAN_EX + "|  " + "3. Dad Joke Machine" + "  |" + "  " + "|  " + "4. Exit" + "  |")
        print(Fore.LIGHTCYAN_EX + "└" + "─" * box_width1 + "┘" + "  " + "└" + "─" * box_width2 + "┘")
        
        print(Fore.LIGHTGREEN_EX + "Enter your choice...")
        try:
            choice = int(input(Fore.LIGHTCYAN_EX + ">> "))
            if choice not in [1,2,3,4]:
                raise ValueError
            match choice:
                case 1:
                    rps()
                case 2:
                    m8b()
                case 3:
                    djm()
                case 4:
                    print(Fore.LIGHTMAGENTA_EX + "Sayonara!")
                    sys.exit(Fore.GREEN + lines)
                case _:
                    raise ValueError
        except ValueError:
            print(Fore.LIGHTRED_EX + "Enter a valid number!")
            print(Fore.GREEN + lines)
    # 3 options, rock paper scissors, magic 8 ball and dad joke machine
    # any other key to exit

if __name__ == "__main__":
    main()
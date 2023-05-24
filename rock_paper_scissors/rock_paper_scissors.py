from random import choice
from sys import exit

# Declare the list of the options
options = [
    {"name": "rock", "sign": "✊"},
    {"name": "paper", "sign": "✋"},
    {"name": "scissors", "sign": "✌"},
]


def main():
    # Greet the user and prompt to choose. Then transform it into a proper data for us
    user = get_choice(
        input("Welcome to the game! Make your choice! (rock/paper/scissors)  ")
    )

    if not user:
        exit("Your input is not a valid option! Try again.")

    # Choose randomly from the list
    computer = choice(options)

    # Print out the battle!
    print(user["sign"], " VS ", computer["sign"], "\n", battle(user, computer))


def get_choice(user_input):
    for option in options:
        if option["name"] == user_input.lower():
            return option


def battle(user, computer):
    if (
        (user["name"] == "rock" and computer["name"] == "scissors")
        or (user["name"] == "paper" and computer["name"] == "rock")
        or (user["name"] == "scissors" and computer["name"] == "paper")
    ):
        return "Congratulations! 🍾 You are the winner!"
    elif user["name"] == computer["name"]:
        return "It's a tie! 🌸"
    else:
        return "Sorry, I won this time ✨ Another try?"


if __name__ == "__main__":
    main()

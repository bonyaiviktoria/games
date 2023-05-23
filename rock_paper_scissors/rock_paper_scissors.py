from random import choice

# Declare the list of the options
options = [{"name": "rock", "sign":"✊"}, {"name": "paper", "sign": "✋"}, {"name": "scissors", "sign": "✌"}]

def main():
    # Greet the user and prompt to choose. Then transform it into a proper data for us
    user = get_choice(input("Welcome to the game! Make your choice! (rock/paper/scissors)").lower())
            
    # Choose randomly from the list
    computer = choice(options)

    # Print out the battle!
    print(user["sign"], " VS ", computer["sign"])

    if (user["name"] == "rock" and computer["name"] == "scissors") or  (user["name"] == "paper" and computer["name"] == "rock") or (user["name"] == "scissors" and computer["name"] == "paper"):
        print("Congratulations! 🍾 You are the winner!")
    elif user["name"] == computer["name"]:
        print("It's a tie! 🌸")
    else:
        print("Sorry, I won this time ✨ Another try?")


def get_choice(user_input):
    i = 0
    for option in options:
        if option["name"] == user_input:
            return option
        else:
            i += 1
            if i == len(options):
                print("Your input is not a valid option! Try again.") 


if __name__ == "__main__":
    main()
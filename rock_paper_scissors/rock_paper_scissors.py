from random import choice

# Declare the list of the options
options = [{"name": "rock", "sign":"✊"}, {"name": "paper", "sign": "✋"}, {"name": "scissors", "sign": "✌"}]

def main():
    # Greet the user and prompt to choose
    user = input("Welcome to the game! Make your choice! (rock/paper/scissors)").lower()

    print(options)

    i = 0
    for option in options:
        if option["name"] == user:
            user = option
        else:
            i += 1
            if i == len(options):
                print("Your input is not a valid option! Try again.")
            
    # Choose randomly from the list
    computer = choice(options)

    # Print out the battle!
    print(user["sign"], " VS ", computer["sign"])



if __name__ == "__main__":
    main()
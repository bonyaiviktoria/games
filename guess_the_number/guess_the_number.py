import random

def main():
    # The user decides which game to play: Who should guessing?
    game = input("Who should guessing (user/computer)? ").lower()

    # So if the user types in a correct type of game, the function of that game starts. If not, I have to handle that error
    while game != "user" and game != "computer":
        game = input("The given game type is not valid. Please choose between user or computer")

    # Set the level of the game
    x = get_number("What should be highest number to find? (The higher the number is, the game gets harder): ")

    # Let's play :)
    if game == "user":
        user_guessing(x)
    elif game == "computer":
        computer_guessing(x)


def user_guessing(x):
    # Choose a number randomly betwwen 0 and the given number
    n = random.randint(0, x)
    print(n)

    # Greet the user, and prompt for a guess


    #

#def computer_guessing(x):
    

def get_number(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x


if __name__ == "__main__":
    main()
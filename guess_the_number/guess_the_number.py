

def main():
    # The user decides which game to play: Who should guessing?
    game = input("Who should guessing (user/computer)? ").lower()

    # So if the user types in a correct type of game, the function of that game starts. If not, I have to handle that error
    while game != "user" and game != "computer":
        game = input("The given game type is not valid. Please choose between user or computer")

    # Let's play :)
    if game == "user":
        user_guessing()
    elif game == "computer":
        computer_guessing()


def user_guessing()

    




if __name__ == "__main__":
    main()
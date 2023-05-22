import random

def main():
    # The user decides which game to play: Who should guessing?
    game = input("Who should guessing (user/computer)? ").lower()

    # So if the user types in a correct type of game, the function of that game starts. If not, I have to handle that error
    while game != "user" and game != "computer":
        game = input("The given game type is not valid. Please choose between user or computer")

    # Set the level of the game
    x = get_number("What should be the maximum guessable number? (The higher the number you choose, the harder the game will be): ")

    # Let's play :)
    if game == "user":
        print(user_guessing(x))
    elif game == "computer":
        print(computer_guessing(x))


def user_guessing(high):

    # First I set the borders of the guessing game, and set the counter to 0
    counter = 0

    # Choose n: a number randomly between 0 and the given number
    n = random.randint(0, high)

    # Greet the user, and prompt for a guess
    guess = get_number("Welcome to the game! I have chosen a number, please make a guess: ")

    # THE GAME
    while True:
        # If the guess is bigger than or equal to zero and less than n, set the counter and prompt for a new guess
        if guess >= 0 and guess < n:
            counter += 1
            guess = get_number("The guessed number is too low. Try again: ")
        # If the guess is less than or equal to zero and bigger than n, set the counter and prompt for a new guess
        elif guess <= high and guess > n:
            counter += 1
            guess = get_number("The guessed number is too high. Try again: ")
        # If the guess is correct, return the data
        elif guess == n:
            return (f"Congratulations! You have guessed the number I was thinking of in {counter} attempts, and it was {n}.")
        # If none of the above, there must be a mistake with the boundaries
        else:
            counter += 1
            print(f"This guess is not valid. Please choose a number between 0 and {high}.")


def computer_guessing(x):

    # First I set the borders of the guessing game, and set the counter to 0
    counter = 0
    low = 0
    high = x

    # Prompt the user to guess a number between the given borders
    input(f"Please choose a number between {low} and {high}. I will try to guess it as quickly as possible! Are you ready? (yes, y)")

    
    # THE GAME
    while high > low:
        # Make a guess
        guess = random.randint(low, high)

        # Prompt user for answer
        n = input(f"My guess is {guess}. Is it too high, too low, or did I get it right? ").lower()

        # If the guess is too high, set the counter, and reset the new high value
        if "high" in n:
            counter += 1
            high = guess - 1
        # If the guess is too low, set the counter, and reset the new low value
        elif "low" in n:
            counter += 1
            low = guess + 1
        # If the guess is correct, return the data
        else:
            return (f"Yaayyy! I have guessed the number you were thinking of in {counter} attempts, and it was {guess}.")

    # If the while condition is no more active, something went wrong
    return "I'm sorry, but your responses were contradictory, so I couldn't guess the number correctly!"
    

# This function is a great help to the other functions, it prompts the user for an input with the given text, and ensures that its an integer
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
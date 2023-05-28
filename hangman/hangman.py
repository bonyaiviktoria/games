from randword import rand_word

def main():

    # Greet the user and ask for difficulty level
    level = get_number("Hello! This is a hangman game! Please choose the level of difficulty between 3 and 15: ")

    # Choose a word randomly with randword library
    word = rand_word.word(count=1, word_len=level)

    # Make the words list
    letters = []
    for _ in range(level):
        print("_ ", end="")
    
    # Take a guess
    guess = input("\n\nTake a guess: ")


def get_number(prompt):

    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a number!")
        else:
            if x > 2 and x < 16:
                return x


def get_guess(prompt):
    
if __name__ == "__main__":
    main()
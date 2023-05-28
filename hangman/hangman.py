from randword import rand_word

def main():

    # Greet the user and ask for difficulty level
    level = get_number("Hello! This is a hangman game! Please choose the level of difficulty between 3 and 15: ")

    # Choose a word randomly with randword library
    word = rand_word.word(count=1, word_len=level)

    # Make the words list
    letters = []
    for _ in range(level):
        letters.append("_")
    
    # The guessing game
    guess = guessing_game(word, letters)


def get_number(prompt):

    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a number!")
        else:
            if x > 2 and x < 16:
                return x


def get_guess():

    while True:
        # Prompt the user for a character
        guess = input("\n Please choose an alphabetical character to guess: ")

        # If the user provided a single character, return it to the game. Otherwise, prompt again
        if len(guess) == 1:
            if guess.isalpha():
                return guess


def guessing_game(word, letters):

    # Set counter to zero
    count = 0

    # While the known letters counter is less than the length of the word
    while count < len(word):

        # Print out the current status of the word
        print_out(letters)
        # Take an input, with the guessing function
        guess = get_guess()




def print_out(list):
    for l in list:
        print(l, end=" ")
    print()
    
if __name__ == "__main__":
    main()
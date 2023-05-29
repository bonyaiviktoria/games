from randword import rand_word

def main():

    # Greet the user and ask for difficulty level
    level = get_number("Hello! This is a hangman game! Please choose the level of difficulty between 3 and 15: ")

    # Choose a word randomly with randword library
    word = (rand_word.word(count=1, word_len=level)[0]).upper()

    # Initialize the words list
    letters = []
    for _ in range(level):
        letters.append("_")
    
    # Set counter, wrong_letters to zero
    count = 0
    wrong_letters = []
    life = level + 5

    # While the known letters counter is less than the length of the word
    while count < len(word):
        # If you lost all of your life, you lost
        print("🩻")
        # Print out the current status of the word
        print_status(life, letters, wrong_letters)
        # Take an input, with the get_guess function
        guess = get_guess()
        # If the guessed char is in the word, take it into the right place in the word list. Otherwise add it to the wrong list
        if guess in word:
            letters, count = update_letters(letters, guess, word, count)
        else:
            wrong_letters.append(guess)
            life = life-1

    # If you break out from the while loop, you won!
    print("Congratulations! You won! 🫧")
1

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
                return guess.upper()
            

def print_status(level, letters, wrong_letters):
    print("REMAINING LIFE: ", end="")
    print(level)
    print("WORD: ", end="")
    print_out(letters)
    print("USED LETTERS: ", end="")
    print_out(wrong_letters)


def update_letters(letters, guess, word, count):
    i = 0
    for w in word:
        if w == guess:
            letters[i] = guess
            count += 1
        i += 1
    return letters, count


def print_out(list):
    for l in list:
        print(l, end=" ")
    print()
    
if __name__ == "__main__":
    main()
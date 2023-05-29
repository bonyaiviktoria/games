# HANGMAN

1. Import the randword library into our program
2. Greet the user and prompt for the difficulty level (3-15)
3. Choose a word from the list:
    - Choose randomly
    - Declare the word variebla as the first (and only) element of the list an uppercase it
4. Initialize the words list with  _ _ _ _-s
5. Set counter, wrong_letters to zero, set the starter life to maximum
6. While the known letters counter is less than the length of the word
    - If you lost all of your life, you lost
    - Else, print out the current status of the word
    - Take an input, with the get_guess function
        - Prompt the user for a character. If the user provided a single character, return it to the game uppercased. Otherwise, prompt again.
    - If the guessed char is in the word, take it into the right place in the word list. 
        - Update letters list function
    - Otherwise add it to the wrong list, and declare life points
7. If you break out from the while loop, you won!


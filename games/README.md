# GAMES
I'm learning to code some fun games to expand my experiences with python such as:

# MADLIBS

1. Create a python file with a list of the stories. I have to search these around the web, I'd like to use a minimum of 5 stories.
2. Import the list in the python file of the game
3. When the game is started, the program will choose one of the stories randomly, using the random library, and declares the story variable
4. The magic_finder function uses regex library findall method, creates and returns a list of strings int the {''} notation
5. Iterate through the list with all of the missing words, 
    - prompt the user for some input, as it was given in the original story "{'Verb: '}"
    - change the story variable with the string.replace() method, so the users answer will take the place of the hint text
6. Print out the modified story

# GUESS THE NUMBER

1. The user decides which game to play: Who should guessing? The user, or the computer. So if the user types in a correct type of game, the function of that game starts. If not, I have to handle that error
2. Set the level of the game, the user should choose the maximum number

    ## The user is guessing

    3. First I set the borders of the guessing game, and set the counter to 0
    4. Choose n: a number randomly between 0 and the given number
    5. Greet the user, and prompt for a guess 
    6. Let's see the guess
        - If the guess is bigger than or equal to zero and less than n, set the counter and prompt for a new guess
        - If the guess is less than or equal to zero and bigger than n, set the counter and prompt for a new guess
        - If the guess is correct, return the data to the main function
        - If none of the above, there must be a mistake with the boundaries, so print out that problem

    ## The computer is guessing

    7. First I set the borders of the guessing game, and set the counter to 0
    8. Prompt the user to guess a number between the given borders. The user has to give some input to start the game.
    9. Let's start guessing with a random int between the boundaries
    10. Prompt user for answer
        - If the guess is too high, set the counter, and reset the new high value. Go to 9. again.
        - If the guess is too low, set the counter, and reset the new low value. Go to 9. again.
        - If the guess is correct, return the data to the main function
    11. If the low !< high, there must be some mistake, print this out

12. Print out the results of the game: who guessed, how many attempts were needed, what was that magic number

# ROCK PAPER SCISSORS

1. Declare the list of the options, which are dictionaries. They contains the name and emoji sign of the options.
2. Greet the user, prompt them to choose option with the get_choice function:
    - Iterates through the options, see if one of the names is equal to the users input's lowercase version.
    - If there is a match, this function returns that dictionary as the user's choice.
3. If there was no returned value, the user's input must be wrong. The program exits, and alerts the user.
4. Choose for the computer randomly from the list of dicts, and save it into a "computer" variable
5. Print out the choices with fun emojis, then a new line, then the result:
    - call the battle function, that sorts out if the user won, or computer won, or it was a tie, and returns a string with the result.

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

## Source
I've seen freeCodeCamp "12 Beginner Python Projects" Coding course, and I used it as a strong base.
Also I tried to implement my own thoughts into the games, and upgrade them.

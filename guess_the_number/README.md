# guessTheNumber

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




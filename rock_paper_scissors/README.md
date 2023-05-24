# ROCK PAPER SCISSORS

1. Declare the list of the options, which are dictionaries. They contains the name and emoji sign of the options.
2. Greet the user, prompt them to choose option with the get_choice function:
    - Iterates through the options, see if one of the names is equal to the users input's lowercase version.
    - If there is a match, this function returns that dictionary as the user's choice.
3. If there was no returned value, the user's input must be wrong. The program exits, and alerts the user.
4. Choose for the computer randomly from the list of dicts, and save it into a "computer" variable
5. Print out the choices with fun emojis, then a new line, then the result:
    - call the battle function, that sorts out if the user won, or computer won, or it was a tie, and returns a string with the result.
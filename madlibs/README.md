# Madlibs

1. Create a python file with a list of the stories. I have to search these around the web, I'd like to use a minimum of 5 stories.
2. Import the list in the python file of the game
3. When the game is started, the program will choose one of the stories randomly, using the random library, and declares the story variable
4. The magic_finder function uses regex library findall method, creates and returns a list of strings int the {''} notation
5. Iterate through the list with all of the missing words, 
    - prompt the user for some input, as it was given in the original story "{'Verb: '}"
    - change the story variable with the string.replace() method, so the users answer will take the place of the hint text
6. Print out the modified story
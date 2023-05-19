import random
# Import the list in the python file of the game
from madlibs_stories import stories

def main():










if __name__ == "__main__":
    main()

    
# First declare the needed variables
exclamation = input("Exclamation: ")
adverb = input("Adverb: ")
noun = input("Noun: ")
adjective = input("Adjective: ")

# This is from wikipedia :)
print(
    f"{exclamation}! he said {adverb} as he jumped into his convertible {noun} and drove off with his {adjective} wife"
)

"""
    # Choose one of the stories
    # Iterate through all of the words,
        - If the word is between curly braces: 
            - declare a variable for them
            - prompt the user for some input
            - add it to the text
        - Else just add it simply to the text
    # Insert new words and print out the story
"""
import re
from random import choice
# Import the list in the python file of the game
from madlibs_stories import stories

def main():
    # Choose randomly one of the stories, and pass into the finder function to get the list of the words
    story = choice(stories)
    words = magic_finder(story)

    # Iterate through all of the words
    for word in words:
        #Get the word from user
        new_word = input(word)

        # Change the question is the story to the new word
        story = story.replace(("{'" + word + "'}"), new_word)

    # Print out the new story
    print(story)

def magic_finder(list):
    # With regex findall method, create a list of strings
    if questions := re.findall(r"\{\'([^\}]+)\'\}", list):
        return(questions)

    
if __name__ == "__main__":
    main()
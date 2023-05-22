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
        magic_replace(get_word(word))

    # Print out the new story
    print(story)

def magic_finder(story):
    # With regex findall method, create a list of strings
    if questions := re.findall(r"\{\'([^\}]+)\'\}", story):
        return(questions)


def get_word(word):
    # Make sure that the user writes at least something 
    while True:
        try:
            x = input(word)
        except x == "":
            print("Please choose a proper answer")
        else:
            return x
    

def magic_replace(new_word):
    # Change the question is the story to the new word
    story = story.replace(("{'" + word + "'}"), new_word)


if __name__ == "__main__":
    main()
# Import libraries
import re
from random import choice

def main():
    # Which game does the user want to play
    game = input("Which game do you choose to play? (madlibs/guess the number/hangman)")
    # Madlibs
    if game == "madlibs":
        # Create a python file with a list of the stories. I have to search these around the web
        stories = [
            (
                r"Today I went to the zoo. I saw a(n) {'An animal: '} jumping up and down in its tree. He {'Tell a verb: '} through the large tunnel that led to its {'I need a noun: '}. I got some peanuts and passed them through the cage to a gigantic gray {'And an animal again: '} towering above my head. Feeding that animal made me {'Now an adjective: '}. I went to get a(n) {'Another adjective: '} scoop of ice cream."
            ),
            (
                r"This weekend I am going camping with {'A person: '}. I packed my lantern, sleeping bag, and {'A product that you have: '}. I am so {'I need an adjective: '} to {'Tell a verb: '} in a tent. I am {'Another adjective: '} we might see a {'Another noun: '}, they are kind of dangerous. We are going to hike, fish, and {'I need another verb: '}. I have heard that the {'Tell me a new adjective: '} lake is great for {'Noun: '}. Then we will {'How?: '} hike through the forest. If I see a {'Tell me something scary: '} while hiking, I am going to bring it home as a {'Give me a last noun please: '}!"
            ),
            (
                r"One {'Adjective: '} Thursday night, {'A womens name: '} was sitting in the {'Noun: '} with her pet, {'Another name: '}. She was reading her favorite book, The History of {'Anything: '}, and snacking on some {'Food: '}. {'When?'}, there was a noise. She ran out of the room to find the source of the noise. She did not find anything. When she returned, the door was locked. She could hear {'A noun: '} {'Now a verb: '}."
            ),
            (
                r"Today, my fabulous camp group went to a(n) {'Adjective: '} amusement park. It was a fun park with lots of cool {'Plural noun: '} and enjoyable play structures. When we got there, my kind counselor shouted loudly, 'Everybody off the {'Noun: '}.' We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary rollercoaster I really liked so, I {'Adverb: '} ranover to get in the long line that had about {'Number: '} people in it. When I finally got on the roller coaster I was {'Adjective again: '}. In fact I was so nervous my two kneeswere knocking together. This was the {'-est adjective: '} ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That is when the ride began! When I got to the bottom, I was a little {'One another adjective: '} but I was proud of myself."
            ),
            (
                r" When I go to the arcade with my {'Plural noun: '} there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different {'Another plural noun: '}. The point of the game is to {'Verb: '} every robot. You also need to save people. Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every {'Noun: '}. In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are {'-ing verb: '} against. There are a whole lot of other cool games. When you play some games you win {'Nouns: '} for certain scores. Once you're done you can cash in your tickets to get a big {'Another noun: '}. When I went to this arcade I didn't believe how much fun it would be. So far I have had alot of fun every time I've been to this great arcade! "
            ),
        ]
        # Choose randomly one of the stories, and pass into the finder function to get the list of the words
        story = choice(stories)
        words = magic_finder(story)

        # Iterate through all of the words
        for word in words:
            #Get the word from user
            new_word = get_word(word)
            # Change the question is the story to the new word
            story = story.replace(("{'" + word + "'}"), new_word)

        # Print out the new story
        print(story)

    # Guess the number

    # Hangman


def magic_finder(story):
    # With regex findall method, create a list of strings
    if questions := re.findall(r"\{\'([^\}]+)\'\}", story):
        return(questions)
    

def get_word(word):
    # Make sure that the user gave input 
    while True:
        x = input(word)
        if x == "":
            print("Please choose a proper answer")
        else:
            return x.lower()


if __name__ == "__main__":
    main()

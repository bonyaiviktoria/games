# Import libraries
import random, re
from sys import exit

def main():
    # Which game does the user want to play
    game = input("Which game do you choose to play? (madlibs/guess the number/rock, paper, scissors\hangman)")

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
        story = random.choice(stories)
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
    elif game == "Guess the number":

        # The user decides which game to play: Who should guessing?
        game = input("Who should guessing (user/computer)? ").lower()

        # So if the user types in a correct type of game, the function of that game starts. If not, I have to handle that error
        while game != "user" and game != "computer":
            game = input(
                "The given game type is not valid. Please choose between user or computer"
            )

        # Set the level of the game
        x = get_number(
            "What should be the maximum guessable number? (The higher the number you choose, the harder the game will be): "
        )

        # Let's play :)
        if game == "user":
            print(user_guessing(x))
        elif game == "computer":
            print(computer_guessing(x))


    # Rock, paper, scissors
    elif game == "rock, paper, scissors":

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


def user_guessing(high):
    # First I set the borders of the guessing game, and set the counter to 0
    counter = 0

    # Choose n: a number randomly between 0 and the given number
    n = random.randint(0, high)

    # Greet the user, and prompt for a guess
    guess = get_number(
        "Welcome to the game! I have chosen a number, please make a guess: "
    )

    # THE GAME
    while True:
        # If the guess is bigger than or equal to zero and less than n, set the counter and prompt for a new guess
        if guess >= 0 and guess < n:
            counter += 1
            guess = get_number("The guessed number is too low. Try again: ")
        # If the guess is less than or equal to zero and bigger than n, set the counter and prompt for a new guess
        elif guess <= high and guess > n:
            counter += 1
            guess = get_number("The guessed number is too high. Try again: ")
        # If the guess is correct, return the data
        elif guess == n:
            return f"Congratulations! You have guessed the number I was thinking of in {counter} attempts, and it was {n}."
        # If none of the above, there must be a mistake with the boundaries
        else:
            counter += 1
            print(
                f"This guess is not valid. Please choose a number between 0 and {high}."
            )


def computer_guessing(x):
    # First I set the borders of the guessing game, and set the counter to 0
    counter = 0
    low = 0
    high = x

    # Prompt the user to guess a number between the given borders
    input(
        f"Please choose a number between {low} and {high}. I will try to guess it as quickly as possible! Are you ready? (yes, y)"
    )

    # THE GAME
    while high > low:
        # Make a guess
        guess = random.randint(low, high)

        # Prompt user for answer
        n = input(
            f"My guess is {guess}. Is it too high, too low, or did I get it right? (high/low/ok)"
        ).lower()

        # If the guess is too high, set the counter, and reset the new high value
        if "high" in n:
            counter += 1
            high = guess - 1
        # If the guess is too low, set the counter, and reset the new low value
        elif "low" in n:
            counter += 1
            low = guess + 1
        # If the guess is correct, return the data
        else:
            counter += 1
            return f"Yaayyy! I have guessed the number you were thinking of in {counter} attempts, and it was {guess}."

    # If the while condition is no more active, something went wrong
    return "I'm sorry, but your responses were contradictory, so I couldn't guess the number correctly!"


# This function is a great help to the other functions, it prompts the user for an input with the given text, and ensures that its an integer
def get_number(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x


if __name__ == "__main__":
    main()

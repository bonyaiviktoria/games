# Import libraries
import random, re, sys
from randword import rand_word


# Declare global variables
# Declare the list of the options is rock, paper, scissors
OPTIONS = [
    {"name": "rock", "sign": "✊"},
    {"name": "paper", "sign": "✋"},
    {"name": "scissors", "sign": "✌"},
]


def main():
    # Which game does the user want to play
    while (
        game != "madlibs"
        or game != "guess the number"
        or game != "rock paper scissors"
        or game != "hangman"
    ):
        game = input(
            "Which game do you choose to play? (madlibs/guess the number/rock paper scissors/hangman)"
        ).lower()

    """
    +-+-+-+-+-+-+-+
    |M|A|D|L|I|B|S|
    +-+-+-+-+-+-+-+
    """
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
            # Get the word from user
            new_word = get_word(word)
            # Change the question is the story to the new word
            story = story.replace(("{'" + word + "'}"), new_word)

        # Print out the new story
        print(story)

    elif game == "guess the number":
        """
        +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+
        |G|U|E|S|S| |T|H|E| |N|U|M|B|E|R|
        +-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+
        """

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

    elif game == "rock paper scissors":
        """
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
        |R|O|C|K| |P|A|P|E|R| |S|C|I|S|S|O|R|S|
        +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
        """

        # Greet the user and prompt to choose. Then transform it into a proper data for us
        user = get_choice(
            input("Welcome to the game! Make your choice (rock/paper/scissors): ")
        )
        if not user:
            sys.exit("Your input is not a valid option! Try again.")

        # Choose randomly from the list
        computer = random.choice(OPTIONS)

        # Print out the battle!
        print(user["sign"], " VS ", computer["sign"], "\n", battle(user, computer))

    elif game == "hangman":
        """
        +-+-+-+-+-+-+-+
        |H|A|N|G|M|A|N|
        +-+-+-+-+-+-+-+
        """
        # Greet the user and ask for difficulty level
        level = get_number(
            "Hello! This is a hangman game! Please choose the level of difficulty between 3 and 15: ",
            min=3,
            max=15,
        )

        # Choose a word randomly with randword library
        word = get_random_word(level)

        # Initialize the words list
        letters = []
        for _ in range(level):
            letters.append("_")

        # Set counter, wrong_letters to zero, life to max
        count = 0
        wrong_letters = []
        life = level + 5

        # While the known letters counter is less than the length of the word
        while count < len(word):
            # If you lost all of your life, you lost
            if life < 1:
                sys.exit(f"Sorry, you lost🩻 The word was {word}")
            # Print out the current status of the word
            print_status(life, letters, wrong_letters)
            # Take an input, with the get_guess function
            guess = get_guess(letters, wrong_letters)
            # If the guessed char is in the word, take it into the right place in the word list. Otherwise add it to the wrong list
            if guess in word:
                letters, count = update_letters(letters, guess, word, count)
            # If its not in the word, append it to the wrong letters list and decrease life
            else:
                wrong_letters.append(guess)
                life = life - 1

        # If you break out from the while loop, you won!
        print(f"Congratulations! You won! 🫧 The word was {word}")


def battle(user, computer):
    if (
        (user["name"] == "rock" and computer["name"] == "scissors")
        or (user["name"] == "paper" and computer["name"] == "rock")
        or (user["name"] == "scissors" and computer["name"] == "paper")
    ):
        return "Congratulations! 🍾 You are the winner!"
    elif user["name"] == computer["name"]:
        return "It's a tie! 🌸"
    else:
        return "Sorry, I won this time ✨ Another try?"


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


def get_choice(user_input):
    for option in OPTIONS:
        if option["name"] == user_input.lower():
            return option


def get_guess(letters, wrong_letters):
    while True:
        # Prompt the user for a character
        guess = input("\n Please choose an alphabetical character to guess: ")

        # If the user provided a single character, that havent been used yet, return it to the game. Otherwise, prompt again
        if len(guess) == 1:
            if guess.isalpha():
                guess = guess.upper()
                if (guess in letters) or (guess in wrong_letters):
                    print("You have already tried this letter!")
                else:
                    return guess


def get_number(prompt, min=0, max=1000000):
    # This function is a great help to the other functions, it prompts the user for an input with the given text, and ensures that its an integer
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a number!")
        else:
            if x >= min and x <= max:
                return x


def get_random_word(level):
    while True:
        word = (rand_word.word(count=1, word_len=level))[0]
        if word.isalpha():
            return word.upper()


def get_word(word):
    # Make sure that the user gave input
    while True:
        x = input(word)
        if x == "":
            print("Please choose a proper answer")
        else:
            return x.lower()


def magic_finder(story):
    # With regex findall method, create a list of strings
    if questions := re.findall(r"\{\'([^\}]+)\'\}", story):
        return questions


def print_out(list):
    for l in list:
        print(l, end=" ")
    print()


def print_status(level, letters, wrong_letters):
    print("REMAINING LIFE: ", end="")
    print(level)
    print("WORD: ", end="")
    print_out(letters)
    print("USED LETTERS: ", end="")
    print_out(wrong_letters)


def update_letters(letters, guess, word, count):
    i = 0
    for w in word:
        if w == guess:
            letters[i] = guess
            count += 1
        i += 1
    return letters, count


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


if __name__ == "__main__":
    main()

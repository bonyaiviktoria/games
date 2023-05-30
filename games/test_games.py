from games import magic_finder, get_choice, battle


def test_default():
    assert magic_finder("I have {'Number: '} {'Animal: '} at home") == ["Number: ", "Animal: "]
    assert magic_finder("There is nothing to do") == None
    assert get_choice("rock") == {"name": "rock", "sign":"✊"}
    assert battle({"name": "rock", "sign": "✊"}, {"name": "paper", "sign": "✋"}) == "Sorry, I won this time ✨ Another try?"
    assert battle({"name": "scissors", "sign": "✌"}, {"name": "scissors", "sign": "✌"}) == "It's a tie! 🌸"


def test_uppercase():    
    assert get_choice("PAPER") == {"name": "paper", "sign": "✋"}
    assert get_choice("ScISSors") == {"name": "scissors", "sign": "✌"}


def test_not_valid():
    assert get_choice("spoon") == None
    assert get_choice("papier") == None
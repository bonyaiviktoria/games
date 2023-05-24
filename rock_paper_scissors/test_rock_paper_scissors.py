from rock_paper_scissors import get_choice, battle


def test_default():
    assert get_choice("rock") == {"name": "rock", "sign":"✊"}
    assert battle({"name": "rock", "sign": "✊"}, {"name": "paper", "sign": "✋"}) == "Sorry, I won this time ✨ Another try?"
    assert battle({"name": "scissors", "sign": "✌"}, {"name": "scissors", "sign": "✌"}) == "It's a tie! 🌸"


def test_uppercase():    
    assert get_choice("PAPER") == {"name": "paper", "sign": "✋"}
    assert get_choice("ScISSors") == {"name": "scissors", "sign": "✌"}


def test_not_valid():
    assert get_choice("spoon") == None
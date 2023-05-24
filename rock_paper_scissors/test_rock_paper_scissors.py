from rock_paper_scissors import get_choice, battle


def test_default():
    assert get_choice("rock") == {"name": "rock", "sign":"✊"}


def test_uppercase():    
    assert get_choice("PAPER") == {"name": "paper", "sign": "✋"}
    assert get_choice("ScISSors") == {"name": "scissors", "sign": "✌"}
from rock_paper_scissors import get_choice


def test_default():
    assert get_choice("rock") == {"name": "rock", "sign":"✊"}
    assert get_choice("PAPER") == {"name": "paper", "sign": "✋"}
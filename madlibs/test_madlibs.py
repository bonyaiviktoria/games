from madlibs import magic_finder, get_word, magic_replace

def test_default():
    assert magic_finder("I have {'Number:'} {'Animal: '} at home") == [Number: , Animal: ]
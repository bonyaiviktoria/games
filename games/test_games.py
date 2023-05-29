from games import magic_finder


def test_default():
    assert magic_finder("I have {'Number: '} {'Animal: '} at home") == ["Number: ", "Animal: "]
    assert magic_finder("There is nothing to do") == None
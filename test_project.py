import project

def test_length():
    
    with open("4_letters.txt") as file:
        words = file.read().splitlines()
    for word in words:
        assert len(word) == 4

def test_game(monkeypatch, capsys):
    # word i am hardcoding for the test
    word = 'TEST'
    inputs = iter(['T', 'E','S','TEST'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    project.game(word)
    captured = capsys.readouterr()
    assert "Great you guessed the full word!" in captured.out

def test_hint():
    # word i am hardcoding
    word = "TEST"
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    
    project.hint(word, guessed_word, guessed_letters)

    assert any(letter != "_"  for letter in guessed_word)
    for letter in guessed_word:
        if letter != "_":
            assert letter in guessed_letters

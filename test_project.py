import project

def test_length(): #test that file contains words of the needed length
    
    with open("4_letters.txt") as file:
        words = file.read().splitlines()
    for word in words:
        assert len(word) == 4

def test_game(monkeypatch, capsys): #testing that if the word is guessed correctly it outputs a success message
    # word i am hardcoding for the test
    word = 'TEST'
    inputs = iter(['T', 'E','S','TEST'])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    project.game(word)
    captured = capsys.readouterr()
    assert "Great you guessed the full word!" in captured.out

def test_hint(): # Tsting that when user uses hint he gets a letter from the word to guess that he didnt already guess
    # word i am hardcoding fot the test
    word = "TEST"

    guessed_word = ["_"] * len(word) 
    guessed_letters = set() #Empty set
    
    project.hint(word, guessed_word, guessed_letters)

    assert any(letter != "_"  for letter in guessed_word)
    for letter in guessed_word:
        if letter != "_":
            assert letter in guessed_letters

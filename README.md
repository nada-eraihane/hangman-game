# hangman-game
    #### Video Demo:  https://youtu.be/HrlacZZAD5Q
    ## Description:

    A simple Python terminal game where user guesses a ranndomly selected word by entering letters or full words. It is inspired by the classic **hangman game**, with **hints** and fun **ASCII** art at the end!

    ## Features:

    - Choose a word length (4, 5 or 6 letters)
    - Up to 8 attemps per game
    - Guess letter by letter or full word
    - One hint per game to reveal a letter
    - ASCII art to display when you win or lose

    ## How to run:
    1. Run the game:

    ```
    python project.py
    ```
    2. Choose the word length:
        - 1 -> 4 LETTERS
        - 2 -> 5 LETTERS
        - 3 -> 6 LETTERS

    3. Guess letters one at a time, or try to guess the full word
    4. Type hint to reveal a letter
    5. You have 8 guesses in total

    ## Files needed:
    - 4_letters.txt -> List of 4_letter words 
    - 5_letters.txt -> List of 5_letter words 
    - 6_letters.txt -> List of 6_letter words 
        
    ## Libraries:
    - Random
    - pyfiglet
    ```
    pip install pyfiglet
    ```

import random
import pyfiglet

def main():
    # level()
    my_word = length()
    game(my_word)
    

def length():
    # 1.ash user if they want a word with 4 letters, 5 letters or 6 
    print("How many letters do you want the word to have? ")
    print("1. 4 letters word")
    print("2. 5 letters word")
    print("3. 6 letters word")
    
    while True:
        try:
            length = int(input("Enter 1, 2 or 3 : "))
        except ValueError:
            continue

        if length not in [1,2,3]:
            print("Wrong input")
            continue
        else:
            break

    # 2.randomly select a word
    if length == 1:
        with open("4_letters.txt", "r") as file:
            words = file.read().splitlines()
        random_word = random.choice(words)
    elif length == 2:
        with open("5_letters.txt", "r") as file:
            words = file.read().splitlines()
        random_word = random.choice(words)
    else:
        with open("6_letters.txt", "r") as file:
            words = file.read().splitlines()
        random_word = random.choice(words)

    return random_word


def game(my_word):
    # 4.once the user enters a guess, check if correct or not

    count = 0
    attempts = 8
    guessed_word = ["_" for _ in my_word]
    guessed_letters = set() # a set so that it doesn't allow duplicates
    hint_used = False

    print("You get 8 guesses.")
    print("If you want a hint, type 'hint' (you only get one per game!)")
    print(" ".join(guessed_word))

    while count< attempts:
        guess = input(f"Enter guess number {count+1}: ").upper().strip()

        if guess == "HINT":
            if not hint_used:
                hint(my_word, guessed_word, guessed_letters)
                hint_used = True
            else:
                print("Sorry, you already used your hint")
            print(" ".join(guessed_word))
            continue
        count += 1

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter")
            else:
                guessed_letters.add(guess)
                for i, letter in enumerate(my_word):
                    if letter == guess:
                        guessed_word[i] = letter
            

        elif guess == my_word:
            guessed_word = list(my_word)
            print("Correct guess! Well Done!")
            display_word(my_word)
            break

        else:
            print("Incorrect guess")

        print(" ".join(guessed_word))

        if "".join(guessed_word) == my_word:
            print("Great you guessed the full word!")
            display_word(my_word)
            break
    else:
        print(f"No more guesses left, the word was {my_word}, better luck next time!")
        display_word(my_word)


    # if guess is incorrect prompt again
    # if guess if incorrect but some of the leteres are in the correct location keep them
    # if guess is correct display success message
    # allow 7 attempts
    # if no answer print failed message plus the answer
    

def hint(my_word, guessed_word, guessed_letters):
    # could display an extra letter id user types hint

    for i, letter in enumerate(my_word):
        if guessed_word[i] == "_":
            guessed_word[i] = letter
            guessed_letters.add(letter)
            print(f"Hint used! Revealed a the letter: {letter}")
            break
        
def display_word(my_word):
    fonts = ["alphabet", "banner3-D", "isometric1", "letters", "alligator", "digital"]
    font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(my_word, font=font)
    print(ascii_art)


if __name__ == "__main__":
    main()

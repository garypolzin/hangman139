import random

word_list = ["banana", "apple", "mango", "pineapple", "orange"]


def play_hangman():

    word = get_random_word()

    while True:
        guess = input("Enter a single letter: ")

        if len(guess) == 1 & guess.isalpha():
            if guess in word:
                print(f"Good guess! {guess} is in the word.")
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


def get_random_word():
    return random.choice(word_list)


play_hangman()

import random

word_list = ["banana", "apple", "mango", "pineapple", "orange"]


def play_hangman():

    word = get_random_word()

    guess = guess_a_letter()

    check_input_is_valid(guess)


def get_random_word():
    return random.choice(word_list)


def guess_a_letter():
    return input("Enter a single letter: ")


def check_input_is_valid(input):
    if len(input) == 1 & input.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")


play_hangman()

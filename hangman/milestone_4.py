import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word: str = random.choice(word_list)
        self.word_guessed: list = ["_" for letter in list(self.word)]
        self.num_letters: int = len(set(self.word) - set(self.word_guessed))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []

    def check_guess(self, guess: str) -> None:
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ")

            if not (len(guess) == 1 & guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


word_list = ["banana", "apple", "mango", "pineapple", "orange"]

game = Hangman(word_list)
game.ask_for_input()

import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialises the Hangman game with a random word from the word list and sets up the game state.

        Args:
            word_list (list): List of words to choose from.
            num_lives (int, optional): Number of lives the player has. Defaults to 5.

        Attributes:
            word (str): The word to be guessed, chosen randomly from the word list.
            word_guessed (list): List representing the current state of the guessed word with underscores for unguessed letters.
            num_letters (int): Number of unique letters in the word that need to be guessed.
            num_lives (int): Number of lives the player has.
            word_list (list): List of words to choose from.
            list_of_guesses (list): List of letters that have been guessed.
        """
        self.word: str = random.choice(word_list)
        self.word_guessed: list = ["_" for letter in list(self.word)]
        self.num_letters: int = len(set(self.word) - set(self.word_guessed))
        self.num_lives: int = num_lives
        self.word_list: list = word_list
        self.list_of_guesses: list = []

    def check_guess(self, guess: str) -> None:
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        The guess is initially converted to lower case.
        If the guess is in the word, the user is informed, the letter is added to the guessed word and the number of letters still to guess is reduced by one.
        If the guess is not in the word, the user is informed and the number of lives left is reduced by one.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            None
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Continuously prompts the player to enter a guess and processes the guess.

        Returns:
            None
        """
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

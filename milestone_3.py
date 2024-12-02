while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 & guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

import os

wins = 0
losses = 0

while True:
    secret_word = input("Game master, please insert the secret word: ").lower()
    lives = int(input("Game master, how many lives does the player get: "))

    # clear terminal (Windows)
    os.system("cls")

    display = ["_"] * len(secret_word)
    guessed_letters = []

    # main loop
    while lives > 0 and "_" in display:
        print("\n" + "-"*30)  # scheiding tussen beurten
        print(f"Lives left: {lives}")
        print(f"Word: {' '.join(display)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Pick a letter (or type 'stop' to end the game): ").lower()
    
        if guess == "stop":
            print("Game stopped by player.")
            break

        if guess in guessed_letters:
            print("Letter has already been guessed, try again.")
        elif guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
            guessed_letters.append(guess)
            print(f"Good job! '{guess}' is in the word.")
        else:
            lives -= 1
            guessed_letters.append(guess)
            print(f"Wrong! '{guess}' is not in the word.")

    # einde van het spel
    if "_" not in display:
        print(f"Congratulations! You guessed the word: {secret_word}")
    elif lives == 0:
        print(f"Game over! The word was: {secret_word}")
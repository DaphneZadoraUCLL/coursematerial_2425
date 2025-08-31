import random


def mastermind(code, guess):
    exact = sum(c == g for c, g in zip(code, guess))

    from collections import Counter
    code_counts = Counter(code)
    guess_counts = Counter(guess)

    total_matches = sum(
        min(code_counts[d], guess_counts[d]) for d in code_counts)

    misplaced = total_matches - exact

    return [exact, misplaced]


def play_game():
    print("Welkom bij Mastermind!")
    print("De computer kiest een geheime code van 4 cijfers (tussen 1 en 6).")
    print("Jouw taak: raad de code!")
    print("Na elke gok krijg je feedback: [exact, misplaced].")
    print("Exact = juiste cijfer op juiste plaats.")
    print("Misplaced = juiste cijfer op verkeerde plaats.\n")

    code = [random.randint(1, 6) for _ in range(4)]

    attempts = 0

    while True:
        attempts += 1
        guess_str = input(
            f"Poging {attempts} - Geef je gok (4 cijfers, bv. 1234): ")

        if guess_str.lower() == "stop":
            print("Je hebt het spel gestopt.")
            break
        if len(guess_str) != 4 or not guess_str.isdigit():
            print("Ongeldige invoer! Typ precies 4 cijfers (1-6).")
            continue

        guess = [int(ch) for ch in guess_str]

        feedback = mastermind(code, guess)
        print("Feedback:", feedback)

        if feedback[0] == 4:
            print(
                f"Gefeliciteerd! Je hebt de code geraden in {attempts} pogingen!")
            break


play_game()

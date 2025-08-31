import random

wallet = 250
card_values = {'7': 7, '8': 8, '9': 9, 'J': 1, 'Q': 2, 'K': 3, 'A': 1}
deck = list(card_values.keys()) * 4
random.shuffle(deck)

player = []
bank = []


def deal_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    bank_hand = [deck.pop(), deck.pop()]
    return player_hand, bank_hand


def calculate_score(hand):
    return sum(card_values[card] for card in hand)


def get_bet(wallet):
    while True:
        try:
            bet = int(input(f"How much do you want to bet? (1 - {wallet}): "))
            if 1 <= bet <= wallet:
                return bet
            else:
                print(f"Please make a bet between 1 and {wallet}")
        except ValueError:
            print("Please enter a valid number.")


def player_turn(deck, player_hand):
    while True:
        choice = input("Would you like to draw or pass? ").lower()
        if choice == 'draw':
            player_hand.append(deck.pop())
            print("Your hand:", player_hand, "Score:",
                  calculate_score(player_hand))
            if calculate_score(player_hand) >= 21:
                print("You reached 21 or more!")
                break
        elif choice == 'pass':
            break
        else:
            print('Please enter "draw" or "pass"')


def bank_turn(deck, bank_hand):
    while calculate_score(bank_hand) < 17:
        bank_hand.append(deck.pop())
        print("Bank draws a card:", bank_hand,
              "Score:", calculate_score(bank_hand))
    print("Bank stops with score:", calculate_score(bank_hand))


def compare_scores(player_hand, bank_hand, bet, wallet):
    player_score = calculate_score(player_hand)
    bank_score = calculate_score(bank_hand)

    if player_score > 21:
        print("You busted! You lose your bet.")
        wallet -= bet
    elif bank_score > 21 or player_score > bank_score:
        print("You win! You get double your bet.")
        wallet += bet
    elif player_score == bank_score:
        print("Draw! You get your bet back.")
    else:
        print("You lose! Better luck next time.")
        wallet -= bet

    return wallet


# game flow:

while wallet > 0:
    print("\n--- New Round ---")
    deck = list(card_values.keys()) * 4
    random.shuffle(deck)

    player, bank = deal_cards(deck)
    print("Your hand:", player, "Score:", calculate_score(player))
    print("Bank shows:", bank[0], "?")

    bet = get_bet(wallet)

    player_turn(deck, player)
    bank_turn(deck, bank)

    wallet = compare_scores(player, bank, bet, wallet)
    print("Wallet:", wallet)

    if wallet <= 0:
        print("You are out of money! Game over.")
        break

    again = input("Play another round? (y/n): ").lower()
    if again != "y":
        break

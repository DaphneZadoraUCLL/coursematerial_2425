# --- Tic Tac Toe Game ---

# ANSI escape codes voor kleuren
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"

# --- Functies ---


def display_board(board, player_symbols_colors):
    """Display the Tic Tac Toe board with colors for clarity."""
    print("\n")
    for i in range(3):
        row = []
        for j in range(3):
            idx = 3*i + j
            if board[idx] == " ":
                # Vrij vak: toon het nummer in blauw
                row.append(f"{BLUE}{idx}{RESET}")
            else:
                # Bezet vak: toon symbool in de kleur van de speler
                color = player_symbols_colors.get(board[idx], RESET)
                row.append(f"{color}{board[idx]}{RESET}")
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print("\n")


def display_indices():
    """Display the board indices for reference at the start."""
    indices = list(range(9))
    print("\nBoard indices:")
    print(f"{indices[0]} | {indices[1]} | {indices[2]}")
    print("--+---+--")
    print(f"{indices[3]} | {indices[4]} | {indices[5]}")
    print("--+---+--")
    print(f"{indices[6]} | {indices[7]} | {indices[8]}")
    print("\n")


def player_move(player_name, symbol, board):
    """Ask the player to make a move, with input validation and quit option."""
    while True:
        move_input = input(
            f"{player_name}, choose a cell (0-8) or 'q' to quit: ")
        if move_input.lower() in ("q", "quit"):
            print("Game stopped by player. Exiting...")
            exit()
        try:
            move = int(move_input)
            if move < 0 or move > 8:
                print("Invalid cell. Choose a number between 0 and 8.")
            elif board[move] != " ":
                print("Cell already occupied. Choose a different cell.")
            else:
                board[move] = symbol
                break
        except ValueError:
            print("Invalid input. Enter an integer between 0 and 8, or 'q' to quit.")


def check_winner(board, symbol):
    """Check if the given symbol has won the game."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False


def check_tie(board):
    """Check if the board is full without any winner."""
    return " " not in board


# --- Game Setup ---
print("Welcome to Tic Tac Toe!\n")

player1_name = input("Enter Player 1 name: ")
player1_symbol = input(
    f"{player1_name}, choose your symbol (X or O): ").upper()

player2_name = input("Enter Player 2 name: ")
player2_symbol = input(
    f"{player2_name}, choose your symbol (different from {player1_symbol}): ").upper()
while player2_symbol == player1_symbol:
    player2_symbol = input(
        f"Symbol already taken. {player2_name}, choose a different symbol: ").upper()

# Kleuren toewijzen aan spelers
player_symbols_colors = {
    player1_symbol: RED,
    player2_symbol: GREEN
}

# Initialize board
board = [" "] * 9
display_indices()

# --- Game Loop ---
current_player = 1
while True:
    display_board(board, player_symbols_colors)

    if current_player == 1:
        player_move(player1_name, player1_symbol, board)
        if check_winner(board, player1_symbol):
            display_board(board, player_symbols_colors)
            print(f"Congratulations {player1_name}, you win!")
            break
        current_player = 2
    else:
        player_move(player2_name, player2_symbol, board)
        if check_winner(board, player2_symbol):
            display_board(board, player_symbols_colors)
            print(f"Congratulations {player2_name}, you win!")
            break
        current_player = 1

    if check_tie(board):
        display_board(board, player_symbols_colors)
        print("It's a tie!")
        break

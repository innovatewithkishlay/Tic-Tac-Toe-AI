# utils.py

def print_board(board):
    """Pretty-print the board with numbers for empty spots."""
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            val = board[i + j] if board[i + j] != ' ' else str(i + j + 1)
            row.append(val)
        print(' | '.join(row))
        if i < 6:
            print('-' * 9)

def get_player_move(board):
    """
    Prompt the user for a move, validate, and return as an index (0-8).
    """
    while True:
        try:
            user_input = input("Enter your move (1-9): ")
            move = int(user_input) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Position taken or out of range. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

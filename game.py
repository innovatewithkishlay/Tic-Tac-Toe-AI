# game.py

def create_board():
    """Create a 3x3 Tic-Tac-Toe board initialized with empty spaces."""
    return [' ' for _ in range(9)]

def display_board(board):
    """Display the Tic-Tac-Toe board in a 3x3 grid format."""
    for i in range(0, 9, 3):
        print(' | '.join(board[i:i+3]))
        if i < 6:
            print('-' * 9)

def is_valid_move(board, move):
    """Check if the move (0-8) is valid (empty position on board)."""
    return 0 <= move <= 8 and board[move] == ' '

def place_move(board, move, player):
    """Place player's move ('X' or 'O') on the board at the given move index."""
    if is_valid_move(board, move):
        board[move] = player
        return True
    return False

def check_winner(board, player):
    """Check if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    """Check if the board is full (no empty spaces)."""
    return all(space != ' ' for space in board)

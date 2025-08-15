# ai.py

import math

def minimax(board, depth, is_maximizing, player, opponent):
    """
    Minimax algorithm to choose the best move for the AI.
    """
    if check_winner(board, player):
        return 10 - depth
    elif check_winner(board, opponent):
        return depth - 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                score = minimax(board, depth + 1, False, player, opponent)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = opponent
                score = minimax(board, depth + 1, True, player, opponent)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board, player, opponent):
    """
    Find the best move for the AI to make using the minimax algorithm.
    """
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            score = minimax(board, 0, False, player, opponent)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# We need to import check_winner and is_board_full from game.py
from game import check_winner, is_board_full

# main.py

from game import create_board, place_move, check_winner, is_board_full
from utils import print_board, get_player_move
from ai import find_best_move

def play_game():
    board = create_board()
    human = 'X'
    ai_player = 'O'
    current_player = human

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == human:
            print("Your turn.")
            move = get_player_move(board)
            place_move(board, move, human)
        else:
            print("AI's turn.")
            move = find_best_move(board, ai_player, human)
            place_move(board, move, ai_player)

        print_board(board)

        if check_winner(board, current_player):
            if current_player == human:
                print("Congratulations! You won!")
            else:
                print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = ai_player if current_player == human else human

if __name__ == "__main__":
    play_game()

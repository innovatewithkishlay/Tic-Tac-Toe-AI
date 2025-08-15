from flask import Flask, render_template, request, jsonify, session
from game import create_board, place_move, check_winner, is_board_full
from ai import find_best_move

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

def get_board():
    return session.get("board", create_board())

def save_board(board):
    session["board"] = board

def current_player():
    # Alternate based on number of moves
    board = get_board()
    if board.count('X') == board.count('O'):
        return 'X'
    else:
        return 'O'

@app.route('/', methods=["GET", "POST"])
def index():
    board = get_board()
    winner = None
    message = None

    if request.method == "POST":
        move = int(request.form['move'])
        player = current_player()

        if place_move(board, move, player):
            # Check for winner after player move
            if check_winner(board, player):
                winner = player
                message = f"{player} wins!"
            elif is_board_full(board):
                message = "It's a tie!"
            else:
                # If it's human's move, now it's AI's turn
                if player == 'X':
                    ai_move = find_best_move(board, 'O', 'X')
                    if place_move(board, ai_move, 'O'):
                        if check_winner(board, 'O'):
                            winner = 'O'
                            message = "O wins!"
                        elif is_board_full(board):
                            message = "It's a tie!"
        save_board(board)

    # For GET or after POST, reset session if game over
    if message or winner:
        session.pop("board", None)

    return render_template("index.html", board=board, message=message)

@app.route('/reset')
def reset():
    session.pop("board", None)
    return ('', 204)  # No Content

if __name__ == '__main__':
    app.run(debug=True)

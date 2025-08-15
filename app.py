from flask import Flask, render_template, request, jsonify, session
from game import create_board, place_move, check_winner, is_board_full
from ai import find_best_move

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_board():
    return session.get('board', create_board())

def save_board(board):
    session['board'] = board

def find_winning_combo(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return combo
    return []

@app.route('/')
def index():
    board = get_board()
    message = None
    winning_combo = []
    return render_template(
        'index.html', 
        board=board, 
        message=message, 
        winning_combo=winning_combo
    )

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    move = data.get('move')
    board = get_board()
    message = None
    winning_combo = []
    # Human move = X
    if board[move] == ' ':
        place_move(board, move, 'X')
        if check_winner(board, 'X'):
            message = "You win! 🎉"
            winning_combo = find_winning_combo(board, 'X')
        elif is_board_full(board):
            message = "It's a tie!"
        else:
            # AI move
            ai_move = find_best_move(board, 'O', 'X')
            if ai_move is not None and ai_move != -1:
                place_move(board, ai_move, 'O')
                if check_winner(board, 'O'):
                    message = "AI wins, but no worries—try again! 🤖"
                    winning_combo = find_winning_combo(board, 'O')
                elif is_board_full(board):
                    message = "It's a tie!"
    save_board(board)
    return jsonify({'board': board, 'message': message, 'winning_combo': winning_combo})

@app.route('/reset', methods=['POST'])
def reset():
    session['board'] = create_board()
    return jsonify({'board': session['board']})

if __name__ == '__main__':
    app.run(debug=True)

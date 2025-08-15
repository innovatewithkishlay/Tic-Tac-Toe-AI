import tkinter as tk
from tkinter import messagebox
from game import create_board, place_move, check_winner, is_board_full
from ai import find_best_move

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe AI")
        self.board = create_board()
        self.buttons = []
        self.human = 'X'
        self.ai_player = 'O'
        self.current_player = self.human

        self.status_label = tk.Label(self.master, text="Your Turn", font=('Arial', 16))
        self.status_label.pack(pady=8)

        self.create_widgets()
        self.reset_button = tk.Button(self.master, text="Restart", font=('Arial', 12), command=self.reset_game)
        self.reset_button.pack(pady=4)

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg='#e6f2ff', padx=10, pady=10)
        self.frame.pack()
        for i in range(9):
            btn = tk.Button(self.frame, text=' ', font=('Arial', 32, 'bold'), width=4, height=2,
                            command=lambda i=i: self.on_button_click(i), bg="#cccccc", fg="#333")
            btn.grid(row=i//3, column=i%3, padx=4, pady=4)
            self.buttons.append(btn)

    def on_button_click(self, index):
        if self.board[index] == ' ' and self.current_player == self.human:
            place_move(self.board, index, self.human)
            self.update_buttons()
            if check_winner(self.board, self.human):
                self.status_label.config(text="You won!")
                self.highlight_winner(self.human)
                self.disable_all_buttons()
            elif is_board_full(self.board):
                self.status_label.config(text="It's a tie!")
                self.disable_all_buttons()
            else:
                self.current_player = self.ai_player
                self.status_label.config(text="AI's Turn")
                self.master.after(500, self.ai_turn)

    def ai_turn(self):
        move = find_best_move(self.board, self.ai_player, self.human)
        if move != -1:
            place_move(self.board, move, self.ai_player)
            self.update_buttons()
        if check_winner(self.board, self.ai_player):
            self.status_label.config(text="AI wins!")
            self.highlight_winner(self.ai_player)
            self.disable_all_buttons()
        elif is_board_full(self.board):
            self.status_label.config(text="It's a tie!")
            self.disable_all_buttons()
        else:
            self.current_player = self.human
            self.status_label.config(text="Your Turn")

    def update_buttons(self):
        for i in range(9):
            ch = self.board[i]
            self.buttons[i]['text'] = ch
            self.buttons[i]['state'] = 'normal' if ch == ' ' else 'disabled'
            # Change color for X and O
            if ch == 'X':
                self.buttons[i]['fg'] = '#1a75ff'
            elif ch == 'O':
                self.buttons[i]['fg'] = '#ff3333'
            else:
                self.buttons[i]['fg'] = '#333'

    def highlight_winner(self, player):
        winners = self.get_winning_cells(player)
        for idx in winners:
            self.buttons[idx]['bg'] = '#ffff99'

    def get_winning_cells(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_conditions:
            if all(self.board[i] == player for i in combo):
                return combo
        return []

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn['state'] = 'disabled'

    def reset_game(self):
        self.board = create_board()
        self.current_player = self.human
        self.status_label.config(text="Your Turn")
        for btn in self.buttons:
            btn['bg'] = "#cccccc"
            btn['state'] = 'normal'
            btn['text'] = ' '
            btn['fg'] = '#333'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

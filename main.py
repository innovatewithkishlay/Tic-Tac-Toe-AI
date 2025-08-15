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
        
        self.create_widgets()
        self.update_buttons()

    def create_widgets(self):
        frame = tk.Frame(self.master)
        frame.pack()
        
        for i in range(9):
            btn = tk.Button(frame, text=' ', font=('Arial', 24), width=5, height=2,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_button_click(self, index):
        if self.board[index] == ' ' and self.current_player == self.human:
            place_move(self.board, index, self.human)
            self.update_buttons()
            if check_winner(self.board, self.human):
                messagebox.showinfo("Game Over", "You won!")
                self.reset_game()
            elif is_board_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = self.ai_player
                self.master.after(500, self.ai_turn)

    def ai_turn(self):
        move = find_best_move(self.board, self.ai_player, self.human)
        if move != -1:
            place_move(self.board, move, self.ai_player)
            self.update_buttons()

        if check_winner(self.board, self.ai_player):
            messagebox.showinfo("Game Over", "AI wins!")
            self.reset_game()
        elif is_board_full(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = self.human

    def update_buttons(self):
        for i in range(9):
            self.buttons[i]['text'] = self.board[i]
            self.buttons[i]['state'] = 'normal' if self.board[i] == ' ' else 'disabled'

    def reset_game(self):
        self.board = create_board()
        self.current_player = self.human
        self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()

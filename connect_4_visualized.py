import tkinter as tk
from tkinter import messagebox


class Connect4GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect 4")
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [
            [tk.Button(self.master, text='', width=5, height=2, command=lambda col=col: self.drop_token(col))
             for col in range(7)] for _ in range(6)]

        for row in range(6):
            for col in range(7):
                self.buttons[row][col].grid(row=row, column=col)

    def drop_token(self, col):
        for row in range(5, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                self.buttons[row][col]['text'] = self.current_player
                if self.check_winner(self.current_player):
                    messagebox.showinfo("Connect 4", f"Player {self.current_player} wins!")
                    self.reset_board()
                elif self.is_board_full():
                    messagebox.showinfo("Connect 4", "It's a tie!")
                    self.reset_board()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
                break

    def check_winner(self, player):
        # Check horizontally
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][
                    col + 3] == player:
                    return True

        # Check vertically
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][
                    col] == player:
                    return True

        # Check diagonally (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == \
                        self.board[row + 3][col + 3] == player:
                    return True

        # Check diagonally (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == \
                        self.board[row - 3][col + 3] == player:
                    return True

        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def reset_board(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        for row in range(6):
            for col in range(7):
                self.buttons[row][col]['text'] = ''


if __name__ == "__main__":
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()

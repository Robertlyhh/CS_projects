def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 29)


def check_winner(board, player):
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == player:
                return True

    # Check vertically
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == player:
                return True

    # Check diagonally (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][
                col + 3] == player:
                return True

    # Check diagonally (bottom-left to top-right)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][
                col + 3] == player:
                return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def connect4():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            col = int(input(f"Player {current_player}, choose a column (0-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= col <= 6:
            for row in range(5, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    if check_winner(board, current_player):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        return
                    elif is_board_full(board):
                        print_board(board)
                        print("It's a tie!")
                        return
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
                    break
            else:
                print("Column is full. Please choose another column.")
        else:
            print("Invalid column. Please choose a number between 0 and 6.")


if __name__ == "__main__":
    connect4()

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == ' ':
                board[row][col] = current_player
                if check_winner(board):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. The cell is already occupied. Try again.")
        else:
            print("Invalid move. Please enter a number between 0 and 2 for both row and column.")


if __name__ == "__main__":
    tic_tac_toe()

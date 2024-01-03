import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}




def check_win(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in range(1, len(columns)):
            if columns[column][line] != symbol:
                break
        else:
            print("You won on line " + str(line + 1) + " with " + str(symbol) + "!")
            winnings += bet * values[symbol]
    
    return winnings


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            random_symbol = random.choice(current_symbol)
            current_symbol.remove(random_symbol)
            column.append(random_symbol)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:   
                print("Invalid amount. Please try again.")
        else:
            print("please enter a valid amount, which should be a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet: (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print("Invalid number of lines. Please try again.")
        else:
            print("Please enter a valid number of lines, which should be a number.")


    return lines


def get_bet():
    while True:
        bet = input("Enter bet amount on each line (" + str(MIN_BET) + "-" + str(MAX_BET) + "): ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print("Invalid bet amount. Please try again.")
        else:
            print("Please enter a valid bet amount, which should be a number.")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print("You don't have enough balance to bet. Please try again. Your current balance is: " + str(balance))
    
    print(f"You have deposited {balance} and bet {bet} on {lines} lines. Total bet is: {bet * lines}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_win(slots, lines, bet, symbol_value)
    print(f"You won {winnings}")
    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Your balance is: {balance}")
        if balance <= 0:
            print("You have no more balance. Game over.")
            break
        else:
            play_again = input("Do you want to play again? (Y/N) ")
            if play_again.lower() != "y":
                print("Thanks for playing!")
                break
        balance += spin(balance)

    print(f"Your final balance is: {balance}")



main()
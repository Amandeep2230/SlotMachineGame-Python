from curses.ascii import isdigit
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winnings_lines.append(line+1)
    return winnings, winnings_lines

def get_slot_machine_spin(ROWS, COLS, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(COLS):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    #transposing the columns matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

def dep():
    while True:
        deposit = input("What would you like to deposit? $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Invalid Input: Deposit should be greater than zero!")
        else:
            print("Invalid Input: Deposit should be a number!")
    return deposit

def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Invalid Input: Number of lines should be greater than zero!")
        else:
            print("Invalid Input: Number of lines should be a number!")
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid Input: Bet must be between ${MIN_BET} - ${MAX_BET}!")
        else:
            print("Invalid Input: Bet should be a number!")
    return bet

def spin(balance):
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet>balance:
            print(f"You don't have enough funds to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winnings_lines)    # * is the unpack operator
    return winnings - total_bet

def main():
    balance = dep()
    while True:
        print(f"Current balance is ${balance}")
        ans=input("Press enter to play (q to quit): ")
        if ans == 'q':
            break
        balance += spin(balance)
    
    print(f"You are left with ${balance}")


main()
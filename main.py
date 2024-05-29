import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_value = {
    "$": 4,
    "?": 5,
    "!": 6,
    "*": 7
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range (lines):
        symbol = columns [0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if (i != len(columns)-1):
                print (column[row], end = " | ")
            else:
                print (column[row], end="")
        print ()

def deposit():
    while (True):
        amount = input ("Enter amount of money: $")
        if amount.isdigit():
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print ("Please enter a positive number.")
        else:
            print("Please enter a number.")
    return amount

def number_of_lines():
    while (True):
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break
            else:
                print("Please enter a number between 1-" + str(MAX_LINES))
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while (True):
        bet = input("Enter how much to bet on each line ("+ str(MIN_BET) + "-" + str(MAX_BET) + ")? ")
        if bet.isdigit():
            bet = int(bet)
            if (MIN_BET <= bet <= MAX_BET):
                break
            else:
                print("Please enter a number between " + str(MIN_BET) + "-" + str(MAX_BET))
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = number_of_lines()
    while (True):
        bet = get_bet()
        total_bet = bet * lines
        if (total_bet > balance):
            print("You do not have enough to bet that amount, your current balance is: " + str(balance))
        else:
            break

    print("You are betting $" + str(bet) + " on " + str(lines) + " lines. Total bet is equal to $" + str(total_bet))

    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won " + str(winnings))
    print("You won on lines: " + str(winning_lines))
    return winnings - total_bet

def main():
    balance = deposit()
    while (True):
        print ("Current balance is: $" + str(balance))
        answer = input("Press ENTER to spin. (q to quit)")
        if (answer == "q"):
            break
        else:
            balance += spin(balance)
        if (balance == 0):
            print("You lost all your money.")
            break

    print ("You left with $" + str(balance))
main()





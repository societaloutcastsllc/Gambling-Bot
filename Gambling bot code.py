#Project 2

import random


LINES_BET = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

get_symbol = {
    "A": 4,
    "B": 5, 
    "C": 7, 
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3, 
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symobl_to_check = column[line]
            if symbol != symobl_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, get_symbol in symbols.items():
        for _ in range(get_symbol):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns 

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" | ")
            else:
                print(column[row], end="")
        
        print()




def deposit():
    while True:
        amount = input('How much money you got? $ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('You can not play if you broke')
        else:
            print('A number dumbass' )

    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines you betting boy (1-" + str(LINES_BET) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= LINES_BET:
                break
            else:
                print(f'you can only pick 1 - {LINES_BET}')
        else:
            print('You gotta pick a valid number of lines')
    
    return lines

def get_bet():
    while True:
        bet_ting = input('what would you like to bet? $')
        if bet_ting.isdigit():
            bet_ting = int(bet_ting)
            if MIN_BET <= bet_ting <= MAX_BET:
                break
            else:
                print(f'amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('A number dumbass' )

    return bet_ting


def spin(balance):
    lines = get_number_of_lines()
    print(balance, lines)
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"you don't have enought money punk you only got ${balance}"
            )
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. Total bet will be ${total_bet}")

    slots = get_spin(ROWS, COLS, get_symbol)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}." )
    print(f"You wont on lines", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit() 
    while True:
        print(f"current balance is ${balance}")
        answer = input("press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f" You left with ${balance}")        

main()


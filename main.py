import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROW = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winning(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []     
    for symbol, symbol_count in symbols.items():     
        for _ in range (symbol_count):     
            all_symbols.append(symbol)     
     
    columns = []     
    for _ in range(cols):     
        column = []     
        current_symbols = all_symbols[:]     
        for _ in range(rows):     
            value = random.choice(current_symbols)     
            current_symbols.remove(value)     
            column.append(value)     
        columns.append(column)     
    return columns     
     
def display_machine(columns):     
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()

def deposite():
    while True:
        amount = input("Enter the amount you want to deposite: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must greater than $0")
        else:
            print("Please enter only numbers.")
    return amount

def number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on(1-"+ str(MAX_LINES)+ ") ?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid lines!")
        else:
            print("Please enter a number!")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must in berween ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter only numbers.")
    return amount

def game(balance):
    
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print(f"You do not have enough $ to bet that, Your current balance is {balance}$")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.Your total bet is ${total}")

    slots = get_slot_machine_spin(ROW,COLS,symbol_count)
    display_machine(slots)
    winnings,winning_lines = check_winning(slots,lines,bet,symbol_values)
    print(f'You won ${winnings}.')
    print(f"You won on lines:", *winning_lines)
    return winnings-total

def main():
    balance = deposite()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("press enter to play(q to quit)")
        if spin == 'q':
            break
        balance += game(balance)
    print(f"You balance with${balance}")


main()
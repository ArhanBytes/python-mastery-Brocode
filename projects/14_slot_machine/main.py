# SLOT MACHINE
import random

def interface():
    print("-----------------------------")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("-----------------------------")

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("-----------------------------")
    print(" | ".join(row)) # join the the elements of iterable seperated by " | "
    print("-----------------------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
    else:
        return 0
def main():
    balance = 100
    
    while balance > 0:
        interface()
        print(f"Current balance: ${balance}")
        # taking bet amount
        bet_amount = input("Place you bet amount: ")
        # if bet amount in other than digit
        if not bet_amount.isdigit():
            print(f"{bet_amount} is an invalid bet")
            continue
        bet_amount = int(bet_amount)
        
        if bet_amount <= 0:
            print("Bet amount should be greater than zero")
            continue
        if bet_amount > balance:
            print("Insufficient balance")
            continue
        
        balance -= bet_amount
        
        print("Spinnning.....\n")
        
        row = spin_row()
        print(row)
        payout = get_payout(row, bet_amount)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")
            
        balance += payout
        
        if not input("Do you want to play again (Y/N)? ").upper() == 'Y':
            break
    
    print("-----------------------------")
    print(f"Game Over! Your final balance is ${balance}")
    print("-----------------------------")

if __name__ == '__main__':
    main()

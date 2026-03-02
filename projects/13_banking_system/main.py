# BANKING SYSTEM PROGRAM

def overview():
    print("******************************")
    print("        Banking Program       ")
    print("******************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def show_balance(balance):
    print("******************************")
    print(f"Your current Balance: ${balance:.2f}")
    print("******************************")


def deposit(balance):
    print("******************************")
    amount = input("Enter a deposit amount: ")

    # Allow integers and floats (only one decimal point)
    if amount.replace(".", "", 1).isdigit():
        amount = float(amount)
        if amount < 0:
            print(f"{amount} is an invalid amount")
        else:
            balance += amount
            print(f"${amount:.2f} has been deposited.")
            print(f"Current Balance: ${balance:.2f}")
    else:
        print(f"{amount} is an invalid amount")

    print("******************************")
    return balance


def withdraw(balance):
    print("******************************")
    amount = input("Enter a withdraw amount: ")

    # Allow integers and floats (only one decimal point)
    if amount.replace(".", "", 1).isdigit():
        amount = float(amount)
        if amount < 0:
            print(f"{amount} is an invalid amount")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"${amount:.2f} has been withdrawn")
            print(f"Current Balance: ${balance:.2f}")
    else:
        print(f"{amount} is an invalid amount")

    print("******************************")
    return balance


def main():
    balance = 0
    is_running = True

    while is_running:
        overview()

        choice = input("Enter a choice (1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance = deposit(balance)
            case "3":
                balance = withdraw(balance)
            case "4":
                is_running = False
            case _:
                print(f"{choice} is an invalid choice.")

    print("Thanks for using BANKING SYSTEM")


if __name__ == '__main__':
    main()

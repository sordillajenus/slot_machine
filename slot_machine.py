MAX_LINES = 3
MAX_BET = 1000000000
MIN_BET = 1

def deposit():
    while True:
        amount = input("Please Enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Please enter a valid numerical amount.")
        else:
            print("Would you please enter a number?")        


def get_number_of_lines():
    while True:
        lines = input(f"Please enter a valid number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a digit.")   


def get_amount_of_bet():
    while True:
        bet = input("Please Enter a valid amount of bet on each line ₱: ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet   
            else:
                print(f"Amount must be between ₱{MIN_BET} - ₱{MAX_BET}")
        else:
            print("Please enter a number.")


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_amount_of_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is: ₱{balance}")
        else:
            break

    print(f"You are betting ₱{bet} on {lines} lines.")
    print(f"Total bet is: ₱{total_bet}")


main()
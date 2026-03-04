MAX_LINES = 3
MAX_BET = 1000000000
MIN_BET = 1

def deposit():
    while True:
        amount = input("Please Enter the amount you want to deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid numerical amount")
        else:
            print("Would you please enter a number?")        

    return amount     

def get_number_of_lines():
    while True:
        lines = input("Please enter a valid number of lines to bet on (1- " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= max_lines:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please Enter a digit")   

    return lines            

def get_amount_of_bet():
    while True:
        bet = input("Please Enter a valid amount of bet on each line ₱:")
        if bet.isdigit():
            bet = int(bet)
            if MAX_BET >= bet >= MIN_BET:
                break
            else:
                print(f"Amount must be between ₱{MIN_BET} - ₱{MAX_BET}")




def main():
    balance = deposit()
    lines =   get_number_of_lines
    bet = get_amount_of_bet
    total_bet = bet * lines
    print(f"You are betting ₱{bet} on {lines} lines. Total bet is: {total_bet}")
    
       
    

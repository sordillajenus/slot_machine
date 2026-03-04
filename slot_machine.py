max_lines = 3

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
        lines = input("Please enter a valid number of lines to bet on (1- " + str(max_lines) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= max_lines:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please Enter a digit")       



def main():
    balance = deposit()
    lines =   get_number_of_lines
    print = (balance, lines)    
    

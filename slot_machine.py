def deposit():
    while True:
        amount = input("Please Enter the amount you want to deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid numerical amount:")
        else:
            print("Would you please enter a number?")        

    return amount     

deposit()      
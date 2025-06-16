menu = """

[l] Lodgement
[w] withdraw
[s] statement
[e] exit

=>"""

amount = 0
limit = 500
bank_statement = ""
withdraw_amount = 0
WITHDRAW_LIMIT = 3

while True:
    option = input(menu) 

    if option == "l":
        value = float(input("Amount of your lodgement: "))

        if value > 0:
            amount += value
            bank_statement += f"lodgement of: £{value:.2f}\n"

        else:
            print("Operation failed: invalid value")
            

    elif option == "w":
        value = float(input("Inform withdraw amount: "))
        
        exceeded_amount = value > amount

        exceeded_limit = value > limit

        exceeded_withdraw = withdraw_amount >= WITHDRAW_LIMIT

        if exceeded_amount:
            print("opration failed1 You do not have sufficient amount")

        elif exceeded_limit:
            print("operation failed! the value exceeds the limit")

        elif exceeded_withdraw:
            print("Operation failed! Maximum number of withdraw reached")

        elif value > 0:
            amount -= value
            bank_statement += f"Withdraw: £{value:.2f}"
            withdraw_amount += 1


    elif option == "s":
        print("\n ================ Statement ================")
        print("There wasn't moviments done" if not bank_statement else bank_statement)
        print(f"\n Amount: £{amount:.2f}")
    
    elif option == "e":
        break

    else:
        print("Invalid option, please select again")


print(menu)
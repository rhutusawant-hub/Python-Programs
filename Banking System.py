
# Requirements:
# Use match-case for menu selection.
# Use if-else for balance validation.
# Use nested conditions for PIN verification.
# Prevent withdrawal when balance is insufficient.
# Display appropriate transaction messages.


bal = 2500
pin = 2108

print("""
===== BANKING SYSTEM =====
1. Check Balance
2. Deposit
3. Withdraw
4. Change PIN
5. Exit
===========================
""")

ch = int(input("Enter your choice : "))

match ch:
    case 1:
        entered_pin = int(input("Enter your pin : "))
        if entered_pin == pin:
            print(f"Your balance is rs {bal}")
        else:
            print("Incorrect pin! Please try again.")

    case 2:
        entered_pin = int(input("Enter your pin : "))
        if entered_pin == pin:
            dep = float(input("Enter your deposit amount : "))
            if dep > 0:
                print(f"Deposit Successfull!!")
                print(f"New balance = {bal+dep}")
            else:
                print("Invalid amount!")
        else:
            print("Incorrect pin! Please try again.")

    case 3:
        entered_pin = int(input("Enter your pin : "))
        if entered_pin == pin:
            wid = float(input("Enter your withdrawal amount : "))
            if bal >= 500:
                print("Withdrawal Successfull!!")
                print(f"New balance amount = {bal - wid}")
            else:
                print("Insufficient Balance :(")
        else:
            print("Incorrect pin! Please try again")

    case 4:
        entered_pin = int(input("Enter current pin : "))
        if entered_pin == pin:
            new_pin = int(input("Enter new pin : "))
            if new_pin >= 1000 and new_pin <=9999:
                pin = new_pin
                print("Pin has been successfully changed!")
            else:
                print("Invalid input(Enter pin between 1000-9999)")
        else:
            print("Incorrect pin! Please try again")

    case 5:
        print("Thank you!")

    case _:
        print("Invalid choice! Please try again.")
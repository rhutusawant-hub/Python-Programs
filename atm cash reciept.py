# 4. ATM Cash Withdrawal
#
# Accept:
#
# Account Holder Name
# Available Balance
# Withdrawal Amount
#
# Display:
#
# Remaining Balance
# Transaction Details



name  input("Enter the name of account holder : ")
balance = int(input("Enter available balance : "))
withdraw_amt = int(input("Enter your withdrawal amount : "))
rem = balance - withdraw_amt

print(f''' 
    -----------------------------------------
                ATM TRANSACTION 
    -----------------------------------------
      Date : 17/7/2026      Reciept Number:90
      
      \tAccount Holder :\t{name}
      \tWithdrawal Amount :\t{withdraw_amt}
      \tRemaining Balance :\t{rem}
    ------------------------------------------
    Thank You ! 

''')
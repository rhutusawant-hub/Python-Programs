# Accept principal, rate, and time and calculate simple interest and total amount.  

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"""Simple Interest: ₹{simple_interest:.2f}
Total Amount: ₹{total_amount:.2f}""")

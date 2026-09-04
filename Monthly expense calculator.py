# Create a Monthly Expense Calculator that accepts monthly income and expenses for rent, food, travel, education, 
# and entertainment. Display total expenses, remaining balance, and percentage of income spent.

monthly_income  = float(input("Enter your monthly income : "))
rent = float(input("Enter your rent expenses : "))
food = float(input("Enter your food expenses : "))
travel = float(input("Enter your travel expenses : "))
education = float(input("Enter your education expenses : "))
entertainment = float(input("Enter your entertainment expenses : "))

total = rent + travel + education + entertainment 
remaining_bal = monthly_income - total
percent = (total / monthly_income) * 100

print(f"""
      ----------Monthly Expense----------
      Monthly income = {monthly_income}
      Total expenses = {total}
      Remaining balance = {remaining_bal}
      Percent of income spent = {percent}
      -----------------------------------
      """)
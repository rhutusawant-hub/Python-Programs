# Create a Monthly Budget Calculator that accepts monthly income and expenses for rent, food, travel, education, 
# and entertainment. Display total expenses, savings, and percentage of income spent.

income = float(input("Enter monthly income: "))
rent = float(input("Enter rent expense: "))
food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
education = float(input("Enter education expense: "))
entertainment = float(input("Enter entertainment expense: "))

total_expenses = rent + food + travel + education + entertainment
savings = income - total_expenses
percentage_spent = (total_expenses / income) * 100

print(f"Total Expenses: ₹{total_expenses:.2f}")
print(f"Savings: ₹{savings:.2f}")
print(f"Percentage of Income Spent: {percentage_spent:.2f}%")   
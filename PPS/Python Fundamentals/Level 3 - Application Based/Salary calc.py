# Create a salary calculator that accepts basic salary, HRA, DA, and deductions and calculates net salary.  

basic_salary = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
deductions = float(input("Enter deductions: "))

gross_salary = basic_salary + hra + da
net_salary = gross_salary - deductions

print(f"Gross Salary: ₹{gross_salary:.2f}")
print(f"Net Salary: ₹{net_salary:.2f}")
# Create an employee salary calculator that accepts basic salary, HRA percentage, and allowance percentage and calculates gross salary.

basic_salary = float(input("Enter basic salary: "))
hra_percentage = float(input("Enter HRA percentage: "))
allowance_percentage = float(input("Enter allowance percentage: "))

hra = basic_salary * hra_percentage / 100
allowance = basic_salary * allowance_percentage / 100
gross_salary = basic_salary + hra + allowance

print(f"Basic Salary: ₹{basic_salary:.2f}")
print(f"HRA: ₹{hra:.2f}")
print(f"Allowance: ₹{allowance:.2f}")
print(f"Gross Salary: ₹{gross_salary:.2f}")
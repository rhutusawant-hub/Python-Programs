# Accept basic salary and percentage values for HRA and DA and calculate the employee's gross salary.

basic_salary = float(input("Enter basic salary: "))
hra_percentage = float(input("Enter HRA percentage: "))
da_percentage = float(input("Enter DA percentage: "))

hra = basic_salary * hra_percentage / 100
da = basic_salary * da_percentage / 100

gross_salary = basic_salary + hra + da

print(f"Gross Salary: ₹{gross_salary:.2f}")
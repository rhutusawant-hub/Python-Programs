# 4. Accept two numbers and display addition, subtraction, multiplication, and division.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter Second number : "))
sum = num1 + num2 
sub = num1 - num2 
mul = num1 * num2 
div = num1 / num2 
print(f"""
=======================
Addition is {sum}
Subtraction is {sub}
Multiplication is {mul}
Division is {div}
=======================
""")
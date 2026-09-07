# Accept two integers and exchange their values.

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

print(f"Before exchange: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

print(f"After exchange: num1 = {num1}, num2 = {num2}")
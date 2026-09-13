# Accept two integers from the user and display their sum, difference, product, quotient, and remainder.  

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient:.2f}")
print(f"Remainder: {remainder}")
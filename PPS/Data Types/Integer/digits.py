# Accept a three-digit integer and display its first, middle, and last digit.

number = int(input("Enter a three-digit integer: "))

first_digit = number // 100
middle_digit = (number // 10) % 10
last_digit = number % 10

print(f"First Digit: {first_digit}")
print(f"Middle Digit: {middle_digit}")
print(f"Last Digit: {last_digit}")
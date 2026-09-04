# 14. Accept a four-digit number and calculate the sum and average of its digits.
num = int(input("Enter a four-digit number: "))

D1 = num // 1000
D2 = (num // 100) % 10
D3 = (num // 10) % 10
D4 = num % 10

sum_digits = D1 + D2 + D3 + D4
average = sum_digits / 4

print(f"Sum of digits = {sum_digits}")
print(f"Average of digits = {average}")
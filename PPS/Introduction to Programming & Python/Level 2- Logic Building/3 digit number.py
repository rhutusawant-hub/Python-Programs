#13. Accept a three-digit number and calculate the sum of its digits.

num = int(input("Enter a three digit number : "))
D1 = num // 100
D2 = (num //10) % 10
D3 = num % 10
print(f"The sum of all three digits are : {D1 + D2 + D3}")
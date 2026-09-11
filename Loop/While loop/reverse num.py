# Q2. Reverse a Number
# Accept an integer and display its reverse.

num = int(input("Enter an integer: "))

reverse = 0

while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(f"Reverse = {reverse}")
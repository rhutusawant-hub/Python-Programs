# Q1. Count Digits
# Accept an integer and count the number of digits using a while loop.

num = int(input("Enter an integer: "))

count = 0

while num != 0:
    num = num // 10
    count = count + 1

print(f"Number of digits = {count}")
# Accept a number and create Boolean results for:
# Is it positive?
# Is it even?
# Is it divisible by 5?

number = int(input("Enter a number: "))

is_positive = number > 0
is_even = number % 2 == 0
is_divisible_by_5 = number % 5 == 0

print(f"""
Is Positive: {is_positive}
Is Even: {is_even}
Is Divisible by 5: {is_divisible_by_5}
""")

# Q3. Power Calculation
# Calculate a^b without using the ** operator.

a = int(input("Enter the base: "))
b = int(input("Enter the power: "))

result = 1
i = 1

while i <= b:
    result = result * a
    i = i + 1

print(f"Answer = {result}")
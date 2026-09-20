# Accept five numbers from the user and store them in a list. Display the largest and smallest values.

numbers = []

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

largest = max(numbers)
smallest = min(numbers)

print(f"""
Numbers: {numbers}
Largest Value: {largest}
Smallest Value: {smallest}
""")
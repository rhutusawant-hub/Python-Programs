# Create a student marks calculator that accepts marks of five subjects and displays total, average, and percentage.

marks = []

for i in range(5):
    mark = float(input(f"Enter marks of subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print(f"Marks: {marks}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
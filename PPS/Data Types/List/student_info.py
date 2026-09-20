# Create a student marks list and display:
# Highest mark
# Lowest mark
# Total
# Average
# Number of subjects

marks = [85, 78, 92, 88, 76, 90, 81, 95]

highest = max(marks)
lowest = min(marks)
total = sum(marks)
average = total / len(marks)
subjects = len(marks)

print(f"""
Highest Mark: {highest}
Lowest Mark: {lowest}
Total: {total}
Average: {average:.2f}
Number of Subjects: {subjects}
""")

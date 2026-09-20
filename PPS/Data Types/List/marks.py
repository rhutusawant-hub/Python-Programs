# 31. Create a list containing the marks of eight subjects and display the total and average.

marks = [85, 78, 92, 88, 76, 90, 81, 95]

sum = sum(marks)
total = len(marks) * 100
average = total / len(marks)

print(f"""
Marks: {sum} / {total}
Total: {total}
Average: {average:.2f}
""")
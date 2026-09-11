# **Q8. Student Marks Analyzer**

# Accept marks of N students using a loop and calculate:


# -
#   Total marks
# - Average marks
# - Highest marks
# - Lowest marks
# - Number of students who passed
#  - Number of students who failed


n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0

for mark in marks:
    if mark >= 35:
        passed += 1
    else:
        failed += 1


print(f"""
Total Marks: {total}
Average Marks: {average:.2f}
Highest Marks: {highest}
Lowest Marks: {lowest}
Students Passed: {passed}
Students Failed: {failed}
""")
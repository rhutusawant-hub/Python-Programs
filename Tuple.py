marks = (58, 96, 52, 85, 63, 63)

# 1. Display the mark of first and last subject
print(f"The Marks of first subject is : {marks[0]}")
print(f"The Marks of last subject is : {marks[-1]}")

# 2. Display the marks of the first three subjects using slicing.
print(f"The marks of first three subjects are :{marks[:3]}")

# 3. Check whether the mark 75 is present in the list using the membership operator (in).
print(f"Is mark 75 in the list? {75 in marks}")

# 4. Print the total number of subjects using len().
print(f"The total number of subjects are : {len(marks)}")

# 5. The index position of a specific mark using index()
print(f"The index position of mark 85 is {marks.index(85)}")

# 6. count how many times a mark 90 appears using count()
print(f"How many times the mark 90 appears? :{marks.count(90)}")

# 7. Display the entire tuple of marks
print(f"The final tuple is : {marks}")

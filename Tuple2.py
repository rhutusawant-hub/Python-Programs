
marks = (78, 92, 65, 88, 74)

# Print the highest mark
print(f"The highest marks are : {max(marks)}")

# Print the lowest mark
print(f"The lowest marks are : {min(marks)}")

# Print the total marks
print(f"The total obtained marks are : {sum(marks)}")

# Print the average
print(f"The average mark is : {sum(marks) / len(marks)}")

# Check whether 90 is present in the tuple
print(f"Is 90 present in the marks given : {90 in marks}")

# Find the index of 88
print(f"The index of mark 88 is {marks.index(88)}")

# Print the tuple in reverse order.
print(f"The tuple in reversed order is : {marks[::-1]}")
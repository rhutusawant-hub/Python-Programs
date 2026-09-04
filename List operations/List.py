# Tasks to Perform:

# 1. Create a list called marks containing marks of 8 subjects. Example: [78, 85, 92, 67, 88, 73, 90, 81]
marks=[78, 85, 92, 67, 88, 73, 90, 81]

# 2. Print the first mark and last mark using indexing as well as slicing.
print(f"The Marks of first subject is : {marks[0]}")
print(f"The Marks of last subject is : {marks[-1]}")

# 3. Display the marks of the first four subjects using slicing.
print(f"The marks of first four subjects are :{marks[:4]}")

# 4. Display the marks of the last three subjects using negative slicing.
print(f"Marks of last three subjects : {marks[-3:]}")

# 5. Display every second mark from the list using step slicing.
print(f"Every second mark is : {marks[::2]}")

# 6. Check whether the mark 90 is present in the list using the membership operator (in).
print(f"Is mark 90 in the list? {90 in marks}")

# 7. Add a new mark 95 to the list using a list method.
marks.append(95)
print(f"List after adding the mark 95 is : {marks} ")

# 8. Insert a mark 80 at index position 2 using insert().
marks.insert(2,80)
print(f"List after adding the mark 80 at index position 2 : {marks}")

# 9. Remove the lowest mark from the list.
marks.remove(min(marks)) 
print(f"List after removing the lowest mark is : {marks}")

# 10. Sort the marks in ascending order.
print(f"List in ascennding order is : {sorted(marks)}")

# 11. Reverse the list using a list method.
marks.reverse()
print(f"The reverse of the list is : {marks}")

# 12. Print the total number of marks using len().
print(f"The total number of marks are : {len(marks)}")

# 13. Print the maximum and minimum marks using max() and min().
print(f"The minimum mark is: {min(marks)}")
print(f"The maximum mark is: {max(marks)}")

# 14. Display the final updated marks list.
print(f"The Final updated list is : {marks}")
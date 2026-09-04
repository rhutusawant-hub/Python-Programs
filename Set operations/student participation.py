# 1. Write a Python program to analyze student participation using sets.

# Tasks to Perform:

# 1. Create two collections:
# A containing students who participated in Coding Club
# B containing students who participated in Sports Club
codingclub = {"Conrad","Belly","Jeremiah","taylor","steven"}
sportsclub = {"Garret","Hannah","Allie","Dean","Logan"}

# 2. Display both collections.
print(f"The people in coding club are : {codingclub}")
print(f"The people in sports club are : {sportsclub}")

# 3. Add a few duplicate student names in any one collection and display it again.
sportsclub.update(["Garret","Hannah"])
print(f"The new collection is : {sportsclub} ")

# # 4. Try to access an element using index and observe what happens.
# print(f"Name on index no 3 is : {codingclub[3]}")

# 5. Add a new student "Rahul" to collection A.
codingclub.add("Rahul")
print(f"The collection after adding Rahul to coding club is : {codingclub}")

# 6. Add multiple students "Amit" and "Neha" to collection B.
sportsclub.add("Amit")
sportsclub.add("Neha")
print(f"The collection after adding amit and neha to the sports club is : {sportsclub} ")

# 7. Remove a student "Amit" from collection B.
sportsclub.remove("Amit")
print(f"The collection after removing Amit from sports club is : {sportsclub}")

# 8. Remove any one random student from collection A.
codingclub.pop()
print(f"The collection after removing a random name form coding club is {codingclub}")

# 9. Create a new collection containing students who are in both activities.
intersection = codingclub.intersection(sportsclub)
print(f"Students in both clubs : {set(intersection)}")

# 10. Create a new collection containing students who are in at least one activity.
union = codingclub.union(sportsclub)
print(f"Students who are atlest in one activity : {set(union)}")

# 11. Create a collection of students who are in Coding Club but not in Sports Club.
diff = codingclub.difference(sportsclub)
print(set(diff))

# 12. Create a collection of students who are in only one of the two activities.
symmetric_diff = codingclub.symmetric_difference(sportsclub)
print(f"Students in only one club: {symmetric_diff}")

# 13. Check whether all students of A are present in B.
print(f"Are all coding club students in sports club? : {codingclub.issubset(sportsclub)}")

# 14. Check whether B completely contains A.
print(f"Does sports club completely contain coding club? : {sportsclub.issuperset(codingclub)}")

# 15. Check whether both collections have no common students.
print(f"Do both clubs have no common students? : {codingclub.isdisjoint(sportsclub)}")

# 16. Display the final collections.
print(f"""
Final collections : 
Coding club - {codingclub}
Sports Club - {sportsclub}'
""")
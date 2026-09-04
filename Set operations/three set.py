# 2. Write a Python program to analyze student participation in Python Course, Java Course, and AI Club using sets.

# Tasks to Perform:

# 1. Create three sets:
python_course = {"Rahul", "Amit", "Neha", "Sneha", "Karan", "Pooja"}
java_course = {"Amit", "Neha", "Rohan", "Priya", "Karan", "Suresh"}
ai_club = {"Neha", "Sneha", "Priya", "Rahul", "Karan", "Meena"}

# 2. Display all three collections.
print(f"""Students in Python : {set(python_course)} 
Students in Java : {set(java_course)}
Students in Ai : {set(ai_club)}
    """)
# 3. Add repeated student names in any one collection and display it again.
repeated = python_course.intersection(java_course,ai_club)
print(f"1)Repeated students from all the courses : {set(repeated)}\n")

# 4. Try to access an element using position and observe the result.
# print({ai_club[1]})

# 5. Add a new student "Deepak" to the Python course.
python_course.add("Deepak")
print(f"2)List after adding deepak to python course : {set(python_course)}\n")

# 6. Add multiple students "Arjun" and "Pooja" to the Java course.
java_course.add("Arjun")
java_course.add("Pooja")
print(f"3)List after adding Arjun and pooja in Java course is : {set(java_course)}\n")

# 7. Remove a student "Amit" from the Java course.
java_course.remove("Amit")  
print(f"4)List after removing Amit is : {set(java_course)}\n")

# 8. Remove any one random student from the AI club.
ai_club.pop()
print(f"5)Ai club list after removing a random student is : {set(ai_club)}\n")

# 9. Create a new collection containing students enrolled in both Python and Java.
both_py_java = python_course.intersection(java_course)
print(f"6)List of students enrolled in both Python and Java : {set(both_py_java)}\n")

# 10. Create a new collection containing students enrolled in both Java and AI Club.
both_java_ai = java_course.intersection(ai_club)
print(f"7)List of students enrolled both in Java and AI club is : {set(both_java_ai)}\n")

# 11. Create a new collection containing students enrolled in all three.
all_three = python_course.intersection(java_course,ai_club)
print(f"8)List of students enrolled in all the courses : {set(all_three)}\n")

# 12. Create a new collection containing students enrolled in at least one.
atleast_one = python_course | java_course | ai_club
print(f"9)Students who have enrolled in atleast one course are : {set(atleast_one)}\n")

# 13. Create a new collection containing students enrolled in Python only.
only_py = python_course.difference(java_course,ai_club)
print(f"10)Students who have enrolled in python only are : {only_py}\n")

# 14. Create a new collection containing students enrolled in Java only.
only_java = java_course.difference(python_course,ai_club)
print(f"11)Students who have enrolled in Java only are : {only_java}\n")

# 15. Create a new collection containing students enrolled in AI Club only.
only_AI = ai_club.difference(python_course,java_course)
print(f"12)Students who have enrolled in Ai club only are : {only_AI}\n")

# 16. Create a new collection containing students enrolled in exactly one of Python and Java.
exactly_one_python_java = python_course.symmetric_difference(java_course)
print(f"13)Students in exactly one of Python and Java : {exactly_one_python_java}\n")

# 17. Create a new collection containing students enrolled in exactly one of all three groups.
exactly_one_all_three = python_course.difference(java_course,ai_club)
print(f"14)students enrolled in exactly one of all three groups : {exactly_one_all_three}\n")

# 18. Create a new collection containing students enrolled in at least two groups.
at_least_two = (python_course & java_course) | (python_course & ai_club) | (java_course & ai_club)
print(f"15)Students enrolled in at least two groups : {at_least_two}\n")

# 19. Create a new collection containing students enrolled in Python and Java but not AI Club.
py_java = python_course&java_course
not_ai = py_java - ai_club
print(f"16)students enrolled in Python and Java but not AI Club : {not_ai}\n")

# 20. Create a new collection containing students enrolled in Java and AI Club but not Python.
ai_java = ai_club&java_course
not_py = ai_java - python_course
print(f"17)students enrolled in Ai and Java but not AI Club : {not_py}\n")

# 21. Create a new collection containing students enrolled in Python or AI Club but not Java.
ai_py = ai_club|python_course
not_java = ai_py - java_course
print(f"18)students enrolled in Python or Ai but not java : {not_java}\n")

# 22. Check whether all Python students are also in Java.
py_and_java = python_course<=java_course
print(f"19)Whether all python students are in java : {py_and_java}\n")

# 23. Check whether Java completely contains Python.
if python_course.issubset(java_course):
    print("20)Java completely contains Python\n")
else:
    print("20)Java does not completely contain Python\n")

# 24. Check whether Python and AI Club have no common students.
if python_course.isdisjoint(ai_club):
    print("21)Python and AI Club have no common students\n")
else:
    print("21)Python and AI Club have common students\n")

# 25. Check whether Java and AI Club are exactly equal.
if java_course == ai_club:
    print("22)Java and AI Club are exactly equal\n")
else:
    print("22)Java and AI Club are not exactly equal\n")

# 26. Check whether students common in Python and Java are completely present in AI Club.
common_students = python_course & java_course
if common_students.issubset(ai_club):
    print("23)All common Python and Java students are present in AI Club\n")
else:
    print("23)Not all common Python and Java students are present in AI Club\n")

# 27. Check whether AI Club students are completely present in students enrolled in at least one course.
at_least_one = python_course | java_course
if ai_club.issubset(at_least_one):
    print("24)All AI Club students are present in at least one course\n")
else:
    print("24)Not all AI Club students are present in at least one course\n")

# 28. Check whether any two collections have no common students.
if python_course.isdisjoint(java_course):
    print("25)Python and Java have no common students\n")

if python_course.isdisjoint(ai_club):
    print("26)Python and AI Club have no common students\n")

if java_course.isdisjoint(ai_club):
    print("27)Java and AI Club have no common students\n")

# 29. Display the size of each collection.
print(f"28)Number of students in Python course : {len(python_course)}")
print(f"29)Number of students in Java course : {len(java_course)}")
print(f"30)Number of students in Ai club : {len(ai_club)}\n")

# 30. Create one collection containing students who are not common in any pair.
not_common = (python_course | java_course | ai_club) - ((python_course & java_course) |(python_course & ai_club) |(java_course & ai_club))
print(f"31)Students not common in any pair : {not_common}\n")

# 31. Display the final updated collections.
print(f"32)Final list of students in Python Course : {python_course}\n")
print(f"33)Final list of students in Java Course : {java_course}\n")
print(f"34Final list of students in AI Club : {ai_club}")
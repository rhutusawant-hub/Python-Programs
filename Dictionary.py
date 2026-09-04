# Write a Python program to manage employee details using a dictionary.

# Tasks to Perform:

# 1. Create a collection called employee containing employee id, name, department, salary, and city.

employee = {
    "Employee id" : "00124",
    "Name" : "Rhutu",
    "Department" : "CSE",
    "Salary" : 100000,
    "City" : "Mumbai"
}
# 2. Display the complete collection.
print(f"1) The collection is : {employee}\n")

# 3. Display only the employee name and salary.
print(f"2) The employee name is {employee["Name"]} and their salary is {employee["Salary"]}\n")

# 4. Check whether the key "department" exists in the collection.
print(f"3) Does the key department exists in the collection : {"Department" in employee}\n")

# 5. Add a new detail "designation" with a suitable value.
employee.update({"Designation" : "Software Engineer" }) 
print(f"4) The updated collection after adding designation is : {employee}\n")

# 6. Update the employee salary with a new value.
employee["Salary"] = 150000
print(f"5) The collection after updating salary  is : {employee}\n")

# 7. Remove the "city" detail from the collection.
employee.pop("City")
print(f"6) The updated collection after removing city is : {employee}\n")

# 8. Display all the keys separately.
print(f"7) All the keys are : {employee.keys()}\n")

# 9. Display all the values separately.
print(f"8) All the values are : {employee.values()}\n")

# 10. Create another collection containing experience and joining year, then combine it with the existing collection.
employee_new = {
    "experience" : "5 years",
    "Joining year" :  2020
}
employee_final = employee | employee_new
print(f"9) The updated collection is : {employee_final}\n")

# 11. Display all key-value pairs separately.
print(f"10) All the key value pairs are : {employee_final.items()}\n")

# 12. Create a duplicate copy of the collection.
copy = employee_final.copy()
print(f"11) A duplicate copy of the collection is : {copy}\n")

# 13. Remove the last inserted detail from the copied collection.
employee_final = employee_final.popitem()
print(f"12) The collcetion after removing the last added detail is : {employee_final}\n")

# 14. Clear all details from the copied collection.
copy = copy.clear()
print(f"13) The copy collection after clering all details is : {copy}\n")

# 15. Display the final updated original collection.
print(f"14) The final updated original collection is : {employee_final}\n")
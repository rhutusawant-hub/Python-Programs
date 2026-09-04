# 1. Write a Python program to accept a student's name, college, and city from the user. Perform the following operations:

name = input("Enter the student's name: ")
college = input("Enter the college name: ")
city = input("Enter the city: ")

# Display the original details.
print(f"Students Name : {name}")
print(f"College : {college}")
print(f"City : {city}")


# Display the name in uppercase
print(f"Student's name in uppercase : {name.upper()}")

# Display the college name in lowercase.
print(f"College name in lowercase : {college.lower()}")

# Display the city in title case.
print(f"City name in title case : {city.title()}")

# Display the total number of characters in the student's name.
print(f"Total number of characters in the student's name : {len(name)}")

# Display the first and last characters of the student's name.
print(f"First character of the student's name : {name[0]}")
print(f"Last character of the student's name : {name[-1]}")

# Display the student's name in reverse order.
print(f"Student's name in reverse order : {name[::-1]}")

# Check whether the student's name starts with the letter A.
check1=name
if check1[0]=="A":
    print(f"The student's name starts with the letter A.")
else:
    print(f"The student's name does not start with the letter A.")

# Check whether the city ends with the letter i.
check2=city
if check2[-1]=="i":
    print(f"The city ends with the letter i.")
else:
    print(f"The city does not end with the letter i.")

# Display all details using an f-string.
print(f"Student Details: \nName: {name}\nCollege: {college}\nCity: {city}")


# Write a Python program to accept an employee's name, department, company name, and a sentence from the user.
# Perform the following operations:

name = input("Enter employee's name: ")
department = input("Enter department name: ")
company = input("Enter company name: ")
sentence = input("Enter a sentence: ")

# Display the employee's name in uppercase.
print(f"Employee's name in uppercase: {name.upper()}")

# Display the department name in lowercase.
print(f"Department name in lowercase: {department.lower()}")

# Display the company name in title case.
print(f"Company name in title case: {company.title()}")

# Display the total number of characters in the employee's name.
print(f"Total number of characters in employee's name: {len(name)}")

# Display the first and last characters of the company name.
print(f"First character of company name: {company[0]}")
print(f"Last character of company name: {company[-1]}")

# Display the employee's name in reverse order.
print(f"Employee's name in reverse order: {name[::-1]}")  

# Check whether the employee's name starts with the letter R.
if name[0] == 'R':
    print("Employee's name starts with the letter 'R' ")
else:
    print("Employee's name does not start with the letter 'R' ")

# Check whether the company name ends with the letter a.
if company[-1] == 'a':
    print("Company name ends with 'a'")
else:
    print("Company name does not end with 'a' ")

# Display all the details using an f-string.
print(f'''
    EMPLOYEE DETAILS :
    ---------------------------------------
    Name of the employee: {name}
    Department they are form: {department}
    Company they work in : {company}
    Sentence submitted: {sentence}
    ---------------------------------------
''')

# Display the original sentence.
print(f"Original sentence: {sentence}")

# Display the total number of characters in the sentence.
print(f"Total number of characters in sentence: {len(sentence)}")

# Display the first five and last five characters of the sentence.
print(f"First five characters of sentence: {sentence[:5]}")
print(f"Last five characters of sentence: {sentence[-5:]}")

# Display every alternate character of the sentence.
print(f"Every alternate character of sentence: {sentence[::2]}")

# Reverse the sentence.
print(f"Reversed sentence: {sentence[::-1]}")

# Count the number of occurrences of the letter e in the sentence.
print(f"Number of occurrences of 'e' in sentence: {sentence.count('e')}")

# Replace all spaces in the sentence with underscores (_).
print(f"Sentence with spaces replaced by underscores: {sentence.replace(' ', '_')}")

# Check whether the sentence contains the word "Python".
print(f"Sentence contains the word 'Python': {'Python' in sentence} ")

# Display the sentence in uppercase, lowercase, and title case.
print(f"Sentence in uppercase: {sentence.upper()}")
print(f"Sentence in lowercase: {sentence.lower()}")
print(f"Sentence in title case: {sentence.title()}")
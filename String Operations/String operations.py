# 2. Write a Python program to accept a string from the user and perform the following operations: 

string=input("Enter a string : ")

# Display the original string.
print(f"Original string : {string}")

# Display the total number of characters.
print(f"Total number of characters in the string: {len(string)}")

# Display the first five characters.
print(f"First five characters: {string[:5]}")

# Display the last five characters.
print(f"Last five characters: {string[-5:]}")

# Display every alternate character.
print(f"Every alternate character: {string[::2]}")
# Reverse the string.
print(f"String in reverse order: {string[::-1]}")

# Count the number of occurrences of the letter 'a'.
print(f"Number of occurrences of the letter 'a': {string.count('a')}")

# Replace all spaces with hyphens (-).
print(f"String with spaces replaced by hyphens: {string.replace(' ', '-')}")

# Check whether the string contains the word 'Python'.
if "Python" in string:
    print("The string contains the word 'Python'.")
else:
    print("The string does not contain the word 'Python'.")

# Display the string in uppercase, lowercase, and title case.
print(f"String in uppercase: {string.upper()}")
print(f"String in lowercase: {string.lower()}")
print(f"String in title case: {string.title()}")
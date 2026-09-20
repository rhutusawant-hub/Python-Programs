# Accept a student's full name and display it in uppercase, lowercase, and title case.  


name = input("Enter student's full name: ")

print(f"""
Uppercase: {name.upper()}
Lowercase: {name.lower()}
Title Case: {name.title()}
""")

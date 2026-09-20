# Accept an employee's name, department, and company name and generate a formatted employee profile.

name = input("Enter employee name: ")
department = input("Enter department: ")
company = input("Enter company name: ")

print(f"""
----- Employee Profile -----
Name: {name}
Department: {department}
Company: {company}
----------------------------
""")
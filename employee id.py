name = input("Enter your name : ")
dep = input("Enter your department : ")
comp_name = input("Enter your Company name : ")
sent = input("Enter a sentence : ")

print(f" Name in uppercase : {name.upper()}")

print(f"Department name in lowercase : {dep.lower()}")

print(f"Company name in title case : {comp_name.title()}")

print(f"Total characters in employee's name : {len(name)}")

print(f"First chracter of Company name : {comp_name[0]}")

print(f"Last character of company name : {comp_name[-1]}")

print(f"Employee name in reverse order : {reversed(name)}")
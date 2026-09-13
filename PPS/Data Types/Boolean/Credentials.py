# 20. Accept username and password and create a Boolean variable indicating whether the entered credentials match 
# predefined values.

username = input("Enter username: ")
password = input("Enter password: ")

valid = (username == "admin" and password == "2108")

print(f"Credentials Match: {valid}")
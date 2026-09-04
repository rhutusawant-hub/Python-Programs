username = input("Enter your username : ")
if username == "Admin":
    print("Welcome Admin!!")
    pass1 = input("Enter your password : ")
    if pass1 == "Admin123":
        print("Admin login successful ")
    else:
        print("Admin login failed")
elif username == "User":
    print("Welcome user")
    pass2 = input("Enter your password : ")
    if pass2 == "User123":
        print("User login successful ")
    else:
        print("User login failed")
else:
    print("chal nikal")
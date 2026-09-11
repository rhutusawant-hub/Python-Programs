# Q7. Valid Password Attempts
# Give the user a maximum of 3 attempts to enter a predefined password.
# Correct password → display "Login Successful"
# Three incorrect attempts → display "Account Locked"

password = "210608"

attempts = 1

for i in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print(f"Login Successful")
        break
    else:
        attempts = attempts + 1

if attempts > 3:
    print(f"Account Locked")
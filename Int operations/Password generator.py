import random
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*"
all_char = letters + numbers + symbols
password = int(input("What should be the length of the password : "))
for i in range(password):
    print(random.choice(all_char),end="")


# Accept a three-digit number and display its first digit, last digit, and middle digit.  

number = int(input("Enter a three-digit number: "))

first_digit = number // 100
middle_digit =  (number // 10) % 10
last_digit = number % 10

print(f"""First Digit: {first_digit}
Middle Digit: {middle_digit}
Last Digit: {last_digit}
      """)

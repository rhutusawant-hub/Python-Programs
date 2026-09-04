print(f""" 
----------CALCULATOR----------
1.Addition
2.Subtraction
3.Multiplication
4.Division
------------------------------
""")

choice = int(input("Enter your choice : "))

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))


if choice == 1:
    add = num1 + num2
    print(f"{num1} + {num2} ={add}")

elif choice == 2:
    sub = num1 - num2
    print(f"{num1} - {num2} ={sub}")

elif choice == 3:
    mul = num1 * num2
    print(f"{num1} * {num2} ={mul}")

elif choice == 4:
    if num2 == 0:
        print("Cannot divide by 0")
    else:
        div = num1 / num2
        print(f"{num1} / {num2} ={div:.2f}")

else:
    print("Invalid choice, please try again.")
 

    
    
    


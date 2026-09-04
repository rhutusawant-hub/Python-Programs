print(f""" 
----------CALCULATOR----------

MAIN MENU
------------------------------
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Floor Division
6.Modulus
7.Exponent
------------------------------
""")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

choice = int(input("Enter your choice : "))

match choice:
    case 1:
        add = num1 + num2
        print(f"{num1} + {num2} ={add}")

    case 2:
        sub = num1 - num2
        print(f"{num1} - {num2} = {sub}")

    case 3:
        mul = num1 * num2
        print(f"{num1} * {num2} ={mul}")

    case 4:
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            div = num1 / num2
            print(f"{num1} / {num2} ={div:.2f}")

    case 5:
        flr_div = num1 // num2
        print(f"{num1} // {num2} = {flr_div:2f}")

    case 6:
        mod = num1 % num2
        print(f"{num1} % {num2} = {mod}")

    case 7:
        exp = num1 ** num2
        print(f"{num1} ** {num2} = {exp}")

    case _:
        print("Invalid choice, please try again.")
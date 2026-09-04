def add(a,b):
    print(f"{a} + {b} = {a + b}")
    
def sub(a,b):
    print(f"{a} - {b} = {a - b}")
    
def mul(a,b):
    print(f"{a} * {b} = {a * b}")
    
def div(a,b):
    print(f"{a} / {b} = {a / b}")
    
def flr_div(a,b):
    print(f"{a} // {b} = {a // b}")
    
def mod(a,b):
    print(f"{a} % {b} = {a % b}")
    
def exp(a,b):
    print(f"{a} ** {b} ={a ** b}")
    
i = 1
while i < 8:
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
8.Exit
------------------------------
""")

    choice = int(input("Enter your choice : "))
    if choice in range(1,8):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

    match choice:
        case 1:
            add(num1,num2)

        case 2:
           sub(num1,num2)

        case 3:
          mul(num1,num2)

        case 4:
            if num2 == 0:
                print("Cannot divide by 0")
            else:
                div(num1,num2)
                
        case 5:
           flr_div(num1,num2)

        case 6:
            mod(num1,num2)

        case 7:
           exp(num1)

        case 8:
            break

        case _:
            print("Invalid choice, please try again.")
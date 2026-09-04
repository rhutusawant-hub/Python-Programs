
# 1. WAP to implement Basic Calculator


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
mod= num1 % num2
exp = num1 ** num2

print(f'''
    CALCULATION RESULT
      
    Addition : {add}
    Subtraction : {sub}
    Multiplication : {mul}
    Division : {round(div, 2)}
    Floor division : {floor_div}
    Modulus : {mod}
    Exponent : {exp} 
    ''')



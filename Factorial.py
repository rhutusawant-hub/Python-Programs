num = int(input("Enter a number for factorial : "))
inp = num
fact = 1
while num > 1:
    fact = fact * num
    num -=1
   
print(f"Factorial of {inp} is {fact}")
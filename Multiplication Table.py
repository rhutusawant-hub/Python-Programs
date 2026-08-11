num = int(input("Enter a number for which you want the multiplication table : "))

print(f"Multiplication table of {num} is : \n")
for i in range(11):
    print(f"{num} x {i} = {num*i}")
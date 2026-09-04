num = int(input("Enter a number for which you want the multiplication table : "))

print(f"Multiplication table of {num} is : \n")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1
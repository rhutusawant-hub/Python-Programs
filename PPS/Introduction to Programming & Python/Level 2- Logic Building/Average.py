#8. Accept marks of three subjects and display total and average.

mark1 = int(input("Enter marks of Physics : "))
mark2 = int(input("Enter marks of Chemistry : "))
mark3 = int(input("Enter marks of Maths : "))

avg = (mark1 + mark2 + mark3) / 3
print(f"Average of three subjects is {avg}")
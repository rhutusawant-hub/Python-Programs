#Choice of calculation
print("1.Area of Rectangle")
print("2.Area of Square")
print("3.Area of Triangle")
choice = int(input("Enter your choice (1/2/3) : "))

#Area of rectangle
if choice == 1:
    L = float(input("Enter length of rectangle :"))
    W = float(input("Enter width of rectangle :"))
    A1 = L * W
    print(f"The area of rectangle is {A1:.2f}")


#Area of Square
elif choice == 2:
    S = float(input("Enter length of side of Square :"))
    A2 = S * S
    print(f"The area of square is {A2:.2f}")


#Area of Traingle
elif choice == 3:
    H = float(input("Enter the height of triangle : "))
    B = float(input("Enter the length of base of triangle : "))
    A3 = (H * B)/2
    print(f"The area of triangle is {A3:.2f}")

else:
    print("Invalid choice, please try again.")







# Accept the real and imaginary parts from the user and create a complex number.

real = float(input("Enter real part: "))
imaginary = float(input("Enter imaginary part: "))

complex_number = complex(real, imaginary)

print(f"Complex Number: {complex_number}")
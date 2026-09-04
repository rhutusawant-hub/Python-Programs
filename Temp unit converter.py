#Choice of conversion
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2) : "))


#celsius to fahrenheit
if choice == 1:
    C = float(input("Enter temperature in celsius : "))
    F = (C * 9/5) + 32
    print("The temperature in Fahrenheit is : ", F)


#Fahrenheit to celsius
elif choice == 2:
    FA = float(input("Enter temperature in Fahrenheit : "))
    CE = (FA - 32) * 5/9
    print("The temperature in Celsius is : ", CE)

else:
    print("Invalid choice. Please select either 1 or 2.")






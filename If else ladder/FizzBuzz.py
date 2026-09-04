num = int(input("Enter a number : "))
if (num % 3 == 0) and (num % 5 == 0):
    print("Fizz buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by both")
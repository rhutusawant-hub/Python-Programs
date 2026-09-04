time = int(input("Enter time(24hr Format) : "))
name = input("Enter your name : ")
def greet(name):
    print(f"Hi! {name}")
    if time >= 0 and time <=6:
        print("Soja Sale")
    elif time >= 6 and time <=12:
        print("Good Morning")
    elif time >= 12 and time <=17:
        print("Good afternoon")
    elif time >= 17 and time <=20:
        print("Good evening")
    elif time >= 20 and time <=24:
        print("Good night")
    else:
        print("INVALID INPUT!")
greet(name)

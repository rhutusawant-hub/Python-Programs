marks = int(input("Enter your marks :"))
if marks > 100 or marks < 0:
    print("Tere teacher ki shadi hai cya?")
elif marks >= 35:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")
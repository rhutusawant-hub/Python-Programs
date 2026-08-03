
print("----------GRADE CALCULATOR----------")
marks = float(input("Enter your percentage : " ))

if marks < 0 or marks > 100:
       print("Invalid marks! Please enter again")

else:
    
    if marks >= 90 and marks <= 100:
        print(f"Grade : A+ \nOutstanding!!")
    
    elif marks >= 80 and marks <=89:
        print(f"Grade : A \nExcellent!")
    
    elif marks >= 70 and marks <=79:
        print(f"Grade : B \nGood Job!")

    elif marks >=60 and marks <=69:
        print(f"Grade : C \nKeep Improving!")
    
    elif marks >=40 and marks <=59:
        print(f"Grade : D \nYou passed :)")

    else:
        print(f"Grade : F \nBetter luck next time!")



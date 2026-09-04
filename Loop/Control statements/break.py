n = int(input("Enter no of marks : "))
marks = []
for i in range(n):
    mark = int(input("Enter mark : "))
    if mark > 100 or mark < 0:
        print("Invalid marks entered!")
        break
    marks.append(mark)
else:
    print(f"Marks of {n} subjects are {marks}") 
        
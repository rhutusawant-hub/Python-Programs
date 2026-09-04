n = int(input("Enter no of marks : "))
marks = []
for i in range(n):
    mark = int(input("Enter mark : "))
    marks.append(mark)

result = 0
for i in marks:
    result = result + i
print(f"Sum of {marks} is {result}")
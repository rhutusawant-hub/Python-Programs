# Create a Student Report Generator that accepts the student's name and marks of five subjects and displays a formatted
# report containing all marks, total, average, and percentage.

marks = []
name = input("Enter your name : ")

for i in range(5):
    mark = int(input(f"Enter marks of subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
percentage = (total / 500) * 100

print(f"""
      ----------Student Report----------
      Name - {name}
      ----------------------------------
      Report :
      Marks of all subjects are : {marks}
      Total marks : {total}
      Average marks : {average}
      Percentage Obtained : {percentage:.2f}
      ----------------------------------
      """)
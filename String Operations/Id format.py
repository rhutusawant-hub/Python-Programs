# 2. Develop a program that accepts the following details of a student:
#
# Name
# Roll Number
# Branch
# Semester
# Division
# Contact Number
# Blood Group
#
# Display the information in a properly formatted report.
# Display the output in a formatted ID  manner.

name = input("Enter your name : ")
roll_num = int(input("Enter your Roll number : "))
branch = input("Enter your branch : ")
blood_group = input("Enter your Blood Group : ")
sem = int(input("Enter your semester number : "))
div = input("Enter your Divsion : ")
cont_no = int(input("Enter your Contact number : "))

print(f'''

    STUDENT REPORT  
      NAME : {name}
      Roll Number : {roll_num}
      Branch : {branch}
      Semester : {sem}
      Division : {div}
      Blood Group : {blood_group}
      Contact Number : {cont_no}
    
    ID for {name}
    -------------------------------------------------------
    Name : {name}
      
    Roll Number : {roll_num}       Blood Group : {blood_group}

    Branch : {branch}           Semester : {sem}           Division : {div}

    Contact Number : {cont_no}

    --------------------------------------------------------  
    ''')
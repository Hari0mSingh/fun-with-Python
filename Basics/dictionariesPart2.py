#wap to the student name and grade in dict.
studentDetails = {}

off = False
while not off:
    name = input("Enter your name: ")
    grade = input("Enter your grade: ")
    studentDetails[name] = grade
    print("student details added successfully.")
    add_another = input("Would you like to add another user? Y/N").lower()
    if(add_another=='y'):
        pass
    else:
        off = True
    

print(studentDetails)
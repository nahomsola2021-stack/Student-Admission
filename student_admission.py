grade = input("What is your Grade?: ")
attendance = input("What is your attendance percentage?: ")
grade = int(grade)
attendance = int(attendance)

if grade >= 70 and attendance >= 80:
    print("Admitted")
    other = input("Do you want to continue with other student?(type y if you want and n if you dont)")
else:
    print("Not Admitted")
    other = input("Do you want to continue with other student?(type y if you want and n if you dont)")
while other == "y":
    grade = input("What is your Grade?: ")
    attendance = input("What is your attendance percentage?: ")
    other = input("Do you want to continue with other student?(type y if you want and n if you dont)")
while other == "n": 
    other = input(" Thank you for visiting!")

     

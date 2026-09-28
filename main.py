from student import add_students, search_student, view_student
from attendance import add_attendance
from marks import add_marks
from marks import add_marks,calculate_grade
from reports import genrate_report

while True:
    print("\n=====STUDENT ATTENDANCE AND GRADE MANAGER=====")
    print("1.Add student")
    print("2.View all student")
    print("3.Search all student")
    print("4.Add attendance")
    print("5.Add marks")
    print("6.Calculate grade")
    print("7.Genrate Report")
    print("8.EXIT")
    
    choice=input("Enter your choice:")
    if choice=="1":
        add_students()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        add_attendance()
    elif choice=="5":
        add_marks()
    elif choice=="6":
        calculate_grade()
    elif choice=="7":
        genrate_report()
    
    
    elif choice=="8":
        print("Thank you for using student attendance and grade manager")
        break

    else:
        print("Invalid choice.please try again")            


        




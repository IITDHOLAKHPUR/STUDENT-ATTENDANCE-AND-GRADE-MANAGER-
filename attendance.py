from data import students
from validation import valid_attendance


def add_attendance():
    if len(students)==0:
        print("No student available")
        return
    roll_no=input("Enter student roll number:")

    for student in students:
        if student["roll_no"]==roll_no:

            total_classes=int(input("Enter total classes:"))
            attended_classes=int(input("Enter the attended classes:"))
            if not valid_attendance(attended_classes,total_classes):
                print("invalid attendance details")
                return

            percentage=(attended_classes/total_classes)*100
            student["total_classes"]=total_classes
            student["attended_classes"]=attended_classes
            student["attendance_percentage"]=percentage
            print("Attendance added successfully")
            print("Attendance:",percentage,"%")
            return
        print("Student not found.")
        

            
        

                              
 
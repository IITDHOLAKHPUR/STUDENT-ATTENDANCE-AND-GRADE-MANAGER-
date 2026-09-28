from data import students
def genrate_report():
    if len(students)==0:
        print("no student available maybe he is toilet")
        return
    roll_no=input("Enter the student roll number:")
    for student in students:
        if student["roll_no"]==roll_no:

            print("\n=========STUDENT REPORT==========")
            print("Name:",student["name"])
            print("Roll No:",student["roll_no"])
            if "attendance_percentage"in student:
                print("Attendance",student["attendance_percentage"],"%")
            if student["attendance_percentage"]>=75:
                     print("Attendance status:Eligible")
            else:
                 print("Attendance status: Debared")
        
            if "marks" in student:
                    print("Marks:",student["marks"])
            else:
                    print("marks not entered")
            if "grade" in student:
                 
                 print("Grade:",student["grade"])
                 
            else:
                
                print("grade not genrated or entered")

            print("=============================================")
                
            return
            print("student not found")
                
    
                            
    

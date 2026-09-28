from data import students
from validation import valid_marks

def add_marks():
    if len(students)==0:
        print("No students available")
        return
    roll_no=input("Enter the student roll number:")
    for student in students:
        if student["roll_no"]==roll_no:
            marks=float(input("Enter the marks:"))
            if not valid_marks(marks):
                 print("Marks must be between 0 and 100.")
                 return
            
            student["marks"]=marks
            print("Marks added successfully")
            return
        print("Student not found.")
def calculate_grade():
            if len(students)==0:
                print("No students available")
                return
            roll_no=input("Enter the student roll number:")
            for student in students:
                if student["roll_no"]==roll_no:
                    if "marks" not in student:
                        print("marks have not been entered yet")
                        return
                    marks=student["marks"]
                    if marks>=90:
                        grade="A+"
                    elif marks>=80:
                        grade="A"
                    elif marks>=70:
                        grade="B"
                    elif marks>=60:
                        grade="C"
                    elif marks>=50:
                        grade="D" 
                    else:
                        grade="F"
                    student["grade"]=grade
                    print("Grade:",grade)
                    return
                print("Student not found.")

                                   

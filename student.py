from data import students


def add_students():
    while True:
         name=input("Enter student name:")
         roll_no=input("Enter roll number:")
         student={"name":name,
             "roll_no":roll_no}
         students.append(student)
         print("Student added successfully")
         choice=input("DO you want to add more students?(y/n):")
         if choice.lower()!="y":
              break
def view_student():
        
        if len(students)==0:
            print("no students available")
        else:
            print("\nStudents List")

            for student in students:
                print("Roll NO:",student["roll_no"])
                print("Name:",student["name"])
                print("----------------------")
def search_student():
     roll_no=input("Enter roll number to search:")

     found=False

     for student in students:
          if student["roll_no"]==roll_no:
               print("/student Found")
               print("Roll NO",student["roll_no"])
               print("Name",student["name"])
               found=True
               break

     if not found:
          print("Student not found")     

from dao.tasks import *


print(" WELCOME TO SIS ")
while(True):
    print("\n select 1 to perform task 8 - ADDING A STUDENT JOHN AND ENROLLING HIM IN TWO COURSES")
    print(" 2 to perform task 9 - ADDING A NEW TEACHER AND ASSIGNING HIM/HER TO A COURSE")
    print(" 3 to perform task 10 - RECORDS THE PAYMENT IN THE DATABASE")
    print(" 4 to perform task 11 - ENROLLMENT REPORT GENERATION")
    print(" 5 to get all the teacher data")
    print(" 6 to get all the student data")
    print(" 7 to get all the payments data")
    print(" 8 to get all the courses data")
    print(" 9 to get all the enrollments data")
    print(" 10 to exit")
    s = input("Enter your choice : ")
    if s == '1':
        try:
            studentEnrollment()
        except Exception as e:
            print()
    elif s == '2':
        try:
            teacherAssignment()
        except Exception as e:
            print()
    elif s == '3':
        try:
            paymentRecord()
        except Exception as e:
            print()
    elif s == '4':
        try:
            enrollmentReportGeneration()
        except Exception as e:
            print()
    elif s == '5':
        teacherInfo()
    elif s == '6':
        studentInfo()
    elif s == '7':
        paymentInfo()
    elif s == '8':
        courseInfo()
    elif s == '9':
        enrollmentInfo()
    elif s == '10':
        print("*"*30 + " THANK YOU FOR USING STUDENT INFORMATION SYSTEM " + "*"*30)
        break
    else:
        print("Invalid choice")

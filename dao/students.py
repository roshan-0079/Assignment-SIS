from util.dbConnection import dbConnection
from datetime import datetime
from exception.exception import *


# STUDENTS CLASS
class Students(dbConnection):
    # CONSTRUCTOR
    def __init__(self):
        self.studentID = int()
        self.firstName = str()
        self.lastName = str()
        self.dateOfBirth = datetime.date
        self.email = str()
        self.phoneNumber = str()

    # CRUD METHODS
    # SELECT FUNCTION TO GET ALL THE DATA
    def select(self) -> list:
        self.open()
        select_str = '''select * from Students'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        return data

    # CREATE FUNCTION TO CREATE THE TABLE
    def create(self):
        self.open()
        create_str = '''CREATE TABLE if not exists Students (studentID INT PRIMARY KEY,
        firstName VARCHAR(50),
        lastName VARCHAR(50),
        dateOfBirth DATE,
        email VARCHAR(50),
        phoneNumber CHAR(10));'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(create_str)
        self.close()

    # INSERT FUNCTION TO INSERT THE DATA
    def insert(self, studentID, firstName, lastName, dateOfBirth, email, phoneNumber):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNumber = phoneNumber
        self.open()
        insert_str = f'''INSERT INTO Students VALUES
        ({studentID}, '{firstName}', '{lastName}', '{dateOfBirth}', '{email}', '{phoneNumber}')'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(insert_str)
            self.conn.commit()
        except Exception as e:
            print("---DATA ALREADY EXISTS---")
        self.close()

    # UPDATE FUNCTION TO UPDATE THE DATA
    def update(self, studentID, firstName, lastName, dateOfBirth, email, phoneNumber):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.email = email
        self.phoneNumber = phoneNumber
        self.open()
        data = [(firstName, lastName, dateOfBirth, email, phoneNumber, studentID)]
        update_str = '''UPDATE students 
        set firstName = %s, lastName = %s, dateOfBirth = %s, email = %s, phoneNumber = %s
        where studentID = %s'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(update_str, data)
            self.conn.commit()
            print("Updated Successfully")
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # DELETE FUNCTION TO DELETE THE RECORDS
    def delete(self, studentID):
        self.studentID = studentID
        delete_str = f'''delete from students where studentID = {studentID}'''
        self.open()
        self.stmt = self.conn().cursor()
        self.stmt.execute(delete_str)
        self.conn.commit()
        self.close()

    # FUNCTION TO ENROLL STUDENT IN A COURSE
    def EnrollInCourse(self, courseID: int):
        self.courseID = courseID
        self.studentID = 7
        self.open()
        self.stmt = self.conn.cursor()
        select_str = f'select * from enrollments where studentID = {self.studentID} and courseID = {courseID}'
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        if len(data) == 1:
            try:
                raise DuplicateEnrollmentException
            except DuplicateEnrollmentException as e:
                print(e)
        else:
            try:
                id = int(input("Enter a UNIQUE 4 digit enrollment ID : "))
                enroll_course = f'insert into enrollments values({id}, {self.studentID}, {courseID}, CURDATE())'
                self.stmt.execute(enroll_course)
            except Exception as e:
                print('---ENROLLMENT ID EXISTS/ ALREADY ENROLLED---')
            self.conn.commit()
            print("Enrolled successfully")
        self.close()

    # FUNCTION TO UPDATE THE STUDENT DETAILS
    def UpdateStudentInfo(self, firstName: str, lastName: str, dateOfBirth: datetime, email: str, phoneNumber: str):
        ID = int(input("Enter student ID : "))
        self.update(studentID= ID,firstName=firstName,lastName=lastName,dateOfBirth=dateOfBirth,
                    email=email, phoneNumber=phoneNumber)

    # FUNCTION TO MAKE PAYMENT
    def MakePayment(self, amount: int, paymentDate: datetime):
        ID = int(input("Enter student ID : "))
        self.open()
        self.stmt = self.conn.cursor()
        while(True):
            try:
                pID = int(input("Enter a Unique 5 digit payment ID"))
                payment_str = f'insert into payments values({pID}, {ID}, {amount},' \
                              f'{paymentDate.year}{paymentDate.month}{paymentDate.day})'
                self.stmt.execute(payment_str)
                self.conn.commit()
                print("Inserted Successfully")
            except Exception as e:
                print(str(e)+'---PAYMENT ID EXISTS---')
            else:
                break
        self.close()

    # FUNCTION TO DISPLAY STUDENT DETAILS
    def DisplayStudentInfo(self):
        data = self.select()
        try:
            ID = int(input("Enter Student ID : "))
            for i in data:
                if i[0] == ID:
                    print(i)
                    break
            else:
                raise StudentNotFoundException
        except StudentNotFoundException as e:
            print(e)

    # FUNCTION TO FETCH ENROLLED COURSES OF A STUDENT
    def GetEnrolledCourses(self):
        self.open()
        self.stmt = self.conn.cursor()
        ID = int(input("Enter Student ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise StudentNotFoundException
        except StudentNotFoundException as e:
            print(e)
        else:
            getCourses = f'''SELECT courseName FROM Students AS S
                                INNER JOIN Enrollments AS E ON S.studentID=E.studentID
                                INNER JOIN Courses as C ON C.CourseID=E.CourseID
                                WHERE S.studentID = {ID}
                                GROUP BY S.studentID'''
            self.stmt.execute(getCourses)
            data = self.stmt.fetchall()
            print(data)
        finally:
            self.close()

    # FUNCTION TO FETCH PAYMENT HISTORY OF A STUDENT
    def GetPaymentHistory(self, ID):
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise StudentNotFoundException
        except StudentNotFoundException as e:
            print(e)
        else:
            self.open()
            self.stmt = self.conn.cursor()
            paymentHistory = f'''SELECT PAYMENTID, AMOUNT, PAYMENTDATE FROM PAYMENTS
                                WHERE STUDENTID = {ID}'''
            self.stmt.execute(paymentHistory)
            data = self.stmt.fetchall()
            self.close()
            print('PAYMENT_ID, AMOUNT, DATE')
            for i in data:
                print(i)

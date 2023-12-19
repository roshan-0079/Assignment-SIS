from util.dbConnection import dbConnection
from exception.exception import *
from datetime import datetime


# ENROLLMENT CLASS
class Enrollments(dbConnection):
    # CONSTRUCTOR
    def __init__(self):
        self.enrollmentID = int()
        self.studentID = int()
        self.courseID = int()
        self.enrollmentDate = datetime.date

    # CRUD METHODS
    # SELECT METHOD TO GET THE DATA
    def select(self):
        self.open()
        select_str = '''select * from Enrollments'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        return data

    # CREATE METHOD TO CREATE THE TABLE
    def create(self):
        self.open()
        create_str = '''CREATE TABLE if not exists Enrollments (
                        enrollmentID INT PRIMARY KEY,
                        studentID INT, FOREIGN KEY (studentID) REFERENCES Students(studentID) on delete cascade,
                        courseID INT, FOREIGN KEY (courseID) REFERENCES Courses(courseID) on delete cascade,
                        enrollment_date DATE);'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(create_str)
        self.close()

    # INSERT FUNCTION TO INSERT THE DATA
    def insert(self, enrollmentID, studentID, courseID, enrollmentDate):
        self.enrollmentID = enrollmentID
        self.studentID = studentID
        self.courseID = courseID
        self.enrollmentDate = enrollmentDate
        self.open()
        insert_str = f'''INSERT INTO Enrollments VALUES
        ({enrollmentID}, {studentID}, {courseID}, '{enrollmentDate}')'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(insert_str)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # UPDATE FUNCTION TO UPDATE THE DATA
    def update(self, enrollmentID, studentID, courseID, enrollmentDate):
        self.enrollmentID = enrollmentID
        self.studentID = studentID
        self.courseID = courseID
        self.enrollmentDate = enrollmentDate
        self.open()
        data = [(studentID, courseID, enrollmentDate, enrollmentID)]
        update_str = '''UPDATE enrollments 
        set studentID = %s, courseID = %s, enrollmentDate = %s
        where enrollmentID = %s'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(update_str, data)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # DELETE FUNCTION TO DELETE A RECORD
    def delete(self, enrollmentID):
        self.enrollmentID = enrollmentID
        delete_str = f'''delete from enrollments where enrollmentID = {enrollmentID}'''
        self.open()
        self.stmt = self.conn().cursor()
        self.stmt.execute(delete_str)
        self.conn.commit()
        self.close()

    # FUNCTION TO GET STUDENT DETAILS
    def GetStudent(self):
        ID = int(input("Enter Enrollment ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise InvalidEnrollmentDataException
        except InvalidEnrollmentDataException as e:
            print(e)
        else:
            query = f'''SELECT S.FIRSTNAME, S.LASTNAME FROM STUDENTS AS S
            INNER JOIN ENROLLMENTS AS E ON S.STUDENTID = E.STUDENTID
            WHERE E.ENROLLMENTID = {ID}'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            print(data)

    # FUNCTION TO GET COURSE DETAILS
    def GetCourse(self):
        ID = int(input("Enter Enrollment ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise InvalidEnrollmentDataException
        except InvalidEnrollmentDataException as e:
            print(e)
        else:
            query = f'''SELECT C.COURSENAME FROM COURSES AS C
                    INNER JOIN ENROLLMENTS AS E ON C.COURSEID = E.COURSEID
                    WHERE E.ENROLLMENTID = {ID}'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            print(data)

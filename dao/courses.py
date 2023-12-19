from util.dbConnection import dbConnection
from exception.exception import *
from dao.teachers import Teachers


# COURSES CLASS
class Courses(dbConnection):
    # CONSTRUCTOR
    def __init__(self):
        self.courseID = int()
        self.courseName = str()
        self.credits = int()
        self.teacherID = int()

    # CRUD METHODS
    # METHOD TO PERFORM SELECT OPERATION
    def select(self):
        self.open()
        select_str = '''select * from Courses'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        return data

    # THIS METHOD WILL CREATE THE TABLE
    def create(self):
        self.open()
        create_str = '''CREATE TABLE if not exists Courses (
                        courseID INT PRIMARY KEY,
                        courseName VARCHAR(50),
                        credits INT,
                        teacherID INT,
                        FOREIGN KEY (teacherID) REFERENCES Teachers(teacherID) on delete cascade)'''
        self.stmt.execute(create_str)
        self.close()

    # THIS METHOD WILL INSERT DATA INTO THE TABLE
    def insert(self, courseID, courseName, credits, teacherID):
        self.courseID = courseID
        self.courseName = courseName
        self.courseCode = credits
        self.teacherID = teacherID
        self.open()
        insert_str = f'''INSERT INTO Courses VALUES
           ({courseID}, '{courseName}', '{credits}', '{teacherID}')'''
        try:
            self.stmt.execute(insert_str)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # THIS METHOD WILL UPDATE THE DATA
    def update(self, courseID, courseName, credits, teacherID):
        self.courseID = courseID
        self.courseName = courseName
        self.credits = credits
        self.teacherID = teacherID
        self.open()
        data = [(courseName, credits, teacherID, courseID)]
        update_str = '''UPDATE courses 
           set courseName = %s, credits = %s, teacherID = %s
           where courseID = %s'''
        try:
            self.stmt.executemany(update_str, data)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # THIS METHOD WILL DELETE THE RECORD
    def delete(self, courseID):
        self.courseID = courseID
        delete_str = f'''delete from courses where courseID = {courseID}'''
        self.open()
        self.stmt.execute(delete_str)
        self.conn.commit()
        self.close()

    # THIS METHOD WILL ASSIGN TEACHER TO A COURSE
    def AssignTeacher(self, teacher: Teachers, teacherID, courseID):
        try:
            data = teacher.select()
            for i in data:
                if i[0] == teacherID:
                    break
            else:
                raise InvalidTeacherDataException
        except InvalidTeacherDataException as e:
            print(e)
        else:
            try:
                data = self.select()
                for i in data:
                    if i[0] == courseID:
                        break
                else:
                    raise InvalidCourseDataException
            except InvalidCourseDataException as e:
                print(e)
            else:
                data = self.select()
                for i in data:
                    if i[0] == courseID and i[3] == teacherID:
                        print("TEACHER ALREADY ASSIGNED")
                        break
                else:
                    query = f'''UPDATE COURSES SET TEACHERID = {teacherID} WHERE COURSEID = {courseID}'''
                    self.open()
                    self.stmt = self.conn.cursor()
                    self.stmt.execute(query)
                    self.conn.commit()
                    self.close()
                    print("TEACHER ASSIGNED")

    # THIS METHOD WILL UPDATE THE COURSE INFORMATION
    def UpdateCourseInfo(self, courseID: int, courseName: str, teacherID: int, teacher:Teachers):
        try:
            data = teacher.select()
            for i in data:
                if i[0] == teacherID:
                    break
            else:
                raise InvalidTeacherDataException
        except InvalidTeacherDataException as e:
            print(e)
        else:
            try:
                data = self.select()
                for i in data:
                    if i[0] == courseID:
                        break
                else:
                    raise InvalidCourseDataException
            except InvalidCourseDataException as e:
                print(e)
            else:
                query = f'''UPDATE COURSES SET COURSENAME = %s, TEACHERID = %s WHERE COURSEID = %s'''
                data = [(courseName,teacherID,courseID)]
                self.open()
                self.stmt = self.conn.cursor()
                self.stmt.executemany(query, data)
                self.conn.commit()
                self.close()
                print("UPDATED SUCCESSFULLY")

    # THIS METHOD WILL DISPLAY PARTICULAR COURSE INFORMATION
    def DisplayCourseInfo(self):
        ID = int(input("Enter Course ID : "))
        data = self.select()
        try:
            for i in data:
                if i[0] == ID:
                    print(i)
                    break
            else:
                raise CourseNotFoundException
        except CourseNotFoundException as e:
            print(e)

    # THIS METHOD WILL GET ALL THE ENROLLMENTS
    def GetEnrollments(self):
        ID = int(input("Enter Course ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise CourseNotFoundException
        except CourseNotFoundException as e:
            print(e)
        else:
            query = f'''SELECT  C.coursename, S.studentid, S.firstname, S.lastname, E.ENROLLMENT_DATE
                        FROM Students AS S
                        INNER JOIN Enrollments AS E ON E.studentid = S.studentid
                        INNER JOIN Courses AS C ON C.courseid = E.courseid
                        WHERE C.COURSEID = {ID}
                        GROUP BY  C.coursename, S.studentid, S.firstname, S.lastname;'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            return data

    # THIS METHOD WILL GET DETAILS OF A PARTICULAR TEACHER
    def GetTeacher(self):
        ID = int(input("Enter Course ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise CourseNotFoundException
        except CourseNotFoundException as e:
            print(e)
        else:
            query = f'''SELECT C.COURSENAME, T.FIRSTNAME, T.LASTNAME FROM COURSES AS C 
            INNER JOIN TEACHERS AS T ON C.TEACHERID = T.TEACHERID
            WHERE COURSEID = {ID} GROUP BY C.COURSENAME'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            for i in data:
                print(i)

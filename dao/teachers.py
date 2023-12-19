from util.dbConnection import dbConnection
from exception.exception import *


# TEACHERS CLASS
class Teachers(dbConnection):
    def __init__(self):
        self.teacherID = int()
        self.firstName = str()
        self.lastName = str()
        self.email = str()

    # CRUD METHODS
    # SELECT FUNCTION TO GET THE DATA
    def select(self):
        self.open()
        select_str = '''select * from Teachers'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        return data

    # CREATE FUNCTION TO CREATE THE TABLE
    def create(self):
        self.open()
        create_str = '''CREATE TABLE if not exists Teachers (
                        teacherID INT PRIMARY KEY,
                        firstName VARCHAR(50),
                        lastName VARCHAR(50),
                        email VARCHAR(50));'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(create_str)
        self.close()

    # INSERT FUNCTION TO INSERT THE DATA
    def insert(self, teacherID, firstName, lastName, email):
        self.teacherID = teacherID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.open()
        insert_str = f'''INSERT INTO Teachers VALUES
        ({teacherID}, '{firstName}', '{lastName}', '{email}')'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(insert_str)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA OR DATA EXISTS---")
        self.close()

    # UPDATE FUNCTION TO UPDATE THE DATA
    def update(self, teacherID, firstName, lastName, email):
        self.teacherID = teacherID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.open()
        data = [(firstName, lastName, email, teacherID)]
        update_str = '''UPDATE Teachers 
        set firstName = %s, lastName = %s, email = %s
        where teacherID = %s'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(update_str, data)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # DELETE FUNCTION TO DELETE A RECORD
    def delete(self, teacherID):
        self.teacherID = teacherID
        delete_str = f'''delete from teachers where teacherID = {teacherID}'''
        self.open()
        self.stmt = self.conn().cursor()
        self.stmt.execute(delete_str)
        self.conn.commit()
        self.close()

    # FUNCTION TO UPDATE TEACHER DETAILS
    def UpdateTeacherInfo(self, firstName : str, lastName : str, email : str):
        ID = int(input("Enter teacher ID : "))
        self.update(ID, firstName, lastName, email)
        print('UPDATED SUCCESSFULLY')

    # FUNCTION TO DISPLAY TEACHER DETAILS
    def DisplayTeacherInfo(self):
        ID = int(input("Enter Teacher ID : "))
        data = self.select()
        try:
            for i in data:
                if i[0] == ID:
                    print(i)
                    break
            else:
                raise TeacherNotFoundException
        except TeacherNotFoundException as e:
            print(e)

    # FUNCTION TO GET ASSIGNED COURSES OF A TEACHER
    def GetAssignedCourses(self):
        ID = int(input("Enter Teacher ID : "))
        data = self.select()
        try:
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise TeacherNotFoundException
        except TeacherNotFoundException as e:
            print(e)
        else:
            query = f'''SELECT t.teacherid,t.firstname,t.lastname,c.coursename FROM Courses AS C
                        INNER JOIN Teachers AS T ON C.teacherid=T.teacherid
                        where t.teacherid = {ID}
                        GROUP BY t.teacherid,t.firstname,t.lastname,c.coursename'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            for i in data:
                print(i)
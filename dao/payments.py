import datetime

from util.dbConnection import dbConnection


# PAYMENTS CLASS
class Payments(dbConnection):
    # CONSTRUCTOR
    def __init__(self):
        self.paymentID = int()
        self.studentID = int()
        self.amount = int()
        self.paymentDate = datetime.date

    # CRUD METHODS
    # SELECT METHOD TO GET ALL THE DATA
    def select(self):
        self.open()
        select_str = '''select * from Payments'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(select_str)
        data = self.stmt.fetchall()
        return data

    # CREATE METHOD TO CREATE THE TABLE
    def create(self):
        self.open()
        create_str = '''CREATE TABLE if not exists Payments (
                        paymentID INT PRIMARY KEY,
                        studentID INT, FOREIGN KEY (studentID) REFERENCES Students(studentID) on delete cascade,
                        amount INT,
                        paymentDate DATE);'''
        self.stmt = self.conn.cursor()
        self.stmt.execute(create_str)
        self.close()

    # INSERT METHOD TO INSERT THE DATA
    def insert(self, paymentID, studentID, amount, paymentDate):
        self.paymentID = paymentID
        self.studentID = studentID
        self.amount = amount
        self.paymentDate = paymentDate
        self.open()
        insert_str = f'''INSERT INTO Payments VALUES
        ({paymentID}, {studentID}, {amount}, '{paymentDate}')'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.execute(insert_str)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # UPDATE METHOD TO UPDATE THE RECORDS
    def update(self, paymentID, studentID, amount, paymentDate):
        self.paymentID = paymentID
        self.studentID = studentID
        self.amount = amount
        self.paymentDate = paymentDate
        self.open()
        data = [(studentID, amount, paymentDate, paymentID)]
        update_str = '''UPDATE payments 
        set studentID = %s, amount = %s, paymentDate = %s
        where paymentID = %s'''
        self.stmt = self.conn.cursor()
        try:
            self.stmt.executemany(update_str, data)
            self.conn.commit()
        except Exception as e:
            print(str(e) + "---INCORRECT TYPE OF DATA---")
        self.close()

    # DELETE METHOD TO DELETE THE RECORDS
    def delete(self, paymentID):
        self.paymentID = paymentID
        delete_str = f'''delete from payments where paymentID = {paymentID}'''
        self.open()
        self.stmt = self.conn().cursor()
        self.stmt.execute(delete_str)
        self.conn.commit()
        self.close()

    # FUNCTION TO GET STUDENT DETAILS
    def GetStudent(self, ID):
        try:
            data = self.select()
            for i in data:
                if i[1] == ID:
                    break
            else:
                raise Exception
        except Exception as e:
            print("INVALID DATA")
        else:
            query = f'''SELECT S.FIRSTNAME, S.LASTNAME, P.PAYMENTID, P.PAYMENTDATE
                    FROM STUDENTS AS S 
                    INNER JOIN PAYMENTS AS P ON S.STUDENTID = P.STUDENTID
                    WHERE S.STUDENTID = {ID};'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            print(data)

    # FUNCTION TO GET PAYMENT AMOUNT
    def GetPaymentAmount(self):
        ID = int(input("Enter Payment ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise Exception
        except Exception as e:
            print("INVALID PAYMENT ID")
        else:
            query = f'''SELECT AMOUNT FROM PAYMENTS
                    WHERE PAYMENTID = {ID}'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            print(data)

    # FUNCTION TO GET PAYMENT DATE
    def GetPaymentDate(self):
        ID = int(input("Enter Payment ID : "))
        try:
            data = self.select()
            for i in data:
                if i[0] == ID:
                    break
            else:
                raise Exception
        except Exception as e:
            print("INVALID PAYMENT ID")
        else:
            query = f'''SELECT paymentDate FROM PAYMENTS
                            WHERE PAYMENTID = {ID}'''
            self.open()
            self.stmt = self.conn.cursor()
            self.stmt.execute(query)
            data = self.stmt.fetchall()
            self.close()
            print(data)

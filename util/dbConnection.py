import mysql.connector as sql


class dbConnection:
    # THIS FUNCTION WILL GET THE CONNECTION
    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='sisdb', user='root', password='Shaik@123')
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(str(e) + '-----DATABASE NOT FOUND-----')

    # THIS FUNCTION  WILL CLOSE THE CONNECTION
    def close(self):
        try:
            self.conn.close()
        except Exception:
            pass
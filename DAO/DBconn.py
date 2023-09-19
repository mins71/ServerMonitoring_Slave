import pymysql as db
from DAO.DBInfo import dbInfo

class DBConn:
    def getConn(self):
        try:
            self.connection = db.connect(
                host=dbInfo[0],
                user=dbInfo[1],
                port=dbInfo[2],
                password=dbInfo[3],
                database=dbInfo[4]
            )

        except:
            raise Exception("DB Connection Error.")

    def closeConn(self):
            self.connection.close()
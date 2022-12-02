import os
import psycopg2
from dotenv import load_dotenv

from StudentD import StudentD
from listD import ListD

load_dotenv()


class Database:
    cursor = None
    conn = None

    # def connect(self):
    #     try:

    #     except Exception as e:
    #         print(e)
    def __init__(self):
        self.conn = psycopg2.connect(
            host=str("{}".format(os.getenv('DBHOST'))),
            dbname=str("{}".format(os.getenv('DBNAME'))),
            user=str("{}".format(os.getenv('DBUSER'))),
            password=str("{}".format(os.getenv('DBPASSWORD'))),
            port=os.getenv('DBPORT'))
        self.cursor = self.conn.cursor()
        self.student = StudentD(self.conn, self.cursor)
        self.list = ListD(self.conn, self.cursor)
        self.student.createTable()
        self.list.createTable()

    def close(self):
        self.conn.close()
        self.cursor.close()

# database = Database()
# database.close()

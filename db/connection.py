import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


class Database:
    cursor = None
    conn = None

    def connect(self):
        try:
            conn = psycopg2.connect(
                host=str("{}".format(os.getenv('DBHOST'))),
                dbname=str("{}".format(os.getenv('DBNAME'))),
                user=str("{}".format(os.getenv('DBUSER'))),
                password=str("{}".format(os.getenv('DBPASSWORD'))),
                port=os.getenv('DBPORT'))
            self.cursor = conn.cursor()
        except Exception as e:
            print(e)


database = Database()
database.connect()
# database.close()

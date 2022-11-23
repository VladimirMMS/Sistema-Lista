from models.studentM import Student


class ListD:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def createTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS list (
                id TEXT Primary Key,
                attendance boolean,
                student_id INTEGER,
                date DATE NOT NULL default now()
            )
        ''')
        self.conn.commit()

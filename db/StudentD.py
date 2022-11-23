from models.studentM import Student


class StudentD:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def createTable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id TEXT Primary Key,
                matricula TEXT,
                name TEXT,
                last_name TEXT,
                age INTEGER,
                grade INTEGER,
                mail TEXT,
                date DATE NOT NULL default now()
            )
        ''')
        self.conn.commit()

    def getStudent(self):
        self.cursor.execute('SELECT * FROM student')
        studets = []
        for id, name, age, grade in self.cursor.fetchall():
            studets.append(Student(id, name, age, grade))

        return studets

    def setStudents(self, student):
        self.cursor.execute('INSERT INTO players VALUES (?, ?, ?, ?)',
                            (student.id, student.name, student.age, student.grade))
        self.conn.commit()

    def updateStudent(self, student):
        self.cursor.execute(
            ('UPDATE players SET name = ?, age = ?, grade = ? WHERE id = ?',
             student.name, student.age, student.grade, student.id)
        )

        self.conn.commit()

    def deleteStudent(self, student):
        self.cursor.execute('DELETE FROM student WHERE id = ?',
                            ([student.id]))
        self.conn.commit()

from db.models.studentM import Student


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
                gender TEXT,
                grade TEXT,
                mail TEXT,
                date DATE NOT NULL default now()
            )
        ''')
        self.conn.commit()

    def getStudent(self):
        self.cursor.execute('''SELECT * FROM student''')
        studets = []
        for id, name, age, grade in self.cursor.fetchall():
            studets.append(Student(id, name, age, grade))

    #    self.conn.commit()

    def getStudentEmail(self, student):
        self.cursor.execute(
            "SELECT mail FROM student WHERE name= %s", [student])

        students = self.cursor.fetchone()()
        return students

    def setStudents(self, student):
        self.cursor.execute('''INSERT INTO student (id, matricula, name, last_name, age, gender, grade, mail) VALUES  (%s, %s, %s, %s, %s, %s, %s, %s)''',
                            (student.id, student.matricula, student.name, student.last_name, student.age, student.gender, student.grade, student.mail))
        self.conn.commit()

    def updateStudent(self, student):
        self.cursor.execute(
            ('''UPDATE players SET name = ?, age = ?, grade = ? WHERE id = ?''',
             student.name, student.age, student.grade, student.id)
        )

        self.conn.commit()

    def deleteStudent(self, student):
        self.cursor.execute('''DELETE * FROM student WHERE id = %s''',
                            ([student.id]))
        self.conn.commit()

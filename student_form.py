from tkinter import *
from entry_cap import entry_cap
import uuid

from db.connection import Database
from db.models.studentM import Student
from utils.createId import createId

database = Database()
def student_form():
    mywindow = Tk()
    def send_data():
        id = createId()
        matricula = createId()
        name = name_data.get()
        lastname = lastname_data.get()
        age = int(age_data.get())
        gender = gender_data.get()
        grade = grade_data.get()
        mail = mail_data.get()
        student = Student(id, matricula, name, lastname,  gender, age, grade, mail)
        database.student.setStudents(student)
        entry_cap(name_data, matricula, mywindow)
        database.close()


    
    mywindow.geometry("650x550")
    mywindow.title("Regristro de Estudiante")
    mywindow.resizable(False,False)
    mywindow.config(background = "#00ffff")
    main_title = Label(text="Formulario de Registro de Nuevo Estudiante",font=("Calibri",14), bg="#4FCAB5", fg="white", width="550", height="2")
    main_title.pack()
    name_label = Label(text="Nombres:", bg="#00ffff", font="30")
    name_label.place(x=22, y=70)
    lastname_label = Label(text="Apellidos:", bg="#00ffff", font="30")
    lastname_label.place(x=22, y=130)
    gender_label = Label(text="Género:", bg="#00ffff", font="30")
    gender_label.place(x=22, y=190)
    age_label = Label(text="Edad:", bg="#00ffff", font="30")
    age_label.place(x=22, y=250)
    grade_label = Label(text="Curso:",  bg="#00ffff", font="30")
    grade_label.place(x=22, y=310)
    mail_label = Label(text="Correo del Padre:", bg="#00ffff", font="30")
    mail_label.place(x=22, y=380)
    name_data = StringVar()
    lastname_data = StringVar()
    gender_data = StringVar()
    age_data = StringVar()
    grade_data = StringVar()
    mail_data = StringVar()
    name_entry = Entry(textvariable=name_data, width="30", font="30")
    lastname_entry = Entry(textvariable=lastname_data, width="30", font="30")
    gender_entry = Entry(textvariable=gender_data, width="30", font="30")
    age_entry = Entry(textvariable=age_data, width="20", font="30")
    grade_entry = Entry(textvariable=grade_data, width="30", font="30")
    mail_entry = Entry(textvariable=mail_data, width="30", font="30")

    name_entry.place(x=22, y=100)
    lastname_entry.place(x=22, y=160)
    gender_entry.place(x=22, y=220)
    age_entry.place(x=22, y=280)
    grade_entry.place(x=22, y=340)
    mail_entry.place(x=22, y=410)
    submit_btn = Button(mywindow, text="Registrar", font=("Calibri",15), command=send_data, width="20", height="2", bg="#00CD63")
    submit_btn.place(x=22, y=460)
    mywindow.mainloop()

from tkinter import *

def send_data(name_entry):
    print(name_entry)
    # pass

mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Regristro de Estudiante")
mywindow.resizable(False,False)
mywindow.config(background = "#00ffff")
main_title = Label(text="Formulario de Registro de Nuevo Estudiante",font=("Calibri",14), bg="#4FCAB5", fg="white", width="550", height="2")
main_title.pack()

name_label = Label(text="Nombres", bg="#FFEEDD", font="30")
name_label.place(x=22, y=70)
lastname_label = Label(text="Apellidos", bg="#FFEEDD", font="30")
lastname_label.place(x=22, y=130)
gender_label = Label(text="Género", bg="#FFEEDD", font="30")
gender_label.place(x=22, y=190)
age_label = Label(text="Edad", bg="#FFEEDD", font="30")
age_label.place(x=22, y=250)
grade_label = Label(text="Curso",  bg="#FFEEDD", font="30")
grade_label.place(x=22, y=310)
mail_label = Label(text="Correo del Padre", bg="#FFEEDD", font="30")
mail_label.place(x=22, y=380)

name = StringVar()
lastname = StringVar()
gender = StringVar()
age = StringVar()
grade = StringVar()
mail = StringVar()

name_entry = Entry(textvariable=name, width="40")
lastname_entry = Entry(textvariable=lastname, width="40")
gender_entry = Entry(textvariable=gender, width="40")
age_entry = Entry(textvariable=age, width="20")
grade_entry = Entry(textvariable=grade, width="40")
mail_entry = Entry(textvariable=mail, width="50")

name_entry.place(x=22, y=100)
lastname_entry.place(x=22, y=160)
gender_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)
grade_entry.place(x=22, y=340)
mail_entry.place(x=22, y=410)

submit_btn = Button(mywindow, text="Registrar", font=("Calibri",15) command=send_data(), width="30", height="2", bg="#00CD63")
submit_btn.place(x=22, y=480)

mywindow.mainloop()

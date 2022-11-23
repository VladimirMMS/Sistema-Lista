from tkinter import *
from student_form import student_form
from result_cap import scan_student

master = Tk()

def select_form():
    master.title("Registrar Estudiante")
    def get_seleted():
        if variable.get() == 'Registrar Estudiante':
            master.destroy()
            student_form()
        elif variable.get() == 'Escanear Estudiante':
            master.destroy()
            scan_student()
            
    variable = StringVar(master)
    variable.set("Selecciona la opcion que deseas")
    master.geometry("650x550")
    w = OptionMenu(master, variable, "Registrar Estudiante", "Escanear Estudiante")
   
    submit_btn = Button(master, text="Seleccionar", command=get_seleted, width="20" ,height="2", bg="#00ffff")
    submit_btn.place(x=245, y=50) 
    w.pack()
    mainloop()

select_form()
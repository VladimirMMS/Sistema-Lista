from tkinter import *

def student_form():
    main = Tk()
    def send_data():
        name_data = full_name.get()
        main.destroy()

    main.title("Registrar Estudiante")
    main.geometry("650x550")
    main.resizable(False, False)
    main.config(background="#00ffff")
    main_title = Label(text="Registrar estudiante", font=("Cambria", 13), fg="white", width="550", height="2", background="#4FCAB5")
    main_title.pack()
    name= Label(text="Nombre del estudiante:", bg="#00ffff", font="30")
    name.place(x=22, y=70)
    full_name=StringVar()
    name_entry=Entry(textvariable=full_name, width="40")
    name_entry.place(x=22, y=100)
    submit_btn = Button(main, text="Registrar", command=send_data, width="30" ,height="2", bg="#00CD63")
    submit_btn.place(x=22, y=130) 
    main.mainloop()
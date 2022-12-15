import cv2 as cv
import os
import numpy as np
from tkinter import *
import time


def hiden_training_cap(second_window):

    def close():
        second_window.destroy()

    second_window.geometry("650x550")
    second_window.title("Menu de Espera")
    second_window.resizable(False,False)
    second_window.config(background = "#00ffff")
    main_title = Label(text="Esperar Mientras las tomas se registran...",font=("Calibri",14), bg="#4FCAB5", fg="white", width="550", height="2")
    submit_btn = Button(second_window, text="Cerrar Ventana", font=("Calibri",15), command=close, width="20", height="2", bg="#00CD63")
    submit_btn.place(x=202, y=160)
    main_title.pack()
    second_window.mainloop()
    data_ruta='C:/Users/vladi/OneDrive/Desktop/Sistema-Lista/data'
    list_data=os.listdir(data_ruta)
    ids =[]
    face_data=[]
    id=0
    for row in list_data:
        completed_route=data_ruta+'/'+row
        for file in os.listdir(completed_route):
            ids.append(id)
            face_data.append(cv.imread(completed_route+'/'+file, 0))
        id=id+1
    training_eigen_face_recognizer=cv.face.EigenFaceRecognizer_create()
    training_eigen_face_recognizer.train(face_data, np.array(ids))
    training_eigen_face_recognizer.write('training_eigen_face_recognizer.xml')
    print('Training finished')

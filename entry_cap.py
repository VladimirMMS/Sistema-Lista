import cv2 as cv
import os
import imutils
from hiden_training_cap import hiden_training_cap
from tkinter import *
from hiden_training_cap import hiden_training_cap 


def entry_cap(name, matricula, window):
    window.destroy()
    second_window = Tk()
    model='data/{}-{}'.format(name, matricula)
    ruta1='C:/Users/vladi/OneDrive/Desktop/Sistema-Lista'
    ruta_completa=ruta1+'/{}'.format(model)
    if not os.path.exists(ruta_completa):
        os.makedirs(ruta_completa)
    ruidos=cv.CascadeClassifier(r"C:/Users/vladi/OneDrive/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml")
    camara= cv.VideoCapture(0)
    id=1
    while True:
        respuesta,captura=camara.read()
        if respuesta==False: break
        captura=imutils.resize(captura, width=640)
        grises=cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
        caras=ruidos.detectMultiScale(grises,1.3,5)
        id_captura=captura.copy()

        for x,y, e1, e2 in caras:
            cv.rectangle(captura, (x,y), (x+e1, y+e2), (255, 0, 0), 2)
            face_captured=id_captura[y:y+e2, x: x+e1]
            face_captured=cv.resize(face_captured, (160, 160), interpolation=cv.INTER_CUBIC)
            cv.imwrite(ruta_completa+'/imagen_{}.jpg'.format(id), face_captured)
            id=id+1
        cv.imshow("Resultado rostro", captura)
        if id == 600 or (cv.waitKey(1) == ord("q")):
            break

    camara.release()
    cv.destroyAllWindows()
    hiden_training_cap(second_window)
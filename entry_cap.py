import cv2 as cv
import os
import imutils

model='data/FotosVladimir'
ruta1='C:/Users/Intellisys/Desktop/universidad-pro'
ruta_completa=ruta1+'/{}'.format(model)
if not os.path.exists(ruta_completa):
    os.makedirs(ruta_completa)

ruidos=cv.CascadeClassifier(r"C:\Users\Intellisys\Desktop\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
camara= cv.VideoCapture(0)
id=0
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
    if id == 100:
        break

camara.release()
cv.destroyAllWindows()
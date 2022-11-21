import cv2 as cv
import os

data_ruta='C:/Users/Intellisys/Desktop/universidad-pro/data'
list_data=os.listdir(data_ruta)

training_eigen_face_recognizer=cv.face.EigenFaceRecognizer_create()
training_eigen_face_recognizer.read('training_eigen_face_recognizer.xml')
ruidos=cv.CascadeClassifier(r"C:\Users\Intellisys\Desktop\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
camara=cv.VideoCapture(0)


while True:
    _,captura=camara.read()
    grises=cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    id_captura=grises.copy()
    caras=ruidos.detectMultiScale(grises, 1.3, 5)
    for x,y, e1, e2 in caras:
        face_captured=id_captura[y:y+e2, x: x+e1]
        face_captured=cv.resize(face_captured, (160, 160), interpolation=cv.INTER_CUBIC)
        result=training_eigen_face_recognizer.predict(face_captured)
        cv.putText(captura, '{}'.format(result), (x,y-5),1,1.3, (0, 225, 0), 1, cv.LINE_AA)
        if result[1] < 9200:
            cv.putText(captura, '{}'.format(list_data[result[0]]), (x,y-20),2,1.1, (0, 225, 0), 1, cv.LINE_AA)
            cv.rectangle(captura, (x, y), (x+e1, y+e2), (255, 0, 0),2)
        else:
            cv.putText(captura, 'No Found', (x,y-20),2,1.1, (0, 225, 0), 1, cv.LINE_AA)
            cv.rectangle(captura, (x, y), (x+e1, y+e2), (255, 0, 0),2)
    cv.imshow("Results", captura)
    if cv.waitKey(1) == ord('s'):
        break
camara.release()
cv.destroyAllWindows()
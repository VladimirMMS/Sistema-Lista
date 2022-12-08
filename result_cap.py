import cv2 as cv
import os

def scan_student():
    data_ruta='C:/Users/vladi/OneDrive/Desktop/Sistema-Lista/data'
    dataList=os.listdir(data_ruta)

    trainingModel=cv.face.EigenFaceRecognizer_create()
    trainingModel.read('training_eigen_face_recognizer.xml')
    ruidos=cv.CascadeClassifier(r"C:\Users\vladi\OneDrive\Desktop\opencv\data\haarcascades\haarcascade_frontalface_default.xml")
    Camera=cv.VideoCapture(0)

    Camera = cv.VideoCapture(0)

    while True:
        response, frame = Camera.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        captureId = gray.copy()
        face = ruidos.detectMultiScale(gray, 1.3, 7)
        for (x,y,e1,e2) in face:        
            faceCapture=captureId[y:y+e2, x:x+e1]
            faceCapture=cv.resize(faceCapture, (160, 160), interpolation=cv.INTER_CUBIC)
            result = trainingModel.predict(faceCapture)
            cv.putText(frame, '{}'.format(result), (x, y-5), 1, 1.2, (0, 255, 0), 2, cv.LINE_AA)
            if result[1] < 5500:
                name = dataList[result[0]].split("-")[0]
                print(dataList[result[0]])
                cv.putText(frame, '{}'.format(name), (x, y-20), 1, 1.3, (0, 255, 0), 2, cv.LINE_AA)            
                cv.rectangle(frame, (x,y), (x+e1, y+e2), (255, 0, 0), 2)
            else:
                cv.putText(frame, ('No encontrado'), (x, y-20), 2, 1.1, (0, 255, 0), 2, cv.LINE_AA)            
                cv.rectangle(frame, (x,y), (x+e1, y+e2), (255, 0, 0), 2)
        cv.imshow("Escanear Estudiante", frame)
        if(cv.waitKey(1) == ord("q")):
            break
    Camera.release()
    cv.destroyAllWindows()
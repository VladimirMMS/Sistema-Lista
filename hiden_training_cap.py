import cv2 as cv
import os
import numpy as np

data_ruta='C:/Users/User/Desktop/Universidad/Tercer Ciclo/Pensamiento Critico/Proyecto final/Sistema-Lista/data'
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
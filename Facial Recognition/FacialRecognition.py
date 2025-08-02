import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import cv2
import numpy as np
import face_recognition

imgEl = face_recognition.load_image_file(r"C:\Users\ibikh\PycharmProjects\PythonProject3\elonmuskk.jpg")
imgEl = cv2.cvtColor(imgEl, cv2.COLOR_BGR2RGB)

imgTe = face_recognition.load_image_file(r"C:\Users\ibikh\PycharmProjects\PythonProject3\bg.jpg")
imgTe = cv2.cvtColor(imgTe, cv2.COLOR_BGR2RGB)


faceLoc = face_recognition.face_locations(imgEl)[0]
encodeEl = face_recognition.face_encodings(imgEl)[0]
cv2.rectangle(imgEl,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(255,0,255),2)

faceLocT = face_recognition.face_locations(imgTe)[0]
encodeTe = face_recognition.face_encodings(imgTe)[0]
cv2.rectangle(imgTe,(faceLocT[3], faceLocT[0]),(faceLocT[1], faceLocT[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeEl],encodeTe)
faceDis = face_recognition.face_distance([encodeEl],encodeTe)
print(faceDis,results)
cv2.putText(imgTe,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
cv2.imshow('Elon Musk', imgEl)
cv2.imshow('Elon Test', imgTe)
cv2.waitKey(0)



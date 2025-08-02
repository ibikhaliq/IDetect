import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
cap = cv2.VideoCapture(0)

path = r'C:\Users\ibikh\PycharmProjects\PythonProject3\attendancefaces'
images = []
classNames = []
list = os.listdir(path)
print(list)
for cl in list:
    currimg = cv2.imread(f'{path}/{cl}')
    images.append(currimg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findencodings(images):
    encodeList= []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListknown = findencodings(images)
print('Encoding Complete')



def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H: %M: %S')
            f.writelines(f'\n{name},{dtString}')

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0), None, 0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facecurframe = face_recognition.face_locations(imgS)
    encodecurrframe = face_recognition.face_encodings(imgS,facecurframe)

    for encodeFace, faceLoc in zip(encodecurrframe, facecurframe):
        matches = face_recognition.compare_faces(encodeListknown, encodeFace)
        faceDist = face_recognition.face_distance(encodeListknown, encodeFace)
        #print(faceDist)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            markAttendance(name)
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
            markAttendance(name)
    cv2.imshow("Webcam", img) #shows webcam
    cv2.waitKey(1)

















 # faceLoc = face_recognition.face_locations(imgEl)[0]
# encodeEl = face_recognition.face_encodings(imgEl)[0]
# cv2.rectangle(imgEl,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(255,0,255),2)
#
# faceLocT = face_recognition.face_locations(imgTe)[0]
# encodeTe = face_recognition.face_encodings(imgTe)[0]
# cv2.rectangle(imgTe,(faceLocT[3], faceLocT[0]),(faceLocT[1], faceLocT[2]),(255,0,255),2)
#
# results = face_recognition.compare_faces([encodeEl],encodeTe)
# faceDis = face_recognition.face_distance([encodeEl],encodeTe)


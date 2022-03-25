from re import S
from tkinter import SW
from handDetector import HandDetector
import cv2

handDetector = HandDetector(min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

while True:
    status, image = cap.read()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count=0

    if(len(handLandmarks) != 0):

        if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:
            count = count+1
        elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:
            count = count+1
        if handLandmarks[8][2] < handLandmarks[6][2]:
            count = count+1
        if handLandmarks[12][2] < handLandmarks[10][2]:
            count = count+1
        if handLandmarks[16][2] < handLandmarks[14][2]:
            count = count+1
        if handLandmarks[20][2] < handLandmarks[18][2]:
            count = count+1
    if count == 0: w = "Nol"
    elif count == 1: w = "Satu"
    elif count == 2: w = "Dua"
    elif count == 3: w = "Tiga"
    elif count == 4: w = "Empat"
    elif count == 5: w = "Lima"
    cv2.putText(image, w, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 100, 0), 10)
    cv2.imshow("1 2 3 4 5", image)
    cv2.waitKey(1)

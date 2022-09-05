import cv2
#start relay
from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import AngularServo
import math
import numpy as np
import dlib

servo =AngularServo(12, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)
#end relay


# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
#Face Detector
detector = dlib.get_frontal_face_detector()


while True:
    # Read the frame
    ret, img = cap.read()
    img = cv2.flip(img,1)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    
    count_face = 0
    for (x, y, w, h) in faces:
        print("GET IN WHILE LOOP")
#       count_face = count_face+1
        cv2.rectangle(img, (x, y),(x+w, y+h), (255, 0, 0), 2)
        
        count_face = count_face+1
#         print("FACE="+str(count_face))
        cv2.putText(img,"face num"+str(count_face),(x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
        print(faces,count_face)
        print(count_face)
        
            
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()

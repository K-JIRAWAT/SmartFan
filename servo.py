import cv2
#start relay
from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import AngularServo
import math

servo =AngularServo(12, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)

# Load the
# face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
    
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    count_face=0
    for (x, y, w, h) in faces:
        count_face=count_face+1
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print("FACE="+str(count_face))
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()

def servo_on():
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.040)

def servo_off():
        servo.value=0
        sleep(0.040)

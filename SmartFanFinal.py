import RPi.GPIO as GPIO
import cv2
#start relay
from gpiozero import Servo
from time import sleep
from gpiozero import AngularServo
import math
import numpy as np
import dlib
import time

global a
a = 0

channel = 21
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.output(channel, GPIO.LOW) 

#GPIO.setup(21, GPIO.OUT)
#GPIO.output(21, GPIO.HIGH)

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

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
    
def servo_on(a):
    i = 0
    print("MOTOR ON")
    motor_on(channel)
    print("SERVO ON")
    if(a==0):
        if(i<359):
            for i in range(0, 360):
                print("i :",i)
                servo.value = math.sin(math.radians(i))
                sleep(0.040)
        if(i==359):
            print("I = 360 TURN MOTOR OFF")
            motor_off(channel)
            a=1

#     motor_off(channel)
        
    
            
           

def servo_off():
    print("MOTOR OFF")
    motor_on(channel)
    print("SERVO OFF")
    servo.value=0
    sleep(0.040)

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
#       count_face = count_face+1
        cv2.rectangle(img, (x, y),(x+w, y+h), (255, 0, 0), 2)
        
        count_face = count_face+1
        print("FACE="+str(count_face))
        cv2.putText(img,"face num"+str(count_face),(x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2)
        #print(faces,count_face)
        #print(count_face)
        
        
        

             
        if(count_face<=1):          
            servo_off()
           
            
            
        if(a==0):
            if(count_face>1):
                servo_on(a)
                
             
            
                        
            
    
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
GPIO.output(channel, GPIO.LOW) 
GPIO.cleanup()


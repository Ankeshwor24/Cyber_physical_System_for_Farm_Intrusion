import RPi.GPIO as GPIO
import time
from picamera import PiCamera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)
#LED output pin
camera = PiCamera()
while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        GPIO.output(3, 0)  #Turn OFF LED
        time.sleep(5)
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        GPIO.output(3, 1)  #Turn ON LED
        camera.capture("/home/pi/Pictures/mynoimg.jpg")
        print("Done.")
        time.sleep(5)
        GPIO.output(3, 0)  #Turn OFF LED
        exit()


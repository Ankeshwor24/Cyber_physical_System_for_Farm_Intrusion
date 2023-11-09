from gpiozero import Buzzer
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
buzzer = Buzzer(27)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
while True:
    buzzer.on()
    GPIO.output(5, 1)  #Turn OFF LED
    GPIO.output(3, 1)
    sleep(1)
    buzzer.off()
    GPIO.output(5, 0)
    GPIO.output(3, 0)
    sleep(0.5)
    

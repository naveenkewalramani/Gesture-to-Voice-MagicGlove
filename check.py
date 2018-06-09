import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.IN)

while True:
    print(GPIO.input(9))
    time.sleep(2)
    

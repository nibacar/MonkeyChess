import time, sys
import RPi. GPIO as GPIO

GPIO.setmode (GPIO.BOARD)
GPIO.setup(15, GPIO .IN, pull_up_down = GPIO.PUD_UP)
while True:
    if GPIO.input == GPIO.HIGH:
        print("NO MAGNET")
    else: 
        print("OMG A MAGNET")
     

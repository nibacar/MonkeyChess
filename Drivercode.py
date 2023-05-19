import time, sys
import RPi. GPIO as GPIO

GPIO.setmode (GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    arrayrows = [[GPIO.output(15),GPIO.output(13)]]
    arraycolumns =[[GPIO.input(18),GPIO.input(16)]]
    print("Magnet is on row:" + arrayrows.index(0)+1 + "\n and column: " + arraycolumns.index(0)+1)

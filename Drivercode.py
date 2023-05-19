import time, sys
import RPi. GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
    while True:
        arrayrows = [[GPIO.output(15, GPIO.LOW),GPIO.output(13, GPIO.LOW)]]
        arraycolumns =[[GPIO.input(18),GPIO.input(16)]]
        print("Magnet is on row:" + arrayrows.index(0)+1 + "\n and column: " + arraycolumns.index(0)+1)

except KeyboardInterrupt:
    GPIO.cleanup()

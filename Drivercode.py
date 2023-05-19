import time, sys
import RPi. GPIO as GPIO

outputs = [15, 13]
inputs = [18, 16]
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(outputs, GPIO.OUT)
GPIO.setup(inputs, GPIO.IN, pull_up_down = GPIO.PUD_UP)
arrayrows = [[GPIO.output(15, GPIO.LOW),GPIO.output(13, GPIO.LOW)]]
arraycolumns =[[GPIO.input(18),GPIO.input(16)]]
try:
    while True:
        for i in outputs:
            GPIO.output(i, GPIO.HIGH)
            for j in inputs:
                if GPIO.input(j) == 0:
                    print("Magnet is on row:" + i + " and column: " + j)
            GPIO.output(outputs, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()

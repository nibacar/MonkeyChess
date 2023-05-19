import time, sys
import RPi. GPIO as GPIO

outputs = [15, 13]
inputs = [18, 16]
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(outputs, GPIO.OUT)
GPIO.setup(inputs, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
    while True:
        for i in outputs:
            GPIO.output(i, GPIO.HIGH)
            for j in inputs:
                if GPIO.input(j) == 0:
                    print("Magnet is on row:" + str(outputs.index(i)) + " and column: " + str(inputs.index(j)))
            GPIO.output(outputs, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()

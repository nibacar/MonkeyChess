import RPi.GPIO as GPIO
import time

# Define the GPIO pins for rows and columns
row_pins = [2, 3, 4, 17]  # Example row GPIO pins
col_pins = [11, 5, 6, 13]  # Example column GPIO pins

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for rows as inputs with pull-up resistors
for row_pin in row_pins:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up GPIO pins for columns as outputs
for col_pin in col_pins:
    GPIO.setup(col_pin, GPIO.OUT)

def detect_magnets():
    magnets = []
    for col_pin in col_pins:
        # Set the current column pin to LOW
        GPIO.output(col_pin, GPIO.LOW)
        time.sleep(0.01)  # Adjust the delay here if needed

        # Read the state of all row pins
        states = [GPIO.input(row_pin) for row_pin in row_pins]

        # Check if magnets are detected in any row
        for row, state in enumerate(states):
            if state == GPIO.LOW:
                magnets.append((row, col_pins.index(col_pin)))

        # Reset the current column pin to HIGH
        GPIO.output(col_pin, GPIO.HIGH)

    return magnets

try:
    while True:
        input("Press Enter to detect magnets...")
        magnets = detect_magnets()
        if magnets:
            print("Magnets detected at:")
            for magnet in magnets:
                print(f"Row: {magnet[0]+1}, Column: {magnet[1]+1}")
        else:
            print("No magnets detected.")

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()

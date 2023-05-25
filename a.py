import RPi.GPIO as GPIO
import time

# Define the GPIO pins for rows and columns
row_pins = [16, 15, 13, 11]  # Example row GPIO pins
col_pins = [36, 31, 29, 18]  # Example column GPIO pins

# Set up GPIO mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for rows as inputs with pull-up resistors
for row_pin in row_pins:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def detect_magnets():
    magnets = []
    for col_pin in col_pins:
        GPIO.setup(col_pin, GPIO.OUT)  # Set the current column pin as output
        GPIO.output(col_pin, GPIO.LOW)  # Set the current column pin to LOW
        time.sleep(0.01)  # Adjust the delay here if needed

        for row_pin in row_pins:
            GPIO.setup(row_pin, GPIO.IN)  # Set the current row pin as input
            state = GPIO.input(row_pin)  # Read the state of the current row pin

            # Check if a magnet is detected
            if state == GPIO.LOW:
                # Magnet detected, get the row and column
                row = row_pins.index(row_pin)
                col = col_pins.index(col_pin)
                magnets.append((row, col))

        GPIO.setup(col_pin, GPIO.IN)  # Reset the current column pin as input

    return magnets

try:
    while True:
        input("Press Enter to detect magnets...")
        magnets = detect_magnets()
        if magnets:
            print("Magnets detected at:")
            for magnet in magnets:
                print(f"Row: {magnet[0]}, Column: {magnet[1]}")
        else:
            print("No magnets detected.")

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()

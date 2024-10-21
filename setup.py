import Jetson.GPIO as GPIO
import time

# Set GPIO mode to BOARD (uses physical pin numbering)
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins for Trigger and Echo (physical pin numbers)
TRIG = 12 # Pin 12 for Trigger

ECHO = 14  # Pin 14 for Echo

IN1 = 21   # GPIO pin for motor 1 forward
IN2 = 22  # GPIO pin for motor 1 backward
IN3 = 23  # GPIO pin for motor 2 left
IN4 = 24  # GPIO pin for motor 2 right

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Ensure Trigger is set to Low and motors off
GPIO.output(TRIG, False)
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Ensure Trigger is set to Low
GPIO.output(TRIG, False)
print("Waiting for sensor to settle...")
time.sleep(2)

def get_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(TRIG, False)

    # Wait for the echo to start
    pulse_start = time.time()
    timeout = pulse_start + 0.01  # Timeout after 10 milliseconds
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > timeout:
            print("Timeout: No pulse start detected")
            return -1  # Return -1 on timeout

    # Wait for the echo to end
    pulse_end = time.time()
    timeout = pulse_end + 0.01  # Timeout after 10 milliseconds
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > timeout:
            print("Timeout: No pulse end detected")
            return -1  # Return -1 on timeout

    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance in centimeters
    distance = pulse_duration * 17150  # Speed of sound in cm/us
    return round(distance, 2)


# Function to move the vehicle straight
def move_straight():
    GPIO.output(IN1, True
)   # Forward motion
    GPIO.output(IN2, False)  # No reverse
    GPIO.output(IN3, False)  # No left
    GPIO.output(IN4, False)  # No right

# Function to turn the vehicle left
def turn_left():
    GPIO.output(IN1, False)  # No forward
    GPIO.output(IN2, False)  # No reverse
    GPIO.output(IN3, True)   # Turn left
    GPIO.output(IN4, False)  # No right

# Function to stop the vehicle
def stop_motors():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

try:
    while True:
        dist = get_distance()
        if dist == -1:
            print("Failed to get distance, retrying...")
            continue  # Skip this iteration if no valid distance was measured

        print("Distance:",dist,"cm")

        # If obstacle is detected within 20 cm, turn left
        if dist < 20 and dist != -1:
            print("Obstacle detected! Turning left...")
            turn_left()
        else:
            print("No obstacle, moving straight...")
            move_straight()

        time.sleep(1)  # Delay before the next reading

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    stop_motors()  # Ensure the motors stop
    GPIO.cleanup()  # Clean up GPIO settings

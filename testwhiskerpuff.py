import time
import RPi.GPIO as GPIO


# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# DEFINE PINS
leftpuff = 8
rightpuff = 7


# INITIALIZE PINS
GPIO.setup(leftpuff, GPIO.OUT, initial=0)
GPIO.setup(rightpuff, GPIO.OUT, initial=0)

# ENTER VARIABLES RANGE TO TEST
timeoninsec = 1
inbetweensec = 1

# SCRIPT
GPIO.output(leftpuff, 1)
print('left on GPIO 8')
time.sleep(timeoninsec)
GPIO.output(leftpuff, 0)
print('OFF left GPIO 8')
time.sleep(inbetweensec)
GPIO.output(rightpuff, 1)
print('left on GPIO 8')
time.sleep(timeoninsec)
GPIO.output(rightpuff, 0)
print('OFF left GPIO 8')
time.sleep(inbetweensec)



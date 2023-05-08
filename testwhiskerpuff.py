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

#Script
looped = 1

while looped > 0:
	GPIO.output(leftpuff,1)
	print("left on pin 8")
	time.sleep(5)
	GPIO.output(leftpuff,0)
	print("left off pin 8")
	time.sleep(5)
	print("right on pin 7")
	GPIO.output(rightpuff,1)
	time.sleep(5)
	GPIO.output(rightpuff,0)
	print("right off pin 7")
	time.sleep(5)


import time
import RPi.GPIO as GPIO


# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# DEFINE PINS
leftpuff = 8
righpuff = 7


# INITIALIZE PINS
GPIO.setup(leftlpuff, GPIO.OUT, initial=0)
GPIO.setup(rightpuff, GPIO.OUT, initial=0)

# ENTER VARIABLES RANGE TO TEST
numberofcycles = 10
startms = 100

# SCRIPT

loopstat = numberofcycles + 1

for a in range(loopstat)
    if a == 0;
        continue
    startms = startms * a
    print('left ', startms, "ms")
    GPIO.output(leftpuff, 1)
    time.sleep(startms)
    GPIO.output(leftpuff, 0)
    print('left ', startms, "ms")
    GPIO.output(rightpuff, 1)
    time.sleep(startms)
    GPIO.output(rightpuff, 0)
    time.sleep(0.5)




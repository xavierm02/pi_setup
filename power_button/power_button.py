#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import subprocess

secondsToShutdown = 5

GPIO.setmode(GPIO.BOARD)

# we will use the pin numbering to match the pins on the Pi, instead of the
# GPIO pin outs (makes it easier to keep track of things)
# use the same pin that is used for the reset button (one button to rule them all!)
GPIO.setup(5, GPIO.IN)

buttonState = True
buttonStateChangeDate = time.time()

while True:
		newButtonState = GPIO.input(5)
		
		if newButtonState != buttonState:
			print("State just changed. Last change was " + str(buttonStateChangeDate - time.time()) + "s ago.")
			buttonState = newButtonState
			buttonStateChangeDate = time.time()
		
		if buttonState and buttonStateChangeDate - time.time() >= secondsToShutdown:
			subprocess.call("shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		time.sleep(.5)

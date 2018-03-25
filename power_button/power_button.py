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
		newButtonState = not(GPIO.input(5)) # True if button is pressed
		
		if newButtonState != buttonState:
			print("State just changed. Last change was " + str(time.time() - buttonStateChangeDate) + "s ago.")
			buttonState = newButtonState
			buttonStateChangeDate = time.time()
		
		if buttonState and time.time() - buttonStateChangeDate >= secondsToShutdown:
			subprocess.call("shutdown -h now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		time.sleep(.5)

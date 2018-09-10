#!/usr/bin/python3

from datetime import datetime
import RPi.GPIO as GPIO
import signal
import subprocess
import sys
import time
import traceback



secondsToShutdown = 5

power_button = 3



cleaned = False

def clean(*args):
	global cleaned
	print("Cleaning power_button.")
	if not(cleaned):
		GPIO.cleanup()
		cleaned = True
	sys.exit(0)

for sig in (signal.SIGABRT, signal.SIGINT, signal.SIGTERM):
	signal.signal(sig, clean)



try:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(power_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	pressed = not(GPIO.input(power_button))
	if pressed:
		press_date = datetime.now()
		print("Power button initially pressed (" + str(press_date) + ").")
	else:
		press_date = None
		print("Power button initially not pressed (" + str(datetime.now()) + ").")
	
	while True:
		new_pressed = not(GPIO.input(power_button))
		
		if new_pressed != pressed:
			pressed = new_pressed
			if pressed:
				press_date = datetime.now()
				print("Power button pressed at " + str(press_date) + ".")
			
			else:
				release_date = datetime.now()
				time_pressed = release_date - press_date
				print("Power button realeased at " + str(release_date) + " (" + str(time_pressed) + " after being pressed).")
				
				if time_pressed.total_seconds() >= secondsToShutdown:
					print("Shutting down!")
					subprocess.call(['shutdown', '-h', 'now'], shell=False)
					
				press_date = None
		
		time.sleep(0.1)

except:
	traceback.print_exc()

finally:
	clean()

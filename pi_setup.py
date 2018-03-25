#!/usr/bin/python3

import lib.py_run as py_run
import os

def sudo_cp_f(source, target):
	cmd = "sudo cp -f " + source + " " + target
	cmd_str = "sudo cp -f " + py_run.uri(source) + " " + py_run.uri(target)
	py_run.run(cmd, cmd_str=cmd_str, error_fatal=False)

def setup_power_button():
	# requires python3-rpi.gpio
	sudo_cp_f(os.path.realpath("./power_button/power_button"), "/etc/init.d/power_button")
	py_run.run("sudo update-rc.d power_button defaults")
	py_run.run("sudo python /home/pi/pi_setup/power_button/power_button.py &> /dev/null &")
	
setup_power_button()

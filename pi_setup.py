#!/usr/bin/python3

import lib.py_run as py_run
import os

def ln_s(source, target):
	cmd = "ln -s " + source + " " + target
	cmd_str = "ln -s " + py_run.uri(source) + " " + py_run.uri(target)
	py_run.run(cmd, cmd_str=cmd_str, error_fatal=True)
		

def sudo_ln_s(source, target):
	cmd = "sudo ln -s " + source + " " + target
	cmd_str = "sudo ln -s " + py_run.uri(source) + " " + py_run.uri(target)
	py_run.run(cmd, cmd_str=cmd_str, error_fatal=True)

def setup_power_button():
	# requires python3-rpi.gpio
	sudo_ln_s(os.path.realpath("./power_button/power_button"), "/etc/init.d/power_button")
	py_run.run("sudo update-rc.d power_button defaults")
	py_run.run("sudo python /home/pi/pi_setup/power_button/power_button.py &> /dev/null &")
	
setup_power_button()

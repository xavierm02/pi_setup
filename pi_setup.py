#!/usr/bin/python3

import lib.py_run as py_run
import os

def ln_s(source, target):
	cmd = "ln -s " + source + " " + target
	cmd_str = "ln -s " + py_run.uri(source) + " " + py_run.uri(target)
	py_run.run(cmd, cmd_str=cmd_str, error_fatal=True)
		

def sudo_ln_s(source, target):
	cmd = "ln -s " + source + " " + target
	cmd_str = "ln -s " + py_run.uri(source) + " " + py_run.uri(target)
	py_run.run(cmd, cmd_str=cmd_str, error_fatal=True)

def setup_power_button():
	ln_s(os.path.realpath("./power_button/power_button.rc"), "/etc/init.d/power_button.rc")
	
setup_power_button()

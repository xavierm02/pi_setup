all: power_led

init:
	sudo apt install python3-pip python3-rpi.gpio hostapd haveged
	pip3 install py-term

init_script:
ifeq ($(name),)
	echo "make init_script needs a name argument."
	exit 1
else
	sudo cp $(name)/$(name).py /usr/local/bin/__$(name).py
	sudo chmod +x /usr/local/bin/__$(name).py
	sudo cp $(name)/$(name).sh /etc/init.d/__$(name).sh
	sudo chmod +x /etc/init.d/__$(name).sh
	sudo update-rc.d __$(name).sh defaults
	sudo /etc/init.d/__$(name).sh stop
	sudo /etc/init.d/__$(name).sh start
endif

power_button:
	make init_script name=power_button

.PHONY: all init init_script power_button

all: power_button dance_mat

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

dance_mat: dance_mat/pi-as-keyboard

dance_mat/pi-as-keyboard:
	(cd dance_mat; git clone https://github.com/c4software/pi-as-keyboard.git)
	(cd dance_mat/pi-as-keyboard; sudo ./setup.sh)

.PHONY: all init init_script power_button dance_mat

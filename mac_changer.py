#!/usr/bin/env_python3

import subprocess
import optparse

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="specify interface to change")
	parser.add_option("-m", "--mac", dest="new_mac", help="enter new mac address for inteface")
	return parser.parse_args()

def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac) 
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

# read arguments and parse data; returns args and values
(options, arguments) = get_args()
# access values in function call to update the mac address 
change_mac(options.interface, options.new_mac)



#!/usr/bin/env_python3

import subprocess
import optparse

# function that takes the CL arguments and executes our script
def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac) 
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

# create an instance of the OptionParser class
parser = optparse.OptionParser()

# specify different ways to specify argument and where value will be stored from user input
parser.add_option("-i", "--interface", dest="interface", help="specify the interface you want to change MAC address")
parser.add_option("-m", "--mac", "--MAC", dest="new_mac", help="specifiy new MAC address")

# method that captures arguments and options into variables
(options, arguments) = parser.parse_args()

# access values in function call to update the mac address 
change_mac(options.interface, options.new_mac)



#!/usr/bin/env_python3

import subprocess
import optparse

# create an instance of the OptionParser class
parser = optparse.OptionParser()

# specify different ways to specify argument and where value will be stored from user input
parser.add_option("-i", "--interface", dest="interface", help="specify the interface you want to change MAC address")
parser.add_option("-m", "--mac", "--MAC", dest="new_mac", help="specifiy new MAC address")

# method that captures arguments and options into variables
(options, arguments) = parser.parse_args()

# access cl arg values - connect variables to destination values
interface = options.interface
new_mac = options.new_mac

print(f"[+] Changing MAC address for {interface} to {new_mac}")

# command we want to execute and run linux commands
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

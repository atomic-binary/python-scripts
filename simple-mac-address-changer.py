#!/usr/bin/env python3

import subprocess

print("[+] Starting MAC address changer............\n")
subprocess.call("ifconfig", shell=True)
#Replace the interface name with eth0 in below line.
# subprocess.call("ifconfig eth0 down", shell=True)
# subprocess.call("ifconfig eth0 hw 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig eth0 up", shell=True)

#Using variables for interface and mac address.
#Use raw_input() for python 2.7
interface = input("Enter the interface name: ")
new_mac_addr = input("Please enter the new mac address: ")

print("[+] Changing MAC address for interface: " + interface + " to: " + new_mac_addr)

# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac_addr, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
#This way of calling "subprocess.call()" is very dangerous as any command can be run by modifying the input 
# as every string can be interpreted as command if escape character is used like ";".
# Example: input for interface = eth0;ls;

#Better way to use "subprocess.call()" is as below, because here only the first argument will be 
#interpreted as command and rest will be considered as the arguments/parts of the initial command.
subprocess.call(["ifconfig", interface, "down"])
#Here same command is split in multiple parts/elements wherever space is encountered.
#Now python knows that interface and down are all parts of the same command ifconfig, and will not treat 
# them as separate commands. Python will try to treat it as a argument to ifconfig command.
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_addr])
subprocess.call(["ifconfig", interface, "up"])

#!/usr/bin/env python3

import subprocess

print("[+] Starting MAC address changer............\n")
subprocess.call("ifconfig", shell=True)
#Replace the interface name with eth0 in below line.
# subprocess.call("ifconfig eth0 down", shell=True)
# subprocess.call("ifconfig eth0 hw 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig eth0 up", shell=True)

#Using variables for interface and mac address.
interface = input("Enter the interface name: ")
new_mac_addr = input("Please enter the new mac address: ")

print("[+] Changing MAC address for interface: " + interface + " to: " + new_mac_addr)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac_addr, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

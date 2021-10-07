#!/usr/bin/env python3

import subprocess
import optparse

subprocess.call("ifconfig")

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest=interface, help="Interface of which mac address is to be changed.")
parser.add_option("-m", "--mac", dest=new_mac_addr, help="New MAC address.")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac_addr = options.new_mac_addr

print("[+] Changing MAC address for " + interface + " to " + new_mac_addr)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_addr])
subprocess.call(["ifconfig", interface, "up"])

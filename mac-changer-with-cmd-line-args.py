#!/usr/bin/env python3

import subprocess
import optparse

# subprocess.call("ifconfig")

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest=interface, help="Interface of which mac address is to be changed.")
parser.parse_args()

interface = input("Enter interface: ")

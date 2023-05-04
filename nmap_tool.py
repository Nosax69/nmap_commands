#!/bin/python3
import subprocess
import optparse

p = optparse.OptionParser()

p.add_option("-i", "--ip",  dest="ip_address", help="IP for scanning")
p.add_option("-c", "--commands", dest="scan_network", help="To scan all host")
#p.add_option("-V", "--sV", dest="scan_network", help="To scan all host")

(options, arguments) = p.parse_args()

ip_address = options.ip_address
scan_network = options.scan_network

if scan_network:
    commands = scan_network.split(",")
    commands.insert(0, "-sS")  # Always use TCP SYN scan
    subprocess.call(["nmap"] + commands + [ip_address])
else:
    p.print_help()
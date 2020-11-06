#!/usr/bin/env python
import subprocess
import argparse
import re


""" MAC CHANGER - changes MAC Address to anything desired. """


def get_arguments():
    """Input commands:<interface> <mac> <help> on the terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    args = parser.parse_args()
    if not args.interface:
        parser.error("Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("Please specify a new MAC address, use --help for more info.")
    return args

def change_mac(interface, new_mac):
    """Change MAC address."""
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    """Prints MAC address using Regex."""
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read the MAC address")

args = get_arguments()
current_mac = get_current_mac(args.interface)
print("Current MAC = " + str(current_mac))

change_mac(args.interface, args.new_mac)

current_mac = get_current_mac(args.interface)
if current_mac == args.new_mac:
    print("MAC address was successfully changed to " + current_mac)
else:
    print("MAC address did not get changed.")

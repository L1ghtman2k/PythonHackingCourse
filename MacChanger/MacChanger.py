#!/usr/bin/python3
import subprocess
import re
import netifaces
import optparse


def mac_changer(interface, macAddress):
    pattern = re.compile(r"^([0-9a-f]{2}[:-]){5}([0-9a-f]{2})$", re.IGNORECASE)
    if pattern.match(macAddress) and netifaces.AF_INET in netifaces.ifaddresses(interface):
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
        subprocess.call(["ifconfig", interface, "up"])

    else:
        raise ValueError("You must specify a valid Mac Address.")

    # older version:
    # if pattern.match(MacAddress):
    #
    #     subprocess.call("ifconfig eth0 down", shell=True)
    #     subprocess.call(f"ifconfig eth0 hw ether {MacAddress}", shell=True)
    #     subprocess.call("ifconfig eth0 up", shell=True)
    #
    # else:
    #     print("Bad value")


def pars():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m","--mac", dest="new_mac", help="New Mac Address")
    return parser.parse_args()


(options, arguments) = pars()
interface = options.interface
macAddress = options.new_mac
mac_changer(interface, macAddress)

print(subprocess.check_output(["ifconfig", options.interface]))

# Using input()
# macAddress = input("input mac > ")
# interface = input("input interface > ")

# DEFAULT MAC 08:00:27:07:2e:d3"
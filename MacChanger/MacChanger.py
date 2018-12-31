#!/usr/bin/python3
import subprocess
import re

inp = input("input mac > ")
pattern = re.compile("^([0-9a-f]{2}[:-]){5}([0-9a-f]{2})$", re.IGNORECASE)
if pattern.match(inp):
    subprocess.call("ifconfig eth0 down", shell=True)
    subprocess.call(f"ifconfig eth0 hw ether {inp}", shell=True)
    subprocess.call("ifconfig eth0 up", shell=True)
else:
    print("Bad value")
# DEFAULT MAC 08:00:27:07:2e:d3"
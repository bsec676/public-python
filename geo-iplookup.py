#!/usr/bin/env python

from subprocess import *
from json import *

url = "https://json.geoiplookup.io/"
ip_address = input("IP Address = ")

process = Popen(['curl', 'https://json.geoiplookup.io/'+ ip_address])
stdout, stderr = process.communicate()
print(stdout)
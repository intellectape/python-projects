# Country Loop up
# Created by: Aditya Bhardwaj

import requests
import os
import json
import sys

if len(sys.argv) != 1:
    print("python whois.py")
    exit(1)

def countrylookup(): 
    
    r = requests.get('http://freegeoip.net/json')
    j = json.loads(r.text)
    ip = str(j['ip'])
    country = str(j['country_name'])
    print("The country for the given IP %s is: %s"%(ip,country))


if __name__ == "__main__":
    countrylookup()

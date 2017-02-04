# WHOIS project
# Created by: Aditya Bhardwaj

from subprocess import call
import sys

if len(sys.argv) != 2:
    print("python whois.py <IP Address> ")
    exit(1)


def findwhois(param): 
    return call(["whois", param])

if __name__ == "__main__":
    findwhois(sys.argv[1])
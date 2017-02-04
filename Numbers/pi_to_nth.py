"""
Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.
"""
# Using Ramanujam formula for finding the value of PI.

import sys
import math
from decimal import *

if len(sys.argv) != 2:
    print("python pi_to_nth.py <value of n> ")
    exit(1)

n = int(sys.argv[1])

def pi_to_nth(n):
    try:
        x = 0

        a =  Decimal((math.sqrt(8)/9801))
        for i in range(n):
            
            b = Decimal(math.factorial(4*n))
            c = Decimal(math.pow((math.factorial(n)) ,4))
            d = Decimal((26390 * n + 1103))
            e = Decimal(math.pow(396, 4 * n))

            x += ((b/c) *(d/e))

        pi = 1 / (a * x)
        print("The value of Pi is:" + str(pi))
    except OverflowError:
        pi = float('inf')
        print("The value of Pi is:" + str(pi))

def main():
    str(pi_to_nth(n))


if __name__ == "__main__":
    main()
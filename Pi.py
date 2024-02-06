#!/usr/bin/python
## Pi
# Takes an input and return all primes up to input
# Pi.py script
# Source Code produced by Willtech 2023
# v0.1 hand coded by HRjJ

#Pi.py calculates Pi to the number of decimal places set by mp.dps
import time
tt = time.time()

print("Initialise...")
## setup dependencies
#import sys
#import re

from mpmath import *
mp.dps = 100 #Configure DECIMAL
#@manual{mpmath,
#  key     = {mpmath},
#  author  = {The mpmath development team},
#  title   = {mpmath: a {P}ython library for arbitrary-precision floating-point arithmetic (version 1.3.0)},
#  note    = {{\tt http://mpmath.org/}},
#  year    = {2023},
#}
print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)
exit ("--- %s Seconds ---" % (mpf(time.time() - tt)))

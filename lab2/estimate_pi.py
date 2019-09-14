#!/usr/bin/env python

#   Author: Makenzie Brian
#   Date: January 23, 2018
#   File: lab2 > estimate_pi.py
#   Class: ME 599
#   Description: estimate pi from function

import math

def estimate_pi():
    estimate = 0
    k = 0
    recent = 1
    mult = 2 * math.sqrt(2) / 9801
    while(abs(recent) > 1e-15 ):
        n = (math.factorial(4*k)) * (1103 + 26390*k)    #numerator
        d = (math.factorial(k)**4) * (396**(4*k))       #denominator
        recent = mult * n / d
        estimate += recent                              #add to total
        k += 1                                          #track for factorial
    return 1/estimate


if __name__ == '__main__':
    piest = estimate_pi()
    print piest-math.pi                                 #compare
    print piest
    print math.pi
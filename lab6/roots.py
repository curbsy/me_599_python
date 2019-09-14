#!/usr/bin/env python

# Author: Makenzie Brian
# Date: February 20, 2018
# Class: ME 599
# File: lab6 > roots.py
# Description: class for roots for quadratic function

from complex import Complex
import math


def roots(a, b, c):
    check = (b**2) - (4 * a * c)
    if check > 0:                   # 2 real roots
        root1 = ((-b) + math.sqrt(check)) / (a * 2)
        root2 = ((-b) - math.sqrt(check)) / (a * 2)
        tup = (root1, root2)
        return tup

    elif check < 0:                 # 2 complex root
        root1 = Complex()
        root2 = Complex()

        root1.im = math.sqrt(abs(check)) / (a * 2)
        root2.im = -(math.sqrt(abs(check)) / (a * 2))

        root1.re = (-b) / (a * 2)
        root2.re = (-b) / (a * 2)

        tup = (root1, root2)
        return tup

    else:                           # 1 real root
        root1 = (-b) / (a * 2)
        tup = (root1,)
        return (tup)


# MAIN
if __name__ == '__main__':
    (x, y) = roots(1, 2, 3)
    print x, y

    x = roots(1, -10, 25)
    print x

    (x, y) = roots(1, 4, -8)
    print x, y
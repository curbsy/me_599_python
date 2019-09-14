#!/usr/bin/env python

#Author: Makenzie Brian
#Date: February 14, 2018
#Class: ME 599
#File: lab5 > testfile.py
#Description: test for classes


from complex import Complex
from shapes import Circle
from shapes import Rectangle

if __name__ == '__main__':
    a = Complex(1.0,'-2.3')
    b = Complex(2)
    c = Complex()
    d = Complex(1,-1)

    print a, b, c, d, '\n'

    c = Circle('21')
    a = c.area()
    d = c.diameter()
    p = c.perimeter()

    r = Rectangle('3',4)
    ar = r.area()
    pr = r.perimeter()

    print a, d, p
    print ar, pr
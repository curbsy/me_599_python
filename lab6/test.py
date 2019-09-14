#!/usr/bin/env python

# Author: Makenzie Brian
# Date: February 20, 2018
# Class: ME 599
# File: lab6 > test.py
# Description: test for complex class

from complex import Complex

# MAIN
if __name__ == '__main__':
    # convenience because I didn't want to use the built in
    a = Complex(6, 3)
    b = Complex(7, -5)
    numb = 3
    print "A: ", a
    print "B: ", b
    print "Add: ", a + b
    print "Subtract: ", a - b,
    print "Mult: ", a * b
    print "Divide: ", a / b
    print "Negate: ", -a, -b
    print "Compl conj: ", ~a, ~b
    print "\n"
    print "Integer second with interger as " + str(numb)
    print "Add: ", a + numb
    print "Subtract: ", a - numb
    print "Mult: ", a * numb
    print "Divide: ", a / numb
    print "\n"
    print "Integer first with interger as " + str(numb)
    print "Add: ", numb + a
    print "Subtract: ", numb - a
    print "Mult: ", numb * a
    print "Divide: ", numb / a
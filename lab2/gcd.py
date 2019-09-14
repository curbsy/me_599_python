#!/usr/bin/env python

#   Author: Makenzie Brian
#   Date: January 23, 2018
#   File: lab2 > gcd.py
#   Class: ME 599
#   Description: greatest common divisor function

def gcd(a,b):   #recursive
    if (type(a)== int and type(b) == int):
        if (b == 0):
            return a
        else:
            #do that remainder thanggggg because the book literally gave it to us thanks
            return gcd(b, a%b)



if __name__ == '__main__':
    x = -4
    y = 1
    g = gcd(x,y)
    print g
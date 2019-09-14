#!/usr/bin/env python

#Author: Makenzie Brian
#Date: February 14, 2018
#Class: ME 599
#File: lab5 > shapes.py
#Description: class for circle and rectangle

from numpy import pi

class Circle:
    def __init__(self, rad):
        if type(rad) == int or type(rad) == float:
            self.radius = rad
        else:
            try:       # if its a number in string format, convert to a string
                trad = float(rad)
                self.radius = trad
            except:
                print 'NO NO'
                raise TypeError


    def area(self):
        return (pi * (self.radius**2))

    def diameter(self):
        return (self.radius * 2)

    def perimeter(self):
        return (2 * pi * self.radius)


class Rectangle:
    def __init__(self, len, wid):
        if type(len) == int or type(len) == float:
            self.length = len
        else:
            try:       # if its a number in string format, convert to a string
                tlen = float(len)
                self.length = tlen
            except:
                print 'NO NO'
                raise TypeError

        if type(wid) == int or type(wid) == float:
            self.width = wid
        else:
            try:       # if its a number in string format, convert to a string
                twid = float(wid)
                self.width = twid
            except:
                print 'NO NO'
                raise TypeError

    def area(self):
        return (self.width * self.length)

    def perimeter(self):
        return (self.width *2) + (self.length * 2)


if __name__ == '__main__':
    c = Circle('21')
    a = c.area()
    d = c.diameter()
    p = c.perimeter()

    r = Rectangle('3',4)
    ar = r.area()
    pr = r.perimeter()

    print a, d, p
    print ar, pr
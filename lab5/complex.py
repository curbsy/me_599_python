#!/usr/bin/env python

#Author: Makenzie Brian
#Date: February 14, 2018
#Class: ME 599
#File: lab5 > complex.py
#Description: class for complex numbers

class Complex:
    def __init__(self, real = 0, imag = 0):    #default to 0 if missing
        if type(real) == int or type(real) == float:
            self.re = real
        else:
            try:       # if its a number in string format, convert to a string
                tre = float(real)
                self.re = tre
            except:
                print 'NO NO'
                raise TypeError

        if type(imag) == int or type(imag) == float:
            self.im = imag
        else:
            try:       # if its a number in string format, convert to a string
                tim = float(imag)
                self.im = tim
            except:
                print 'NO NO'
                raise TypeError


    def __str__(self):     #compile string for value printing
        val = ''
        val += '({0} '.format(self.re)
        if self.im >= 0:
            val += '+ '
        else:
            val += '- '
        val += '{0}i)'.format(abs(self.im))
        return val


if __name__ == '__main__':
    a = Complex(1.0,'-2.3')
    b = Complex(2)
    c = Complex()
    d = Complex(1,-1)

    print a, b, c, d
#!/usr/bin/env python

# Author: Makenzie Brian
# Date: February 20, 2018
# Class: ME 599
# File: lab6 > complex.py
# Description: class for complex numbers with add, sub, mult, div, neg, and conjugate


class Complex:
    def __init__(self, real=0, imag=0):    # default to 0 if missing
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

    def __str__(self):     # compile string for value printing
        val = ''
        val += '({0} '.format(self.re)
        if self.im >= 0:
            val += '+ '
        else:
            val += '- '
        val += '{0}i)'.format(abs(self.im))
        return val

    def __add__(self, other):
        c = Complex()
        try:
            c.im = self.im + other.im
            c.re = self.re + other.re
        except:
            c.re = self.re + other
            c.im = self.im
        return c

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -(self + (-other))

    def __neg__(self):
        c = Complex()
        c.re = -self.re
        c.im = -self.im
        return c

    def __mul__(self, other):
        c = Complex()
        try:
            c.re = -(self.im * other.im) + (self.re * other.re)
            c.im = (self.im * other.re) + (self.re * other.im)
        except:
            c.re = (self.re * other)
            c.im = (self.im * other)
        return c

    def __rmul__(self, other):
        return self*other

    def __div__(self, other):
        c = Complex()
        try:
            conj = ~other       # complex conjugate
            denominator = other * conj
            numerator = self * conj
            c.re = float(numerator.re)/float(denominator.re)
            c.im = float(numerator.im)/float(denominator.re)
        except:
            c.re = float(self.re)/float(other)
            c.im = float(self.im)/float(other)
        return c

    def __rdiv__(self, other):
        c = Complex()
        conj = ~self            # complex conjugate
        denominator = self * conj
        numerator = other * conj
        c.re = float(numerator.re) / float(denominator.re)
        c.im = float(numerator.im) / float(denominator.re)
        return c

    def __invert__(self):       # complex conjugate
        return Complex(self.re, -self.im)

# MAIN
if __name__ == '__main__':
    a = Complex(6, 3)
    b = Complex(7, -5)
    print a/b, a/2, 2/a

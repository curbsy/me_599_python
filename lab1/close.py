#!/usr/bin/env python

#   Author: Makenzie Brian
#   File: Lab1 > close
#   Date: January 15, 2018
#   Class: ME599
#   Description: true of abs diff of first 2 vals is less than third val

def close(num1, num2, num3):
    if (abs(num1-num2) < num3):
        return True
    else:
        return False

if __name__ == '__main__':
    var1 = -1
    var2 = -2
    var3 = 4

    print close(var1, var2, var3)
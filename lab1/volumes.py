#!/usr/bin/env python

#   Author: Makenzie Brian
#   File: Lab1 > volumes
#   Date: January 15, 2018
#   Class: ME599
#   Description: Functions for torus and cylinder volumes


import math

#function definitions
def cylinder_volume(r, h):
    if (r<0) or (h<0):
        return None
    else:
        v = (math.pi)*(r**2)*h
        return v

def torus_volume(majr, minr):
    if (majr<0) or (minr<0) or (minr>=majr):    #deals with equal or smaller radius
        return None
    else:
        v = (math.pi**2)*(minr**2)*2*majr
        return v

#MAIN
if __name__ == '__main__':
    #change variables here
    rad = 3
    height = 4
    cylv = cylinder_volume(rad, height)

    majorr = 7
    minorr = 3
    torv = torus_volume(majorr, minorr)

    print "Cylinder volume: " + str(cylv) + "\nTorus volume: " + str(torv)

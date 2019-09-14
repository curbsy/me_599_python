#!/usr/bin/env python

#   Author: Makenzie Brian
#   Date: January 23, 2018
#   File: lab2 > filters.py
#   Class: ME 599
#   Description: mean, median filters for lists

import numpy
import copy
from null_filter import *

#fixed width mean filter
def mean_filter_simple(old):
    new = copy.copy(old)                 #new list to not change old one
    for x in range(len(old)):
        if (x>0 and x<(len(old)-1)):    #ignore ends
            new[x-1] = float((old[x] + old[x-1] + old[x+1])/3)  #avg
    return new

#variable width mean filter
def mean_filter(old, number):
    new = []
    if(number%2 == 1 and number<len(old) and number>0):      #is odd and positive
        for x in range(len(old)):
            refval = int(number/2)                           #halfish of divisor because useful
            if (x>refval and x<(len(old)-refval-1)):         #end values are cut out after averaging
                lst = old[(x - refval-1):(x + refval)]       #values to be averaged
                #print lst
                new.append((numpy.mean(lst)))
                #print (numpy.mean(lst))

        return new
    else:
        print "Bad value"
        return "Bad value"          #you can't just do none because of the way its printed in other function

#variable width median filter
def median_filter(old, number):
    new = []
    if(number%2 == 1 and number<len(old) and number>0):     #is odd and positive
        for x in range(len(old)):
            refval = int(number/2)                          #halfish of divisor
            if (x>refval and x<(len(old)-refval-1)):        #end values are cut out after averaging
                lst = old[(x - refval-1):(x + refval)]      #values to be averaged
                #print lst
                new.append((numpy.median(lst)))
                #print numpy.median(lst)

        return new
    else:
        print "Bad value"
        return "Bad value"          #you can't just do none because of the way its printed in other function

#MAIN
if __name__ == '__main__':
    data = generate_sensor_data()

    filtered_data = median_filter(data, 3)

    print_sensor_data(data, 'raw')
    print_sensor_data(filtered_data, 'filtered')
#!/usr/bin/env python

#   Author: Makenzie Brian
#   Date: January 23, 2018
#   File: lab2 > reverse.py
#   Class: ME 599
#   Description: reverse list

import copy

#iterative reverse
def reverse_i(list):
    newlist = list[:]
    for i in range(len(list)):
        newlist[len(list)-i-1] = list[i]
    return newlist

#recursive reverse
def reverse_r(list):
    newlist = copy.copy(list)
    if len(newlist) == 0:
        return []
    else:
        return reverse_r(newlist[1:]) + [newlist[0]]  #newlist[len(list)-1] + reverse_r(list[1:])

#MAIN
if __name__ == '__main__':
    l = [1, 2, 3, 4]
    ri = reverse_i(l)
    print ri
    rr = reverse_r(l)
    print rr
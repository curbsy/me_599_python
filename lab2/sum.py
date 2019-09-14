#!/usr/bin/env python

#   Author: Makenzie Brian
#   Date: January 23, 2018
#   File: lab2 > sum.py
#   Class: ME 599
#   Description: sum a list

#iterative sum
def sum_i(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum

#recursive sum
def sum_r(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_r(list[1:])     #sum_r(list[1,len(list)-1])

#MAIN
if __name__ == '__main__':
    l = [1,2,3]
    si = sum_i(l)
    print si
    sr = sum_r(l)
    print sr


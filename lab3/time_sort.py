#!/usr/bin/env python

#Author: Makenzie Brian
#Date: January 30 2017
#File: lab3 > time_sort.py
#Class: ME 599
#Description: time and plot the time it takes to sort lists with builtin sort

import time
import random
import matplotlib.pyplot as plt

def get_times():
    timesort = []
    timesum = []
    for x in (1,10, 100, 1000, 10000, 100000, 1000000):
        lst = [random.randint(0,1000) for i in xrange(x)]
        start1 = time.time()
        sorted(lst)
        timesort.append(time.time() - start1)

        start2 = time.time()
        sum(lst)
        timesum.append(time.time() - start2)

    return timesort, timesum

def plot_times():
    timesort, timesum = get_times()

    plt.figure(1)
    plt.subplot(311)
    plt.plot((1,10, 100, 1000, 10000, 100000, 1000000), timesort)
    plt.ylabel('Execution Time')
    plt.title('Execution Time for sort() Algorithm Execution is linear')

    plt.subplot(313)
    plt.plot((1,10, 100, 1000, 10000, 100000, 1000000), timesum)
    #plt.xlabel('Number of Elements in List')
    plt.ylabel('Execution Time')
    plt.xlabel('Number of Elements in List')
    plt.title('Execution Time for sum() Algorithm Execution is not linear')
    plt.show()
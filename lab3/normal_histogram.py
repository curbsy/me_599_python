#!/usr/bin/env python

#Author: Makenzie Brian
#Date: January 30 2017
#File: lab3 > normal_histogram.py
#Class: ME 599
#Description: gives normal histogram

import matplotlib.pyplot as plt
#import numpy as np
import random

def samples():
    #s = sum(np.random.uniform(0, 1, 10))
    s = sum([random.random() for x in xrange(1,10)])
    return s

def histogram_graph():
    set = []
    for i in xrange(1000):
        set.append(samples())

    plt.hist(set)
    plt.xlabel('Sum Values')
    plt.ylabel('Amount of that Sum')
    plt.title('Random Sum Samples from a Uniform Distribution')
    plt.xlim(0,10)
    #plt.ylim(-1.01, 1.01)
    plt.show()


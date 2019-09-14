#!/usr/bin/env python

#Author: Makenzie Brian
#Date: January 30 2017
#File: lab3 > sin_plot.py
#Class: ME 599
#Description: plots sin function to 4 pi


import matplotlib.pyplot as plt
import numpy as np


def sin_plot():
    x = np.arange(0.0, (4*np.pi), 0.02)

    plt.plot(x, np.sin(x))
    plt.xlabel('X')
    plt.ylabel('Sin(X)')
    plt.title('A Sine Curve')
    plt.xlim(0,(4*np.pi))
    plt.ylim(-1.01,1.01)
    plt.show()
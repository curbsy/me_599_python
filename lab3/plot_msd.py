#!/usr/bin/env python

#Author: Makenzie Brian
#Date: January 30 2017
#File: lab3 > plot_msd.py
#Class: ME 599
#Description: plots mass spring damper system displacement

import matplotlib.pyplot as plt
from msd import *

#POSITION VS DISPLACEMENT????

def plot_msd():
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
    state, t = smd.simulate(0.0, 1.0)

    disp = []
    for s,v in state:
        disp.append(s)

    plt.plot(t, disp)
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.title('Mass Spring Damper System Displacement Over Time')
    #plt.xlim(0,)
    #plt.ylim(-1.01,1.01)
    plt.show()



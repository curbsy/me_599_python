#!/usr/bin/env python

# Author: Makenzie Brian
# Date: March 6, 2018
# Class: ME 599
# File: lab8 > optimize.py
# Description: optimizations for finding max value of function


from math import sin
from math import pi
import random
import matplotlib.pyplot as plt
from scipy import optimize
import itertools


def optimize_step(func, (low, high), num):
    try:
        # order of bounds does not matter names are just helpful
        delta = float(high - low)/float(num)        # change in x for each step
        xcurrent = low
        ymax = func(low)                            # give starting max val
        xmax = low                                  # this is the x of the max not the maximum of x

        for i in xrange(num):
            xcurrent += delta
            if func(xcurrent) > ymax:
                ymax = func(xcurrent)
                xmax = xcurrent

        return xmax

    except:
        raise TypeError


def optimize_random(func, (low, high), num):
    try:
        xcurrent = ((high - low) * random.random()) + low   # starting sample
        ymax = func(xcurrent)                               # give starting max val
        xmax = xcurrent                                     # this is the x of the max not the maximum of x

        for i in xrange(num - 1):
            xcurrent = ((high - low) * random.random()) + low
            if func(xcurrent) > ymax:
                ymax = func(xcurrent)
                xmax = xcurrent

        return xmax

    except:
        raise TypeError


# How well does this need to work??? because the step will matter...
def optimize_gradient(func, (low, high), ep):
    try:
        delta = float(high - low) / 10                       # change in x for each check, probably should change this??
        xmax = ((high - low) * random.random()) + low       # this is the x of the max not the maximum of x
        ymax = func(xmax)                                   # give starting max val
        #numsteps = 0
        #count = 4
        xup = xmax + delta
        xdown = xmax - delta
        while ((func(xup) - ymax) > ep or (func(xdown) - ymax) > ep) or delta > float(high - low) / 2000.0:
            # xup = xmax + delta                              # "up" a step
            # xdown = xmax - delta                            # "down" a step
            # print xup, xdown
            # count += 1
            if delta > float(high - low) / 5000.0:
                #delta = float(high - low) / count
                delta = delta / 1.2

            if (func(xup) - ymax) > ep:
                #print (func(xup) - ymax)
                ymax = func(xup)
                xmax = xup
                #numsteps += 1
            elif (func(xdown) - ymax) > ep:
                #print (func(xdown) - ymax)
                ymax = func(xdown)
                xmax = xdown
                #numsteps += 1
            xup = xmax + delta                              # "up" a step
            xdown = xmax - delta                            # "down" a step
            #print xup, xdown
        #print (func(xdown) - ymax)
        #print (func(xup) - ymax)
        return xmax#, numsteps

    except:
        raise TypeError


def optimize_gradient_for_plot(func, (low, high), ep):
    try:
        delta = float(high - low) / 10  # change in x for each check, probably should change this??
        xmax = ((high - low) * random.random()) + low  # this is the x of the max not the maximum of x
        ymax = func(xmax)  # give starting max val
        numsteps = 0
        # count = 4
        xup = xmax + delta
        xdown = xmax - delta
        while (func(xup) - ymax) > ep or (func(xdown) - ymax) > ep or delta > float(high - low) / 2000.0:
            # xup = xmax + delta                              # "up" a step
            # xdown = xmax - delta                            # "down" a step
            # print xup, xdown
            # count += 1
            if delta > float(high - low) / 5000.0:
                # delta = float(high - low) / count
                delta = delta / 1.2

            if (func(xup) - ymax) > ep:
                ymax = func(xup)
                xmax = xup
                numsteps += 1
            elif (func(xdown) - ymax) > ep:
                ymax = func(xdown)
                xmax = xdown
                numsteps += 1

            xup = xmax + delta  # "up" a step
            xdown = xmax - delta  # "down" a step
        #print xmax
        return xmax, numsteps

    except:
        raise TypeError


# Did graph of absolute error because just says accuracy
def plot_optimizations(func, (bound1, bound2), numevals, realval):
    errorstep = []
    errorrandom = []
    errorgradientx = []
    errorgradienty = []
    scipyopt = optimize.minimize_scalar(lambda x: -func(x), None).x
    for i in xrange(1, numevals):
        errorstep.append(abs(realval - optimize_step(func, (bound1, bound2), i)))
        errorrandom.append(abs(realval - optimize_random(func, (bound1, bound2), i)))
        mx, stps = optimize_gradient_for_plot(func, (bound1, bound2), .00001)
        if stps not in errorgradientx:
            errorgradienty.append(abs(realval - mx))
            errorgradientx.append(stps)

    lists = sorted(itertools.izip(*[errorgradientx, errorgradienty]))
    newx, newy = list(itertools.izip(*lists))
    plt.plot(xrange(1, numevals), errorrandom, errorstep)
    plt.axhline(y=(realval-scipyopt), color='r')
    plt.plot(newx, newy)
    plt.xlabel('Number of Evaluations')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error of Optimizations for Finding the Maximum of a Function (Sin)')
    plt.legend(['Random Optimization', 'Step Optimization', 'Scipy Error', 'Gradient Ascent Optimization'], loc='upper right')
    plt.xlim(-10, numevals+10)
    plt.show()


def optimize_md(func, bounds):
    # doing random sampling because it seems easiest with an undefined number of dimensions
    try:
        for j in xrange(500000):
            values = []
            for i in xrange(len(bounds)):
                values.append(random.uniform(bounds[i][0], bounds[i][1]))
            testval = func(*values)
            try:
                if testval > maxval:
                    maxval = testval
            except:                         # fill on first round through
                maxval = testval


        return maxval

    except:
        raise TypeError


def ughfunction(x, y, z):
    return sin(x) * sin(y)


# MAIN
if __name__ == '__main__':
    #x = optimize_step(sin, (0, pi), 1000)
    #y = optimize_random(sin, (0, pi), 10000)
    #z = optimize_gradient(sin, (0, pi), .000001)
    #print x,y, z

    plot_optimizations(sin, (0, pi), 500, pi/2)

    #w = optimize_md(ughfunction, [(0, pi), (0, pi), (0, pi)])
    #print w

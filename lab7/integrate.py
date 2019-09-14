#!/usr/bin/env python

# Author: Makenzie Brian
# Date: February 27, 2018
# Class: ME 599
# File: lab7 > integrate.py
# Description: Calculates integrals for riemann sum and monte carlo methods; plots errors from both


from math import sin
from math import pi
from math import fabs
from math import sqrt
import random
import matplotlib.pyplot as plt


# I literally just made an equation into a script so sorry if it probably looks similar to other ones but that's what
# happens when you give us easy stuff like this
def integrate(func, st, end, intervals=1000000.0):
    # works if end and start are flipped but gives negative sum b/c that's what math told me to have anyway
    try:
        dx = float(end-st)/float(intervals)        # calculate dx for each strip because yeah

        numstrips = int(fabs(end-st)/dx)           # calculates int for number of strips b/c without bad things happened

        area = 0
        currentx = st                              # init x to start
        for n in xrange(numstrips):
            da = func(currentx) * dx               # area of strip
            area += da                             # add to total area
            currentx += dx                         # move to next strip and repeat

        return area

    except:
        raise TypeError                             # you gave it something that was not a number, function, etc.


def integrate_mc(func, st, end, (ylow, yhigh), samples=1000000.0):
    try:
        if yhigh < ylow:                                    # bad bounds: throws error, doesn't swap
            raise ValueError

        rectarea = float(abs((yhigh - ylow) * (end - st)))  # total rea
        count = 0

        for m in xrange(int(samples)):
            currentx = ((end - st) * random.random()) + st  # get random (ish) values within the rectangle
            currenty = ((yhigh - ylow) * random.random()) + ylow
            if fabs(currenty) <= fabs(func(currentx)):      # check if under function to add or subtract for count
                if currenty > 0 and func(currentx) > 0:     # positive area: add to count
                    count += 1

                if currenty < 0 and func(currentx) < 0:     # negative area: subtract from count
                    count -= 1

        return (rectarea * float(count)) / float(samples)   # calc probabilistic area thing from count b/c we want that

    except:
        if yhigh < ylow:                                    # bad bounds: throws error, doesn't swap
            raise ValueError
        else:
            raise TypeError                                 # you gave it something that was not a number, function, etc


# Made it adaptable to other functions if you want to use it that way
def plot_approx_error(functionf, starts, ends, (bound1, bound2), numintsamps, realanswer):
    errorvalues = []
    errormcvalues = []

    for i in xrange(1, numintsamps):            # calc error values for each trial
        errorvalues.append(abs(realanswer - integrate(functionf, starts, ends, i)))
        errormcvalues.append(abs(realanswer - integrate_mc(functionf, starts, ends, (bound1, bound2), i)))

    plt.plot(xrange(1, numintsamps), errorvalues, errormcvalues)
    plt.xlabel('Number of Intervals/Samples')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error of Integration with Riemann Sum and Monte Carlo Methods')
    plt.legend(['Riemann Sum', 'Monte Carlo'], loc='upper right')
    plt.show()


def approximate_pi(samples):
    rectarea = 4
    # using circle centered around 0
    # find radius of each point
    try:
        count = 0
        for m in xrange(int(samples)):
            currentx = (2 * random.random()) - 1           # get random (ish) values within the square
            currenty = (2 * random.random()) - 1
            currentrad = sqrt((currentx ** 2) + (currenty ** 2))  # find radius of each point
            if fabs(currentrad) <= 1:                      # if it is within circle add to count
                count += 1

        return (rectarea * float(count)) / float(samples)  # calc probabilistic area thing from count

    except:
        raise TypeError                                    # you gave it something that was not a number, function, etc.


# MAIN
if __name__ == '__main__':
    f = integrate(sin, 0, pi)
    u = integrate_mc(sin, 0, pi, (0, 1))
    print "Riemann Sum Method:", f, "\nMonte Carlo Method:", u
    print "Please give me a few seconds to produce graphs. I'm working I swear."
    plot_approx_error(sin, 0, pi, (0, 1), 3000, 2)   #bigger than 1000 takes a while on little laptapo

    p = approximate_pi(3000000)
    print "Pi is approximately:", p

#!/usr/bin/env python

# Author: Makenzie Brian
# Date: March 7, 2018
# Class: ME 599
# File: hw2 > simulator.py
# Description: Deals with simulator stuff for given file; almost no optimization

# NOTES for grading TA: I wrote more than one function in my class because I wanted it to be modular and it makes more
# sense. Also the lower cost path is currently just random not optimized so you will get a different results each time.


import subprocess
from random import randint


class Simulator:
    def __init__(self, test_number):
        self.test_number = test_number

    def evaluate(self, wayp):
        # write given waypoints to file
        self.waypoints_to_file(wayp)

        # call simulation (with given simulation test number)
        return self.get_sim_output()

    def waypoints_to_file(self, w):
        # write given waypoints to file
        with open("waypoints", "w") as f:
            for (x, y) in w:
                f.write(str(x)+" "+str(y)+"\n")     # concatenate string for file in correct format

    def get_sim_output(self):
        # call simulation (with given simulation test number)
        sim_output = subprocess.check_output(["simulator", "waypoints", str(self.test_number)])
        output_value = sim_output.split()[9]        # take actual output value
        return float(output_value[:-1])                   # get rid of period at end


def find_better_waypoints(path, r, sim):
    # add a new random point in the middle until its better than before
    path.insert(1, (randint(-10, 10), randint(-10, 10)))
    # print path
    sim.waypoints_to_file(path)
    new_r = sim.get_sim_output()

    while new_r > r:
        path[1] = (randint(-10,10), randint(-10,10))
        # print path
        sim.waypoints_to_file(path)
        new_r = sim.get_sim_output()
        # print new_r

    # write new better waypoints to better_waypoints file
    better_waypoints_to_file(path)

    return new_r


def better_waypoints_to_file(w):
    # write better waypoints to file
    with open("better_waypoints", "w") as f:
        for (x, y) in w:
            f.write(str(x)+" "+str(y)+"\n")     # concatenate string for file in correct format


# MAIN
if __name__ == '__main__':
    number = raw_input("Enter a simulation number: ")
    w = [(-10, -10), (10, 10)]
    s = Simulator(number)
    result = s.evaluate(w)
    print "Initial Result: " + str(result)

    # for each waypoint, check new values for better outcome
    new_result = find_better_waypoints(w, result, s)
    print "Better Result: " + str(new_result)
    print "See file 'better_waypoints' for path"

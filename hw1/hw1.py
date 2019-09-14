#!/usr/bin/env python

# Author: Makenzie Brian
# Date: February 7, 2018
# Class: ME 599
# File: hw1 > hw1.py
# Description: takes in csv (grades) and gives stats and stuff on them

# file format: the words student number, assignments name list
#              student number, assignment scores, etc.

import numpy
import math


# PART 2
# read file into array
def readfile(file):
    # make arrays for: final scores, assignment scores, lab scores
    with open(file, 'r') as f1:
        grades = []
        for line in f1:   # list of lists on purpose because each sublist is a student
            try:          # try to convert to floats for calculations because its easier
                grades.append([float(x) for x in line.strip().split(',')])
            except:       # get rid of the stupid things that say EX, convert more things to floats
                new = line.strip().split(',')
                for i in xrange(len(new)):
                    if new[i] == 'EX':
                        new[i] = numpy.nan
                    else:
                        try:
                            new[i] = float(new[i])
                        except:
                            pass
                grades.append(new)
    return grades


# calc average final score in class given array of final scores
def averagescore(grds):
    # average final score which is last element in each row
    total = 0
    count = 0

    for student in xrange(1,len(grds)):    # for each student list but not list of titles
        try:
            total += grds[student][len(grds[student])-1]    # add total
            count += 1                                      # count students
        except:
            pass

    return total/count


# calc percentage of students who are above average given array of final scores
def aboveaverage(grds, avg):
    count = 0
    totalcount = 0
    for student in xrange(1,len(grds)):    # for each student list but not list of titles
        try:
            if grds[student][len(grds[student])-1] > avg:   # check placement
                count += 1                                  # count number above average
        except:
            pass
        totalcount += 1

    return (float(count)/float(totalcount)) * 100.0


# calc median final score in class given array of final scores
def medianscore(grds):
    scores = []
    for student in xrange(1,len(grds)):    # for each student list but not list of titles
        if type(grds[student][len(grds[student])-1]) == float:      # if float because there were issues
            scores.append(grds[student][len(grds[student])-1])      # add to array for calc of median

    return numpy.median(scores)


# calc percentage of students above median given array of final scores
def abovemedian(grds, med):
    count = 0
    totalcount = 0
    for student in xrange(1,len(grds)):    # for each student list but not list of titles
        try:
            if grds[student][len(grds[student])-1] > med:           # check placement
                count += 1                                          # if above median, add to count
            totalcount += 1
        except:
            pass

    return (float(count)/float(totalcount)) * 100.0


# PART 3
# find hardest assignment (lowest average score)
def hardestassignment(grds):
    ngrds = grds[1:]            # take out first row because just names of stuff
    # calc average scores of all assignments (by column)
    averages = numpy.nanmean(ngrds, axis=0)

    # can assume someone actually gets highest possible score so find max (by column)
    maxes = numpy.nanmax(ngrds, axis=0)

    # weigh averages based on max score to find true lowest percentage
    # WILL throw a RUNTIME WARNING if average is so close to zero that it rounds down, but still works
    percentages = [averages/maxes for averages, maxes in zip(averages, maxes)]

    return grds[0][(percentages.index(min(i for i in percentages if i > 0)))], percentages


# PART 4
# find hardest lab (lowest average score)
def hardestlab(grades, percentages):
    # use previously calculated percentages
    notlabs = []
    for assname in xrange(len(grades[0])):
        if 'Lab' not in grades[0][assname]:       # Lab seems to always be caps so I didn't want to change it
            notlabs.append(assname)

    # remove scores that are not for labs
    for i in notlabs:
        percentages[i] = numpy.nan

    return grades[0][(percentages.index(min(i for i in percentages if i > 0)))]


# PART 5
# with normal grading scheme (A,A-,B+,B,...), how many students for each grade
def gradenormally(grds):
    scores = {'As':0, 'Ams':0, 'Bps':0, 'Bs':0, 'Bms':0, 'Cps':0, 'Cs':0, 'Cms':0, 'Dps':0, 'Ds':0, 'Dms':0, 'Fs':0}
    complainers = 0     # look at grades, find close to next percentile
    # look at final score and count in dictionary
    for student in xrange(1,len(grds)):    # for each student list but not list of titles
        try:
            score = grds[student][len(grds[student])-1]
            if score >= 94:           # A
                scores['As'] += 1
            elif 94 > score >= 90:    # A-
                scores['Ams'] += 1
                if 0 > (score-94) > -.5:
                    complainers += 1
            elif 90 > score >= 87:    # B+
                scores['Bps'] += 1
                if 0 > (score-90) > -.5:
                    complainers += 1
            elif 87 > score >= 84:    # B
                scores['Bs'] += 1
                if 0 > (score-87) > -.5:
                    complainers += 1
            elif 84 > score >= 80:    # B-
                scores['Bms'] += 1
                if 0 > (score-84) > -.5:
                    complainers += 1
            elif 80 > score >= 77:    # C+
                scores['Cps'] += 1
                if 0 > (score-80) > -.5:
                    complainers += 1
            elif 77 > score >= 74:    # C
                scores['Cs'] += 1
                if 0 > (score-77) > -.5:
                    complainers += 1
            elif 74 > score >= 70:    # C-
                scores['Cms'] += 1
                if 0 > (score-74) > -.5:
                    complainers += 1
            elif 70 > score >= 67:    # D+
                scores['Dps'] += 1
                if 0 > (score-70) > -.5:
                    complainers += 1
            elif 67 > score >= 64:    # D
                scores['Ds'] += 1
                if 0 > (score-67) > -.5:
                    complainers += 1
            elif 64 > score >= 61:    # D-
                scores['Dms'] += 1
                if 0 > (score-64) > -.5:
                    complainers += 1
            elif 61 > score:          # F
                scores['Fs'] += 1
                if 0 > (score-61) > -.5:
                    complainers += 1
        except:
            pass

    # print in here because don't want to pass it all back
    print 'A  ' + str(scores['As']) + '\nA- '+str(scores['Ams'])
    print 'B+ ' + str(scores['Bps']) + '\nB  ' + str(scores['Bs']) + '\nB- ' + str(scores['Bms'])
    print 'C+ ' + str(scores['Cps']) + '\nC  ' + str(scores['Cs']) + '\nC- ' + str(scores['Cms'])
    print 'D+ ' + str(scores['Dps']) + '\nD  ' + str(scores['Ds']) + '\nD- ' + str(scores['Dms'])
    print 'F  ' + str(scores['Fs'])
    return complainers


# PART 6
# number of students who are within 0.5% of a higher grade
def ughcomplainers(comp):
    # passed from previous grade check because easier hahaha
    print str(comp)+' students will complain about their grade.'


# PART 7
# no +/- grading scheme (A,B,C,D,F), how many students for each grade
def gradedifferently(grds):
    # look at final scores separate
    scores = []
    for student in xrange(1, len(grds)):    # for each student list but not list of titles
        try:
            scores.append(grds[student][len(grds[student])-1])  # add final score to array
        except:
            pass

    sortscores = sorted(scores, reverse=1)     # sort in descending order

    # number of students in each grade category
    astudents = [i for i in range(int(math.floor((len(grds) - 1)/10)))]
    bstudents = [i for i in range(int(math.floor((2*((len(grds) - 1)/10)))))]
    cstudents = [i for i in range(int(math.floor((3*((len(grds) - 1)/10)))))]
    dstudents = [i for i in range(int(math.floor((3*((len(grds) - 1)/10)))))]

    # look at highest section (A student section, etc.), find min, remove used values, repeat
    acuttoff = min([sortscores[i] for i in astudents])
    sortscores = sortscores[len(astudents):]

    bcuttoff = min([sortscores[i] for i in bstudents])
    sortscores = sortscores[len(bstudents):]

    ccuttoff = min([sortscores[i] for i in cstudents])
    sortscores = sortscores[len(cstudents):]

    dcuttoff = min([sortscores[i] for i in dstudents])
    # sortscores = sortscores[len(dstudents):]
    # what's left will be the F scores

    print 'A ' + str(acuttoff)
    print 'B ' + str(bcuttoff)
    print 'C ' + str(ccuttoff)
    print 'D ' + str(dcuttoff)


# functions to call other functions because I don't want to type everything out EVERY FREAKING TIME
# PRINT EVERYTHING
def classstats(file):
    grades = readfile(file)
    avg = averagescore(grades)
    abvavg = aboveaverage(grades, avg)
    med = medianscore(grades)
    abvmed = abovemedian(grades, med)
    print "Average Score: "+str(round(avg,2))+"\nAbove Average: "+str(round(abvavg,2))+"%"
    print "\nMedian Score: "+str(round(med,2))+"\nAbove Median: "+str(format(abvmed,'.2f'))+"%"

    ha, perc = hardestassignment(grades)
    print "Hardest Assignment: "+str(ha)

    hl = hardestlab(grades, perc)
    print "Hardest Lab: "+str(hl)

    complainers = gradenormally(grades)

    ughcomplainers(complainers)

    gradedifferently(grades)


# MAIN
if __name__ == '__main__':
    classstats('grades.csv')


#!/usr/bin/env python

#Author: Makenzie Brian
#Date: February 5 2017
#File: lab4 > compare.py
#Class: ME 599
#Description: does file comparison stuff with words, uses sets

#NOTE: some of this code is similar to what we did in class because it was useful to use here

import sys
import string

#PART1: checks for 2 arguments and prints commandline input
def print_from_commandline():
    if len(sys.argv) is 3:
        print sys.argv[1]
        print sys.argv[2]
    elif len(sys.argv) > 3:
        print "Too many arguments"
    elif len(sys.argv) < 3:
        print "Too few arguments"

#PART2: given file names in commandline, returns number of words in each
def num_words_in_files():
    if len(sys.argv) is 3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    elif len(sys.argv) > 3:
        print "Too many arguments"
        return None
    elif len(sys.argv) < 3:
        print "Too few arguments"
        return None

    with open (file1, 'r') as f1:
        wordsf1 = []
        wordsf2 = []
        for line in f1:
            wordsf1.extend(line.strip().split()) #strip \n and split into words to put in array

    with open (file2, 'r') as f2:
        for line in f2:
            wordsf2.extend(line.strip().split()) #strip \n and split into words to put in array
        #print "The number of words in", file1, ":", len(wordsf1), "\nThe number of words in", file2, ":", len(wordsf2)
        #WHY DOES MY PRINT FORMAT HAVE TO MATCH MINE LOOKS SO MUCH NICER UGH
        print str(file1)+": \n  "+str(len(wordsf1))+ " words\n" +str(file2)+ ": \n  " +str(len(wordsf2)) +" words"


#PART3: find unique words in each file, not case sensitive, no punctuation
def num_unique_words_in_files():
    if len(sys.argv) is 3:
        file1 = sys.argv[1]     #assign commandline args as filenames
        file2 = sys.argv[2]
    elif len(sys.argv) > 3:
        print "Too many arguments"
        return None
    elif len(sys.argv) < 3:
        print "Too few arguments"
        return None

    transtab = string.maketrans('-', ' ') #replace for hypenated words??
    badchars = (".:?/-=()[],;*!_")   #chars to take out; cannot seem to take out ' or " ?????

    #make arrays and sets
    with open(file1, 'r') as f1:
        wordsf1 = []
        setwordsf1 = set()

        for line in f1:
            wordsf1.extend(line.strip().split())  #strip \n and split into words to put in array
            setwordsf1.update([x.lower() for x in line.strip().translate(transtab, badchars).split()])  # strip \n and split into words to put in set with only lowers and no punctuation

    with open(file2, 'r') as f2:
        wordsf2 = []
        setwordsf2 = set()

        for line in f2:
            wordsf2.extend(line.strip().split())  #strip \n and split into words to put in array
            setwordsf2.update([x.lower() for x in line.strip().translate(transtab, badchars).split()])  # strip \n and split into words to put in set with only lowers and no punctuation

    #printing finally yay
    #print "The number of words in", file1, ":", len(wordsf1), "\nThe number of words in", file2, ":", len(wordsf2)
    #print "The number of unique words in", file1, ":", len(setwordsf1), "\nThe number of unique words in", file2, ":", len(setwordsf2)
    print str(file1) + ": \n  " + str(len(wordsf1)) + " words" + "\n  unique: "+str(len(setwordsf1))
    print str(file2) + ": \n  " + str(len(wordsf2)) + " words" + "\n  unique: "+str(len(setwordsf2))


#PART4: (includes previous parts)
def compare_files():
    if len(sys.argv) is 3:
        file1 = sys.argv[1]     #assign commandline args as filenames
        file2 = sys.argv[2]
    elif len(sys.argv) > 3:
        print "Too many arguments"
        return None
    elif len(sys.argv) < 3:
        print "Too few arguments"
        return None

    #transtab = string.maketrans('-', ' ') #replace for hypenated words BECAUSE THIS WOULD BE REALISTIC BUT WHATEVERRRRR
    badchars = (".:_?/-=()[],;*!\"'$#&%+<>@^`~{}|\\")   #chars to take out; cannot seem to take out ' or " ?????

    #make arrays and sets
    with open(file1, 'r') as f1:
        wordsf1 = []
        setwordsf1 = set()

        for line in f1:
            wordsf1.extend(line.strip().split())  #strip \n and split into words to put in array INCLUDES PUNCTUATION
            setwordsf1.update([x.lower() for x in line.strip().translate(None, badchars).split()])  # strip \n and split into words to put in set with only lowers and no punctuation

    with open(file2, 'r') as f2:
        wordsf2 = []
        setwordsf2 = set()

        for line in f2:
            wordsf2.extend(line.strip().split())  #strip \n and split into words to put in array INCLUDES PUNCTUATION
            setwordsf2.update([x.lower() for x in line.strip().translate(None, badchars).split()])  # strip \n and split into words to put in set with only lowers and no punctuation

    #find differences
    f1only = setwordsf1.difference(setwordsf2)
    f2only = setwordsf2.difference(setwordsf1)
    intersetion = setwordsf1.intersection(setwordsf2)                              #get it like intersection but no c hahahahaha


    #printing finally yay
    #print "The number of words in", file1, ":", len(wordsf1), "\nThe number of words in", file2, ":", len(wordsf2)
    #print "The number of unique words in", file1, ":", len(setwordsf1), "\nThe number of unique words in", file2, ":", len(setwordsf2)
    #print "The number of unique words only in", file1, ":", len(f1only), "\nThe number of unique words only in", file2, ":", len(f2only)
    #print "The number of shared words:", len(intersetion)
    print str(file1) + ": \n  " + str(len(wordsf1)) + " words" + "\n  unique: "+str(len(setwordsf1))
    print str(file2) + ": \n  " + str(len(wordsf2)) + " words" + "\n  unique: "+str(len(setwordsf2))
    print "Only "+ str(file1)+": "+str(len(f1only)) +"\nOnly "+ str(file2)+": "+str(len(f2only))
    print "Both files: "+ str(len(intersetion))





#MAIN
if __name__ == '__main__':
    #print_from_commandline()       #PART1
    #num_words_in_files()           #PART2
    #num_unique_words_in_files()    #PART3
    compare_files()                #PART4

    #simple example of how translate works for me
    #transtab = string.maketrans('-', ' ')
    #badchars = (".',")
    #print "A,B.C'E-de".translate(transtab, badchars)

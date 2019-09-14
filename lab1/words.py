#!/usr/bin/env python

#   Author: Makenzie Brian
#   File: Lab1 > words
#   Date: January 15, 2018
#   Class: ME599
#   Description: Count number of letter in text not case senseitive

def letter_count(text, letter):
    letterU =letter.upper()
    letterL = letter.lower()
    U = text.count(letterU)   #built in count is case sensitive
    L = text.count(letterL)
    return (U+L)


if __name__ == '__main__':
    txt = 'Large PIneAPPLes are falling FROM VERY smalL TreEs'
    ltr = 'A'

    print letter_count(txt, ltr)
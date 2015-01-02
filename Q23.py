#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 23
#
# Author:      Mrinal Wahal
#
# Created:     18/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os

inputs = input("Enter The Number Of Inputs - ")
empty = []
freq = []

for y in range (1,inputs+1):
    print "Enter Number %d - " % y
    num = input()
    empty.append(num)
    
print "The List Becomes", empty

def histogram(argument):
    for number in argument:
        print "*"*number

print "The Histogram Becomes :"    
histogram(empty)

empty.sort()

for element in empty:
    count = empty.count(element)
    freq.append(count)

print "The Frequency List Of All Characters Becomes", freq   
print "The Histogram For The Freq. List is :"
histogram(freq)

os.system("pause")
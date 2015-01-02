#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 26
#
# Author:      Mrinal Wahal
#
# Created:     19/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os

n = input("Enter The Number Of Inputs - ")
numbers = []

for x in range(1,n+1):
    print "Enter Number %d - " % x
    num = input()
    numbers.append(num)
    
def max_even(even):
    high = []
    for n1 in even:
        if n1%2 == 0:
            high.append(n1)
    print max(high)
    
def min_odd(odd):
    low = []
    for n2 in odd:
        if n2%2 !=0 :
            low.append(n2)
    print min(low)
    
print "The Highest Even Number In The Inputs is :", max_even(numbers)    
print "The Lowest Odd Number In The Inputs is :", min_odd(numbers)

os.system("pause")
#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 16
#
# Author:      Mrinal Wahal
#
# Created:     16/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

# Part 1 - Sum Of n Terms

import os

x = input("Enter Your Base X : ")
n = input("Enter Your Power N : ")

empty = []

for y in range(1,n+1):
    m = (x**y)/y
    print m, "+",
    empty.append(m)
    
print '=', sum(empty)

# Part 2 - Sum of Square Root of n Terms

n2 = input("Enter Your Nth Term : ")

def sqrt(sq):
    sqrt = sq**(1/2)
    return sqrt

nonempty = []

for i in range(1,n2+1):
    l = i/(sqrt(i+1))
    print l, '+',
    nonempty.append(l)
    
print '=', sum(nonempty)    
os.system("pause")    
    

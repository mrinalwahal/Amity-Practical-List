#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 10
#
# Author:      Mrinal Wahal
#
# Created:     07/07/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

n = input("Enter Your Number - ")   # Asks For The Number

s = 0
t = 0

while (n>0):
    a = n%10
    s = s+a
    n = n/10
    b = n%10
    t = t+b
    n = n/10

print s
print t
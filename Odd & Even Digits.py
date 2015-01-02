#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 10
#
# Author:      Mrinal WAhal
#
# Created:     21/07/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

n = input('Enter Your Number :')

s=0
t=1
p=1       # Tells Us The Position

while n>0:
    a= n%10
    if p%2==1:
        s = s+a
    else:
        t = t*a
    n = n/10
    p = p+1

print "Multiplication of Odd Digits ",s
print "Addition of Even Digits", t
print "Final Result", s+t
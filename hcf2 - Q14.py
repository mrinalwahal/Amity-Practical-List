#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     12/08/2014
# Copyright:   (c) student 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = input("Enter Your Larger no. : ")
m = input("Enter Your Smaller no. : ")

while n>m:
    if m%n==0:
        print m
        break
    x = m%n
    m=x
    n=m
print m
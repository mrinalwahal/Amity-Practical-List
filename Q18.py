#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 18
#
# Author:      Mrinal Wahal
#
# Created:     16/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os

rows = input("enter the input")

for i in range(0,rows):
    b = 11**i
    print " "*(rows-i),b%10,
    b = b/10
    while(b):
        a=b%10
        b=b/10
        print a,
    print

os.system("pause")
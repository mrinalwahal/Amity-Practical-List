#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 17
#
# Author:      Mrinal Wahal
#
# Created:     23/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os

heads = input('Enter No. Of Heads - ')
legs = input("Enter No. Of Legs - ")

for a in range (0,heads+1):
    for b in range (0,heads+1):
        if heads==a+b:
            if legs==4*a+2*b:
                     print a,b

os.system("pause")
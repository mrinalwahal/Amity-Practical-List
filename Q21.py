#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 21
#
# Author:      Mrinal Wahal
#
# Created:     18/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os
n = input("Input Your Number in Decimals - ")

print """\nKEY :
Hexadecimal - H
Octadecimal - O
Binary - B\n"""
dtype = raw_input("Enter You Desired Type Of Output - ")

if dtype == "H" or dtype == "h":
    print hex(n)
elif dtype == "O" or dtype == "o":
    print oct(n)
elif dtype == "B" or dtype == "b":
    print bin(n)
    
os.system("pause")    
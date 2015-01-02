#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 19
#
# Author:      Mrinal Wahal
#
# Created:     18/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os
string = raw_input("Enter Your String Here - ")

# Part (a) - Frequency of all characters

print "\nFrequency Of All Characters : "

for letter in string:
    count = string.count(letter)
    if count > 0:
        print letter, " - ", count

# Part (b) - Word of highest length

words = string.split()
print "\nLongest Word is", max(words, key=len)

# Part(c) - The string in title case

print "\nString In Title Case Will Be", '"', string.upper(), '"'

# Part (d) - Read full name as a string and print only the initials.

print "\nInitials Are :"
for intials in words:
    print (intials[0]).upper(),
    
os.system('pause')    
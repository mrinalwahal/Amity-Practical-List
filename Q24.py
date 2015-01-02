#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 24
#
# Author:      Mrinal Wahal
#
# Created:     18/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os

n = input("Enter Your Number - ")
print n,
elements = 0
empty = []

while n>0:
    if n%2 == 0:
        n /= 2
        print n,
        empty.append(n)
    else:
        n = (n*3) + 1
        print n,
        empty.append(n)
    if n == 1 :
        break
    
# i) Print total number of elements in the list

for element in empty:
    elements += 1
    
print "\nTotal Number Of Elements In The List : ", elements

# ii) Print the sorted list

empty.sort()
print "The Sorted List Becomes : ", empty

# iii) Delete all occurrences of multiples of 10 and print it .

for mult in empty:
    if mult%10 == 0:
        empty.remove(mult)
        
print "After Removing All The Multiples Of 10, List Becomes : ", empty

os.sytem("pause")
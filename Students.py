#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 12
#
# Author:      Mrinal Wahal
#
# Created:     14/07/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

#!/usr/bin/env python

print "-"*40
print "Welcome To Age Calculator."
print "-"*40

age1=0
age2=0
age3=0
age4=0

stds = int(raw_input("Enter Total No. Of Students - "))    # Asks For Total No. Of Students

for student in range(1,stds+1):                            # Executes the following for Every Student Input in 'stds'
    print "Enter Age Of Student %d - " % student
    age = int(raw_input())                                 # Takes The age Of Every Student

    if age>=12 and age<15:
        age1+=1
    if age>=15 and age<17:
        age2+=1
    if age>=17 and age<19:
        age3=age3+1
    if age<12:
        age4+=1


print "Group A : Between 12 & 15 Years - ", age1
print "Group B : Between 15 & 17 Years - ", age2
print "Group c : Between 17 & 19 Years - ", age3
print "Group D : Less Than 12 Years - ", age4

close = raw_input("Press Any Key To Terminate...")
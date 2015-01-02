#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 28
# Author:      Mrinal Wahal
# Created:     28/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

relatives ={"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother", "Homer" : "father", "Santa" : "dog"} 
ages = {"Lisa" : 8, "Bart":10,"Marge":35,"Homer":40,"Santa":2}

print "The Simpsons :"

for rel in relatives.iterkeys():
    print rel, "is a", relatives[rel], "and is",
    for age in ages.itervalues():
        print ages[rel], "Years Old."
        break
    

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     04/08/2014
# Copyright:   (c) student 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n = input("Enter Your First no. : ")
m = input("Enter Your 2nd no. : ")
l = 0
o = 0

for x in range(1,(n/2)+1):
    if n%x==0:
        l = x
        print "Factor is",x
print l, "is the Highest Factor."

for y in range(1,(m/2)+1):
    if m%y==0:
        o = y
        print "Factor is",y
print o,"is the Highest Factor."

if n%x==0 and m%y==0:
    print x
elif m%x==0 and n%y==0:
    print y
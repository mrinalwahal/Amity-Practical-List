#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 15
#
# Author:      Mrinal Wahal
#
# Created:     16/08/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

import os
import random

guess = random.randint(1,20)
name = raw_input("Heya ! What's Your Name : ")
print "Well,", name,", I have chosen of a number between 1 and 20."

chances = 0

for ask in range(1,4):
    ask = input("Take a Wild Guess : ")
    chances += 1
    if ask == guess and chances<3:
        print "Good Job,", name, ", you guessed the number in, ", chances, " !"
    elif chances<3:
        print "It's Okay !"
    elif chances == 3:
        print "Oops !", "You Lost !"
        print "By The Way The Number Was,", guess

os.system("pause")

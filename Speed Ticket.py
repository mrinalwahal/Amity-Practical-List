#-------------------------------------------------------------------------------
# Name:        Python Worksheet 1
# Purpose:     Question 8
#
# Author:      Mrinal Wahal
#
# Created:     07/07/2014
# Copyright:   (c) student 2014
#-------------------------------------------------------------------------------

from datetime import datetime

print 'Welcome To Delhi Police Ticket Computing.'
v = int(raw_input("Please Input Your Speed..."))
birthday = raw_input("Enter Date in MM-DD - ")

today = datetime.today()
today = datetime.strftime(today,"%m-%d")

birthday = datetime.strptime(birthday,"%m-%d")
birthday = datetime.strftime(birthday,"%m-%d")

print "Today is - ",today
if birthday==today:
    if 65<v and v<=85:
        print "You Get A Small Ticket."
    elif 86<=v:
        print "You Get A Big Ticket."
else :
    if 61<=v and v<=80:
        print "You Get A Small Ticket."
    elif 81<=v :
        print "You Get A Big Ticket."
    else :
        print "You're Innocent. You Don't Get a Ticket. Report The Cop To The Nearest Police Station for asking for bribe. "

print 'Thank You For Using The Program.'

close = raw_input("Press Any Key To Terminate...")






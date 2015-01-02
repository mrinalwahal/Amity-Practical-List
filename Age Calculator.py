#!/usr/bin/env python

print """Let's calculate for how long have u been alive ?
    """
def user():
    user = raw_input("Name of the Candidate: ")
    print """
Please enter ur age in numericals.
"""
    
    age = int(input("Age:"))

    days = age*365
    hours = 24*365*age
    minutes = 60*24*365*age
    sec = 60*60*24*365*age

    print user,'has lived for', days,'days,',hours,'hours, ', minutes,'minutes & ',sec,'seconds'
user()
print """
    May god bless u & U Live for 100 yrs.
    Take Care.
    """
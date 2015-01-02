#-------------------------------------------------------------------------------
# Name:        Agent Databse
# Purpose:     Vella-Panti
#
# Author:      Mrinal Wahal
#
# Created:     12/05/2014
# Copyright:   (c) Dynacrux
# Licence:     Dynacrux
#-------------------------------------------------------------------------------

import base64

inputid = raw_input("Enter Agent Login ID: ")
agent= "Mrinal"
if inputid == agent:
    print "Agent Recognized."
    password = raw_input("Enter Clearance Password: ")

    if password == "amity":
        print "Welcome Agent", inputid

        choice=raw_input("What Do You Wish To Know ?")
        print "NOTE : Given Information Will be in Encrypted Form."
        print "1 - Adress"
        print "2 - Parent's Name"
        print "3 - Last Known Base"
        choice1= "1"
        choice2= "2"
        choice3= "3"
        if choice == choice1:
            print "125B Bakers Street, London.".encode('base64')
            cdsfja=raw_input("Press Enter To Terminate...")
        if choice == choice2:
            print "Mr. and Mrs.Dragon BallZ".encode('base64')
            sdfsdafads=raw_input("Press Enter To Terminate...")
        if choice == choice3:
            print "Deep Cover, CIA, Langley, Virginia".encode('base64')
            sdfasdf=raw_input("Press Enter To Terminate...")
    print "Clearance Not Found."
    close=raw_input("Press Enter To Terminate...")
    exit()
print "Agent Not Found."
cdasefasd=raw_input("Press Enter To Terminate...")
exit()

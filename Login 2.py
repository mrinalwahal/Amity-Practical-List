#!/usr/bin/env python

agent = "Zephyr"
pas= "123456"

print "                                   Welcome To The World Of Cyber Security !"
for letter in agent:
    user=raw_input("Username:")
    if letter in user:
        print "Agent",user, "Recognized. "
        for letter in pas:
            authpassword=raw_input("Authentification Password:")
            if letter in authpassword:
                print "Agent logged In."
                colse=raw_input("Press any key to terminate...")
                exit()
            colse=raw_input("Press any key to terminate...")
            exit()    
    print "Login Failed. Have a nice Day !"
    print "Agent Identity Not Recognized."
    colse=raw_input("Press any key to terminate...")
    exit()






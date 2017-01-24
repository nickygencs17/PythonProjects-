#!/usr/bin/python
#Nicholas Genco
#webprog group project

import sys
import datetime
today = datetime.date.today()


lengths = len(sys.argv)

if (lengths == 4):
    print "Firstname:",sys.argv[1]#fristname
    print "Lastname:",sys.argv[2]#lastname
    i = int(sys.argv[3])#parseing string from argument into int
    newage = 2014 -i #finding birthday
    print newage #printing it
    response = raw_input('Has your birthday come yet this year?(Y OR N):')#data from std in
    if (response == "y" or response == "Y"):
        print "As of",today,"you are", newage
        sys.exit(0)#exit with no errors
    elif(response == "N" or response == "n" ):
        newage = newage - 1
        print "As of",today,"you are", newage
        sys.exit(0) #exit with no errors
    else:
        print "ERROR: invalid input"
        sys.exit(3) # exit with error code 3

else:
    print "Must be four arguments"
    sys.exit(4) # exit with error code 4

#you anit about that python life
#..BUT THATS NONE OF MY BUSINESSS THO
               
               
       

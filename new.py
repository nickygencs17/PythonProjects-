#!/usr/bin/python
#Nicholas Genco
#webprog group project
#ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letteR r substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher, developed in ancient Rome.


import sys #importing sys libary
stringname = "" #setting stringname to empty string


key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
#making a dict called key

dkey=dict(zip(key.values(),key))
#reversing key

lenggthh=len(sys.argv)#length of sys.argv set to int 
if (lenggthh == 3): #testing if length is greater then e
        if (sys.argv[1] == "e" or sys.argv[1] == "E"): #testing if second argument is e
                for c in sys.argv[2]: #encoding message 
                        if c in key: #if c is in key
                                stringname=stringname+key[c] #add key of c to emptystring 
                        else: #if stringname is special character
                                stringname=stringname+c #add special character 
        elif (sys.argv[1] == "d" or sys.argv[1] == "D"): #testing if second argument is d
                for f in sys.argv[2]: #decoding message         
                        if f in dkey: #testing if f is in dkey
                                stringname=stringname+dkey[f] #adding key of f into emptystring
                        else: #testing for special characters
                                stringname=stringname+f#adding special character
        else:#else second argument is not d or e
                print "ERROR: SECOND ARGUMENT IS NOT D/d or E/E"
                sys.exit(12)#system exit 
else:#else to arguments
        print " MUST HAVE THREE ARGUMENTS"
        sys.exit(9)#system exit
print stringname#printing stringname
sys.exit(0)#system exit 

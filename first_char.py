#!/usr/bin/env python3

import sys #import the sys function

def first_char(string): #define our function
    newstring = '' #declaring an empty string
    count = 0 #keeping count of the number of chars
    for s in string: #iterating through string at each character
        count +=1 #adding 1 to the count each time it iterates
        if s == string[0] and count >1: #checking to see if s is equal to the first index of the string and if it is not the first char
            newstring+='*' #adding special char for repeated character
        else: #what i want to happen if s is not in my original string
            newstring+=s #adding original 's' into newstring
    return newstring #returns our new string to our main function


#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    # fopen = open(args, 'r')
    # fread = fopen.read()
    #print(fread)
    #print(fread[:])
    print(first_char(args)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line argument
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
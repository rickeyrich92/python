#!/usr/bin/env python3

import sys #import the sys function

def simpadd(args): #defining our function
    args = args.split('\n') #spliting our argument at every newline
    ans = '' #creating an empty string
    for a in args: #iterating through argument
        a = a.split(' ') #spliting the lines of the file at the space
        count = float(a[0]) + float(a[1]) #adding the first and second indexes together and casting them as floats 
        ans+=str(count)+'\n' #adding the answer of the two index to our empty string and casting count as a string with a new line
    return ans #returning our final string
        




#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(simpadd(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
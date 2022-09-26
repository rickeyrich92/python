#! /usr/bin/env python3 


import sys
import re

def src_dst(args):
    src_dict = {}
    dst_dict = {}
    ip_dict = {}
    args = args.split("\n")
    return_str = ''
    count = 0
    count1 = 0 
    for a in args:
        a = a.split(';')
        #print(a[2])
        if len(a) > 7:
            if a[4] == '8.8.8.8':
                count += 1
            if a[4] == '8.8.4.4':
                count += 1

    return count

#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(src_dst(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
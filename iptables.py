#!/usr/bin/env python3

import sys
import re

regex = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


def iptables(args):
    srclist = []
    dstlist = []
    srccount = 0
    dstcount = 0 
    args = args.split('\n')
    #aa = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    
    for a in args:
        #print(a)
        #b = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        #x = a.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        #pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        #x = a.match(SRC)
        #if a not in srclist:
        #if x not in srclist:
            #srclist+=aa
            #srclist.append(x)
        #print(srclist)
        pattern = 'SRC=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' 
        pattern2 = 'DST=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        finalIP = re.findall(pattern, a)
        finalIP2 = re.findall(pattern2, a)
        #print(finalIP2)
        #print(finalIP)
        # x = finalIP[0]
        # y = finalIP[1]
        #if finalIP not in srclist:
        #if 'SRC' in finalIP:
        if finalIP not in srclist:
            srclist.append(finalIP)
            srccount+=1
        if finalIP2 not in dstlist:
            #if y not in dstlist:
            dstlist.append(finalIP2) 
            dstcount+=1

    ttlcount = srccount + dstcount

    #print(dstlist)    
    #print(len(dstlist))    
    print(srccount)
    print(dstcount)
    print(ttlcount)

        #print(finalIP)
        #print(srclist)
    


#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(iptables(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
#! /usr/bin/env python3 


import sys
import re


#write a script that detects icmp traffic and sends an alert to the host
#check the ip addr that is sending the requests against virustotal
#make sure that the script checks the snort rules to allow or deny traffic
#once snort is running, this script should automatically check all traffic coming in


#if snort is running and detects ssh attempts, run this snortrules function

    def snortrules(args):

    


#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(snortrules(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
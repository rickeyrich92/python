#!/usr/bin/env python3

import sys
import re


def blueteam(args):
    ip_dict = {}
    args = args.split("\n")
    return_str = ''
    count = 0
    for a in args:
        #count+=1
        a = a.split(";")
        # pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        # finalIP = findall(pattern, a)
        #print(a[2])
        if a[2] in ip_dict:
            ip_dict[a[2]] += 1
            ip_dict[a[2]] = ip_dict.get(a[2], 0) + 1
            #count = dict.get[a[2]] + 1
            #dict[a[2]] = {'total':0}
        else:
            ip_dict[a[2]] = 1

        #max_key = max(ip_dict, key=ip_dict.get)
        all_values = ip_dict.values()
        max_value = max(all_values)
            # count = 1
            # dict[a[2]] = count
            # dict[a[2]]+1
            # dict[a[2]]['total']+1
        #sorted_dict = sorted(ip_dict.keys())
        #return_str = sorted_dict
    # for sort in sorted_dict:
    #     if sort > 0:
    #         return_str = sort
    #     if sort > count:
    #         return_str = sort    
    #     # return_str += sort + ' - ' + str(dict[sort]) + "\n"
    # return return_str
        #print(ip_dict)
        #print(sorted_dict)
        #print(return_str)
        #print(max_key)
        #print(max_value)
    return max_value
    #print(count)    

    





#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(blueteam(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)
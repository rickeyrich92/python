#!/usr/bin/env python3

import sys

def counter(args):
    #extract different ip addrs from file
    #count the occurences of each ip addr
    #return the ip adddr with how many times it occurred
    #making an empty dict = {ip addr : value} 
    #check if ip addr is in file; if it isn't, add to dict if it is add to ip addr value
    #count = 0
    dict = {}
    return_str = ''
    lines = args.readlines()
    #lines.split('\n')
    #print(type(lines))
    for l in lines:
        #print(type(l))
        #llist=l.split()
        #print(type(llist))
        #print(llist[0])
        #ip_addr = llist[0]
        ip_addr = l.split()[0]
        if ip_addr in lines:
            #dict.key(ip_addr) + 1
            count = dict[ip_addr] + 1
            #print(dict)
        else:
            count = 1
        dict[ip_addr] = count
    return count
    #for l in lines:
        #l = l.strip()
        #if l in dict.keys():
            #dict[l] + 1
        #else:
             #+ 1 
        #dict[l] =      


def main(args):
    olist = open(args, 'r')
    print(counter(olist))
    olist.close()

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)

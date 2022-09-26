#!/usr/bin/env python3

import sys

def naughty_or_nice(list):
    dict = {'good': 0, 'bad' : 0}
    #gcount = 0
    #bcount = 0
    return_str = 'good'
    lines = list.readlines()
    for l in lines:
        #print(l)
        #sssssssl.strip()
        #if return_str in dict.keys():
        if return_str in l:
            dict['good']+=1
        else:
            dict['bad']+=1
    #print(dict.keys())
    #return 'Naughty list has ' + str(bcount) + ' people!' + '\n' + 'Nice list has ' + str(gcount) + ' people!' 
    return 'Naughty list has ' + str(dict['bad']) + ' people!' + '\n' + 'Nice list has ' + str(dict['good']) + ' people!' 


def main(args):
    open_list = open(args, 'r')
    print(naughty_or_nice(open_list))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
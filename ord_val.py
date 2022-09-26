#!/usr/bin/env python3

import sys


def ord_val(args):
    count = 0
    args = ("".join(args))
    args = args.strip()
    #print(args)
    for a in args:
    #     a = str(list(a))
    #     print(ord(a))
        if a.isalpha() == True:
            #print(ord(a))
            count = ord(a) + count
    #     # a = a.split(' ')
    #     #print(a)
    #     #ord(a) + count
    return count

def main(args):
    fopen = open(args, 'r')
    print(ord_val(fopen))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
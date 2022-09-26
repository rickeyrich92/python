#!/usr/bin/env python3

import sys 

def cipher(string):
    retstring = ''
    string = string.split(' ')
    for s in string:
        if s[0].isupper() and s[-1].islower():
            retstring+=s+' '
    return retstring



def main(args):
    fopen = open(args, 'r')
    fread = fopen.read()
    print(cipher(fread))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
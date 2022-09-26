#!/usr/bin/env python3

import sys


def binary_mafs(string):
    sum = 0
    string = string.split(' ')
    for s in string:
        #print(int(s,2))
        sum+=int(s,2)

        # s = int(s)
        # print(bin(s))
    #     int(s,2)+=sum
    return sum

def main(args):
    fopen = open(args, 'r')
    fread = fopen.read()
    #print(fread)
    #print(fread[:])
    print(binary_mafs(fread))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
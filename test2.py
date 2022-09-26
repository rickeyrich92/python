#! /usr/bin/env python3

# import requests
# print(requests.get('8.8.8.8').json())

import re
import sys

# def findmal(file):
#     pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
#     print(pattern)
#     count = 0 
    # if 'Failed password' in file:
    #     count+=1
    #     if count == 5:
    #         return pattern
#file = '/home/kali/python/test.txt'
def test(args):
    args = args.split('\n')
    
    for ip in args:
        #ip = ip.split('\n')
        #print(ip)
        s = 'Failed password for valeria'
        if s in ip:
            return ip
    # return final
            # pattern = re.compile(s + '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
            # pattern2 = re.match(pattern, ip)
            # finalIP = re.findall(pattern, s)
            # print(finalIP)
        #return finalIP
#print(pattern)    

def main(args):
    fopen = open(args, 'r')
    fread = fopen.read()
    #print(fread[:])
    print(test(fread))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
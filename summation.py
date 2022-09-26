#!/usr/bin/env python3

import sys

#open a file and read the numbers in that file
#find the lowest number of the two numbers
#add the numbers in the range of the two and print the sum

def summation(args):
    # for a in args:
    #     sum = 0 
    #     num = a.rstrip().split()
    #     for j in range(len(num)):
    #         num[j] = int(num[j])
    #     num.sort()
    #     print(num)
    #print(args[0])
    #args = args.split(' ')
    #print(args[0])
    x = int(args[0])
    y = int(args[1])

    if x < y:
        x2 = x
        y2 = y 
    else:
        x2 = y
        y2 = x
    #print(x2)
    #print(y2)
    sum = 0 
    for a in range(x2,y2+1):
        #print(a)
        #a = a.split(' ')
        #print(a)
        sum+=a 
    # return count
    # args = args.readlines()
    # x = args[0]
    # #y = args[1]
    # print(args)
    # #print(args[0])
    # #print(args[1])
    # #print(args.split(' '))
    # sum = 0 
    # #print(args)
    # for num in range(int(y),int(x)+1):
    #     #print(num)
    #     if num <= x:
    #         sum+=num
    return sum
    # sum = 0
    # for a in args:
    #     a = a.split(' ')
    #     #print(a[0], a[1])
    #     length = len(args) - 1
    #     print(length)
    #     x = int(a[0])
    #     y = int(a[1])
    #     for n in range (x,y):
    #         print(n)
            #print(n)

    
   
    




def main(args):
    fopen = open(args, 'r')
    fread = fopen.read()
    #print(fread)
    #print(fread[:])
    print(summation(fread))

if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
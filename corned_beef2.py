#!/usr/bin/env python3

import sys
import hashlib 
import random

#the chr() function might be useful; not useful, only good for ASCII text
#string = 'FS{hash-I_had_corned_beef_and_hash_' + var + '}'
#the hex() function is what we need 
hash = '12d2479c78dbe724c777a3950c52bc87d6aee04ff977651bc95fe067b57ac56418b4f910b64ea5cbca346422455f6612ab081de548ecd72fdb56835a1c153621'


for num in range(0,16):
    #print(num)
    c1=(hex(num).split('x')[-1])
    for num in range(0,16):
        #print(num)
        c2=(hex(num).split('x')[-1])
        for num in range(0,16):
            #print(num)
            c3=(hex(num).split('x')[-1])
            var = str(c1)+str(c2)+str(c3)
            flag = 'FS{hash-I_had_corned_beef_and_hash_' + var + '}'
            #print(flag)
            check1 = hashlib.sha256(flag.encode('utf-8')).hexdigest()
            check2 = hashlib.sha512(flag.encode("utf-8") ).hexdigest()
            #print(check1)
            #print(check2)
            if check1 == hash:
                print(flag, check1, 'this is sha256')
            elif check2 == hash:
                print(flag, check2, 'this is sha512')

    
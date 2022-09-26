#!/usr/bin/env python3

import sys
import re
import time
import json
import requests
import os
import os.path
from os import path

#from email.message import EmailMessages


def findmal(file):
    file = file.split('\n')
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    count = 0

    for log in file:
        s = 'Failed password for valeria'
        count+=1
        if s in log:
            ip = re.findall(pattern, log)
            if count >= 5:
                return ip


##### Variables #####
ApiVirus     = '0d77a812ce2b66f28865e4ace2cc9ffb20c3796922032f62a350daf147c8ad43'
#ip = findmal(file)
   
##### Functions #####
def web_request(url, verb, headers, data_json, auth_list):
    #ip = (findmal(file))
    s = requests.Session()
    s.headers.update(headers)
    if verb == 'get':
        response = s.get(url, verify=False)
    elif verb == 'post':
        response = s.post(url, verify=False, data=json.dumps(data_json), auth=auth_list)
    else:
        print('else: '+verb)
    return response


#@findmal
def main(main_args):
    fopen = open(args, 'r')
    fread = fopen.read()
    #print(findmal(fread))
    ip = findmal(fread)[0]
    #print(ip)
    vendors = [
        {
            'url' : 'https://www.virustotal.com/api/v3/ip_addresses/' + str(ip),
            'verb' : 'get',
            'headers' : {'x-apikey': ApiVirus},
            'data_json' : {},
            'auth_list' : ()
        },
    ]

    for vendor in vendors:
        #print(vendor['url'])
        response = web_request(vendor['url'], vendor['verb'], vendor['headers'], vendor['data_json'], vendor['auth_list'])
        #print(vendor['url'])
        #print(response.json())
        print(ip)
        print(response.json()['data']['attributes']['last_analysis_stats'])
        if path.isfile("/snort/logs/hydraAttack.log") == True:
            f = open("/snort/logs/hydraAttack.log", "w")
            f.write("drop tcp " + str(ip) + " any -> 192.168.56.108 22; sid:543367\n")
    #(msg:\'Possible malicious IP\'; sid:4324;)"
            f.close()
        else:
            f = open("/snort/logs/hydraAttack.log", "x")
            f.write("drop tcp " + str(ip) + " any -> 192.168.56.108 22; sid:543367\n")
            f.close()
    f = open("/etc/snort/snort.conf", "a")
    f.write("include /snort/logs/hydraAttack.log\n")
    f.close()
    cmd = 'sudo snort'
    os.system(cmd)
        


if __name__ == '__main__':
    args = sys.argv[1]
    main(args)
#!/usr/bin/env python3

import sys
import re
import time
import json
import requests
import smtplib
from email.message import EmailMessages
import os

    ##### Variables #####
ApiVirus     = '0d77a812ce2b66f28865e4ace2cc9ffb20c3796922032f62a350daf147c8ad43'
    
##### Functions #####
def web_request(url, verb, headers, data_json, auth_list):
    s = requests.Session()
    s.headers.update(headers) 
    if verb == 'get':
        response = s.get(url, verify=False)
    elif verb == 'post':
        response = s.post(url, verify=False, data=json.dumps(data_json), auth=auth_list)
    else:
        print('else: '+verb)
    return response


def main(main_args):
    vendors = [
        {
            'url' : 'https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8',
            'verb' : 'get',
            'headers' : {'x-apikey': ApiVirus},
            'data_json' : {},
            'auth_list' : ()
        },
    ]

    for vendor in vendors:
        response = web_request(vendor['url'], vendor['verb'], vendor['headers'], vendor['data_json'], vendor['auth_list'])
        print(response.json()['data']['attributes']['last_analysis_stats'])
        if response_json['malicious'] >= 4:
            # with open('/etc/snort/rules/local.rules', 'a') as nr:
            #     nr.write(rule) 
            f = open("../snort/logs/hydraAttack.log", "w")
            f.write("alert icmp" + s + " any -> 192.168.56.108 22 (msg:\'Alert! Malicious IP\' react: drop; sid: 20000000;)
            f.close()
            r = open('/etc/snort/snort.config', 'a')
            r.write('include /snort/logs/hydraAttack.log')
            r.close()
            cmd = 'ls -l'
            os.system(cmd)

        

def findmal(file):
    # pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    # count = 0 
    # if 'Failed password' in file:
    #     count+=1
    #     if count < 5:
    #         continue
    #     else:
    #         return pattern
    args = args.split('\n')
    
    for ip in file:
        s = 'Failed password for valeria'
        if s in ip:
            return ip


#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print((fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)


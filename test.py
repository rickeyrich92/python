#! /usr/bin/env python3


import json
import requests

#print('4')


#def check(findmal):
print('4')
api_key = '0d77a812ce2b66f28865e4ace2cc9ffb20c3796922032f62a350daf147c8ad43'
url = 'https://www.virustotal.com/gui/home/search'

# params = {'apikey': api_key, 'resource': site}
# reponse = requests.get(url, params = params)
# response_json = json.loads(response.content)
site = '8.8.8.8'


    #for site in findmal:
params = {'apikey': api_key, 'resource': site}
response = requests.get(url, params = params)
response_json = json.loads(response.content.decode("utf-8"))
print(request.get('https://www.virustotal.com/gui/home/search').content)
        # if response_json['positive'] >= 4:
        #     # with open('/etc/snort/rules/local.rules', 'a') as nr:
        #     #     nr.write(rule) 
        #     f = open("../snort/logs/hydraAttack.log", "w")
        #     f.write("alert icmp" + site + " any -> 192.168.56.108 22 (msg:\'Alert! Malicious IP\' react: block,)
        #     f.close()


# response = requests.get(url)
# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204:
#print(response_json)
# print(response_json)
# print(params)


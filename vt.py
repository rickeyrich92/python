#! /usr/bin/env python3

import sys
import requests
   
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
    s = '8.8.8.8'
    vendors = [
        {
            'url' : 'https://www.virustotal.com/api/v3/ip_addresses/'+ s ,
            'verb' : 'get',
            'headers' : {'x-apikey': ApiVirus},
            'data_json' : {},
            'auth_list' : ()
        },
    ]

    for vendor in vendors:
        response = web_request(vendor['url'], vendor['verb'], vendor['headers'], vendor['data_json'], vendor['auth_list'])
        print(response.json()['data']['attributes']['last_analysis_stats'])


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
#!/usr/bin/env python3

import os
import re

log ='/var/log/auth.log'

def increment(ips: dict, line: str):
    match = re.match(r'^.+?\s+-\s+(?P<ip>\d{1,3}(\.\d{1,3}){3})\s.*$', line)
    if match:
        ip = match.group('ip')
        if not ip in ips:
            ips[ip] = 0
        ips[ip] += 1

def parse_log_file(log: str) -> dict:
    ips = dict()
    with open(log, 'r') as file:
        for line in file:
            increment(ips, line)
    return ips

# log is the path to the log file:
for key, value in parse_log_file(log).items():
    print(key, ":", value)
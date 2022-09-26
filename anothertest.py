#! /usr/bin/env python3

import requests
import json


response = requests.get("https://api.open-notify.org/astros.json")
print(response.status_code)
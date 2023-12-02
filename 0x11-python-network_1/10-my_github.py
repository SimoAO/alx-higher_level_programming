#!/usr/bin/python3
"""Takes my GITHUB credentials and uses the GITHUB API to display"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username, password)
    req = requests.get(url, auth=auth)
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().get('id'))

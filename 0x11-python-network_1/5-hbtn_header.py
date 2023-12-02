#!/usr/bin/python3
"""Takes in a URL, sends a request to it and displays the value"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))

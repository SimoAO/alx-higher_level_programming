#!/usr/bin/python3
"""Takes in a URL and EMAIL, sends a POST request with URL w EMAIL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    req = requests.post(url, data=email)
    print(req.text)

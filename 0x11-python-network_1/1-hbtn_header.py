#!/usr/bin/python3
"""
A Pyhton script that tales in a URL, sends a request to it and
displays the value of the X-request-Id variable found in the header
"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as request:
        print(request.info()["X-Request-Id"])

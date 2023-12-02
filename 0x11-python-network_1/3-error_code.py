#!/usr/bin/python3
"""Takes in a URL, sends a request to it and displays the body"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as request:
            print(request.read().decode('UTF-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

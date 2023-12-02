#!/usr/bin/python3
"""Takes in aletter and sends a POST request to URL with the letter"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post(url, data={"q": q})
    try:
        reqj = req.json()
        if len(reqj) == 0:
            print("No result")
        else:
            print("[{}] {}".format(reqj.get("id"), reqj.get("name")))
    except ValueError:
        print("Not a valid JSON")

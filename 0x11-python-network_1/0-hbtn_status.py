#!/usr/bin/python3
"""A Python script that fetchs an URL"""
import urllib.request


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as request:
        cont = request.read()
        print('Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(cont), cont, cont.decode('UTF-8')))

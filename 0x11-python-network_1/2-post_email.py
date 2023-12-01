#!/ussr/bin/python3
"""
Takes in a URL and an EMAIL, sends a POST request to the passed URL
with the email as a parameter and displays the body of the response
"""
import urllib.request
import sys
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")
    with urllib.request.urlopen(url, data) as request:
        print(request.read().decode("UTF-8"))


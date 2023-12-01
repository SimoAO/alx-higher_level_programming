#!/bin/bash
# Sends a request to a URL and displays only the status code
curl -s -w '%{http_code}' -o /dev/null "$1"

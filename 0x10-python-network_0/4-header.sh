#!/bin/bash
# Takes in a URL, sends a GET and displays the body
curl -s -H "X-School-User-Id: 98" "$1"

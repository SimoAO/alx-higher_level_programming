#!/bin/bash
# Takes in a URL and displays all HTTP methodsthe server accept
curl -sI "$1" | grep -i "Allow" | cut -d ' ' -f 2-

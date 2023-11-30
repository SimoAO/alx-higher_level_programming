#!/bin/bash
# Takes in a URL and displays all HTTP methodsthe server accept#!/bin/bash
curl -i -X OPTIONS "$1" | grep -i "Allow" | cut -d ' ' -f 2-

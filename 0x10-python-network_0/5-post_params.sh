#!/bin/bash
# Takes in a URL, sends a POST and diplays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

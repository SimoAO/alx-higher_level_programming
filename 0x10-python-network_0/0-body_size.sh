#!/bin/bash
# A Bsh script that displays the size of the body
curl -s -o '%{size_download}\n' /dev/null "$1"

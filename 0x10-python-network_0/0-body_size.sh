#!/bin/bash
# A Bsh script that displays the size of the body
curl -s -o /dev/null -w '%{size_download}\n' "$1"

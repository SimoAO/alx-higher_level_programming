#!/bin/bash
# A Bsh script that displays the size of the body
curl -s -I /dev/null -w '%{size_download}\n' "$1"

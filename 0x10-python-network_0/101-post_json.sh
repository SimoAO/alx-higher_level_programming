#!/bin/bash
# Sends a JSON POST and displays rthe body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"

#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server accepts
curl -sI OPTIONS "$1" | grep 'Allow:' | cut --complement -f1 -d" "

#!/bin/bash
# Sends a request to URL passed as an argument, and displays only the status code
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)

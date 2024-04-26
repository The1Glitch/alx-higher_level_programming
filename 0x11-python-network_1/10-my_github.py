#!/usr/bin/python3
"""
Python script that take your GITHUB credentials (username and password)
and uses the GITHUB API to display your id
"""
import sys
import requests
from requests.auth import HHTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

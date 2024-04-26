#!/usr/bin/python3
"""Script that takes in a URL and email, sends a POST request
   And displays the body of the reponse.
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urlib.parse.urlencode(value).encode("ascii")

    request = urlib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))

#!/usr/bin/python3
"""Script that takes in a URL,
   Sends a request to the URL,
   And displays the value of the X-Request-Id
   variable found on the header of the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.header).get("X-Request-Id"))

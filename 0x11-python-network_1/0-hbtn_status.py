#!/usr/bin/python3
''' script that fetches https://intranet.hbtn.io/status '''
from urllib.request import urlopen
url = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t-  utf content:", body.decode())

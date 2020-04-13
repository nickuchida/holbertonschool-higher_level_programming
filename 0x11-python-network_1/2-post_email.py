#!/usr/bin/python3
''' sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response (decoded in utf-8)'''
from sys import argv
from urllib.request import urlopen, Request
import urllib

if __name__ == '__main__':
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    with urlopen(Request(argv[1], data)) as respond:
        retur = respond.read()
    print(retur.decode('utf-8'))

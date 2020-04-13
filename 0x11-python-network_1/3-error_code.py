#!/usr/bin/python3
''' takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8). '''
from sys import argv
from urllib.request import urlopen, Request
import urllib
from urllib.error import HTTPError
from urllib.parse import urlencode

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as url:
            print(url.read().decode('utf-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))

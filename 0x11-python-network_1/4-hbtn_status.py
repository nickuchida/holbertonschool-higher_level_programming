#!/usr/bin/python3
'''
 script that fetches https://intranet.hbtn.io/status
'''
from requests import get

res = get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(res.text)))
print('\t- content: {}'.format(res.content.decode('utf-8')))

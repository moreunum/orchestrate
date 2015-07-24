#!/bin/env python

import requests
import subprocess

poolSize = 4

###########################################
def setDefaultConfig():
  headers = {'Content-Type':'application/x-www-form-urlencoded'}
  body = 'value="more stuff"'
  resp = requests.put('http://localhost:4001/v2/keys/test', 
    headers=headers, 
    data=body)
  print(resp.json())

###########################################
def createPool():
  for i in range(0, 4):
    output = subprocess.check_output(['docker', 'run', '-d', 
      '--name', 'pool_%d' % i, '--net=host', 'centos-supervisor'])

###########################################
if __name__ == '__main__':
  createPool()

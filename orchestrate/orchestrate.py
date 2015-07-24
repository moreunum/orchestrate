#!/bin/env python

import requests
import subprocess

poolSize = 4
containers = []

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
  #Create containers
  for i in range(0, 4):
    name = 'pool_' + str(i)
    output = subprocess.check_output(['docker', 'run', '-d', 
      '--name', name, '--net=host', 'centos-supervisor'])
    containers.append(output.translate(None, ''.join(['\n'])))
    print(containers)

  # Set pool info
  body = 'value=' + str(poolSize)
  resp = requests.put('http://localhost:4001/v2/keys/poolSize', 
    headers={'Content-Type':'application/x-www-form-urlencoded'}, 
    data=body)

###########################################
def assignServices():
  pass

###########################################
if __name__ == '__main__':
  createPool()
  assignServices()

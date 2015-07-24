#!/bin/env python

import requests
import subprocess
import time

poolSize = 4
containers = []
services = ['serviceA', 'serviceB']
etcdUrl = 'http://localhost:4001'
etcdHeader = {'Content-Type':'application/x-www-form-urlencoded'}

###########################################
def setDefaultConfig():
  body = 'value="more stuff"'
  response = requests.put(etcdUrl + '/v2/keys/test', 
    headers=etcdHeader, 
    data=body)
  print(response.json())

###########################################
def createPool():
  #Create containers
  for i in range(0, 4):
    name = 'pool_' + str(i)
    output = subprocess.check_output(['docker', 'run', '-d', 
      '--name', name, '--net=host', '-e', 'MY_NAME=' + name, 'redshirt'])
    containers.append(name)
    print(name)

  # Set pool info
#  body = 'value=' + str(poolSize)
#  response = requests.put(etcdUrl + '/v2/keys/poolSize', 
#    headers=etcdHeader, 
#    data=body)
#  print(response.json())

###########################################
def assignServices():
  for service in services:
    container = containers.pop()
    body = 'value=' + str(service)
    print(body)
    url = etcdUrl + '/v2/keys/poolContainers/' + container + '/service' 
    print(url)
    response = requests.put(url,
      headers=etcdHeader, 
      data=body)
    print(response.json())

###########################################
if __name__ == '__main__':
  createPool()
  time.sleep(5)
  assignServices()

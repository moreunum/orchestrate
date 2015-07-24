#!/bin/env python

import requests
import subprocess
import time
import BaseHTTPServer

poolSize = 4
containers = []
services = ['serviceA', 'serviceB']
etcdUrl = 'http://localhost:4001'
etcdHeader = {'Content-Type':'application/x-www-form-urlencoded'}

###########################################
def createPool():
  for i in range(0, 4):
    name = 'pool_' + str(i)
    output = subprocess.check_output(['docker', 'run', '-d', 
      '--name', name, '--net=host', '-e', 'MY_NAME=' + name, 'redshirt'])
    containers.append(name)
    print(name)

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
def setStatus(status):
    response = requests.put(etcdUrl + '/v2/keys/orchestrator/status', 
      headers=etcdHeader, 
      data=status)
  
###########################################
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    s.send_response(200)
    s.send_header('Content-type', 'text/html')
    s.end_headers()
    s.wfile.write(

###########################################
if __name__ == '__main__':
  setStatus('notReady')
  createPool()
  print("Delay to allow for container startup...")
  time.sleep(5)
  setStatus('ready')
  assignServices()

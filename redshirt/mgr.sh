#!/bin/bash

# Get Docker ID hash
#DOCKER_ID=$(cat /proc/self/cgroup | \
#  grep -o  -e "docker-.*.scope" | \
#  head -n 1 | sed "s/docker-\(.*\).scope/\\1/")

# Register this container in etcd
curl -XPUT http://localhost:4001/v2/keys/poolContainers/"$MY_NAME" -d dir=true

# Wait on command from orchestrator
SERVICE=$( \
  curl http://localhost:4001/v2/keys/poolContainers/"$DOCKER_ID"/service?wait=true | \
  python -c 'import json,sys;j=json.load(sys.stdin);print j["node"]["value"]')
echo "Service: $SERVICE"

supervisorctl start "$SERVICE"

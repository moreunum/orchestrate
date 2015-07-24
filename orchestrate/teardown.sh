#!/bin/bash
docker rm -f $(docker ps -a | ack pool | awk '{print $1}')
docker rm -f sup
docker rm -f etcd
docker run -d --name etcd --net=host etcd

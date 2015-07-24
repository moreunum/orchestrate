#!/bin/bash
docker rm -f $(docker ps -a | ack pool | awk '{print $1}')
docker run --rm --net=host etcd etcdctl rm /poolContainers --recursive
docker run --rm --net=host etcd etcdctl rm /poolSize --recursive

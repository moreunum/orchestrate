#!/bin/bash
docker rm -f $(docker ps -a | ack pool | awk '{print $1}')
docker rm -f sup
docker run --rm --net=host etcd etcdctl rm /poolContainers --recursive
docker run --rm --net=host etcd etcdctl rm /poolSize --recursive

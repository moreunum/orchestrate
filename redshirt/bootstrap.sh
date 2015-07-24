#!/bin/bash

supervisord -c /supervisord.conf

while :
do
  echo 'bootstrap.sh'
  sleep 1
done

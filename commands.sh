docker run -d --name etcd --net=host etcd

docker run --rm --net=host etcd etcdctl set /test stuff
docker run --rm --net=host etcd etcdctl ls --recursive
docker run --rm --net=host etcd etcdctl rm /containers --recursive

curl 'http://localhost:4001/v2/keys/containers?recursive=true&sorted=true' | python -m json.tool

docker run -d --name sup --net=host centos-supervisor

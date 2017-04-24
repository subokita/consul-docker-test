set -v

docker-machine create --driver virtualbox default || true
docker-machine start default || true
eval $(docker-machine env default)
export DOCKER_MACHINE_IP=$(docker-machine ip default)

set +v
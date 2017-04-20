# consul-docker-test
Testing running consul in docker in OS X.

Just me trying to understand how consul works within docker within OSX. 
To get started, run

```
# Create docker machine and set the environment of it
docker-machine create default
eval $(docker-machine env)

# Because we use DOCKER_MACHINE_IP environment variable in the docker-compose.yml
export DOCKER_MACHINE_IP=$(docker-machine ip)

# Start docker compose, forcing it to build if necessary, and run it detached
docker-compose up --build -d
```

Then you could check for consul membership and registered services:

```
# Check for the consul nodes
consul members --http-addr=$(docker-machine ip):8500

# Check for the registered services, json_pp is for pretty printing JSON, use jq if you're in linux
curl $(docker-machine ip):8500/v1/catalog/services | json_pp

# Check for the specific service
curl $(docker-machine ip):8500/v1/catalog/service/hello-server | json_pp
```

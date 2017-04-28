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


Then finally you could do a proof of concept, using call-server to call hello-server internally
using Consul's discovery service

```
# Run curl onto call-server service in consul, and use jq to obtain the port number
curl -s $(docker-machine ip):8500/v1/catalog/service/call-server | jq -r '.[].ServicePort'

# for example it returns me
# 32777
# Now we could call call-server at port 32777

curl -s $(docker-machine ip):32777

# And it should print out something similar to below
{"CreateIndex": 384, "ServicePort": 32776, "ServiceTags": [], "ModifyIndex": 384, "ServiceEnableTagOverride": false, "Node": "bootstrap-node", "ID": "102b597f-0b4c-4702-985e-327a5a022cc7", "NodeMeta": {}, "TaggedAddresses": {"wan": "192.168.99.100", "lan": "192.168.99.100"}, "Address": "192.168.99.100", "ServiceName": "hello-server", "ServiceID": "ab1720162e4c:hello-server:80", "ServiceAddress": "192.168.99.100"} Hello World

```

We're using Consul-Template + NGINX to do reverse proxy and automatic load balancing, thus now the hello-server and call-server services can be accessed from:
```
curl -s $(docker-machine ip)/api/hello-server
curl -s $(docker-machine ip)/api/call-server
```

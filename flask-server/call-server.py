
import os
import uuid
import consul
import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def call():
    # Create a new consul client, with consul address and port obtained from docker environment variables
    consul_agent_address = os.environ.get( 'CONSUL_AGENT_ADDR', 'consul-bootstrap' )
    consul_agent_port    = int(os.environ.get( 'CONSUL_AGENT_PORT', 8500 ))
    consul_client        = consul.Consul( host=consul_agent_address, port=consul_agent_port )

    # Get the registered hello-server service
    hello_service = consul_client.catalog.service('hello-server')[1][0]
    message = json.dumps(hello_service)

    # Craft the request URL using registered hello-server's address and port
    url = 'http://%s:%d' % ( hello_service['ServiceAddress'], hello_service['ServicePort'] )

    return message + " " + requests.get( url ).text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
import os
import uuid
import consul
from flask import Flask

app = Flask(__name__)

@app.route("/")
def call():
    return "Call"

if __name__ == '__main__':
    consul_agent_address = os.environ.get( 'CONSUL_AGENT_ADDR', 'consul-bootstrap' )
    consul_agent_port    = int(os.environ.get( 'CONSUL_AGENT_PORT', 8500 ))
    consul_client        = consul.Consul( host=consul_agent_address, port=consul_agent_port )

    services = consul_client.agent.services()
    for service in services:
        print( service )
    app.run(host='0.0.0.0', port=80, debug=True)
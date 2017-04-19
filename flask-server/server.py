import os
import socket
import uuid
import consul
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == '__main__':
    print( "hostname: " + socket.gethostname() ) 

    consul_service_name  = os.environ.get( 'CONSUL_SERVICE_NAME', 'flask-server' )
    consul_agent_address = os.environ.get( 'CONSUL_AGENT_ADDR', 'consul-bootstrap' )
    consul_agent_port    = int(os.environ.get( 'CONSUL_AGENT_PORT', 8500 ))

    consul_client = consul.Consul( host=consul_agent_address, port=consul_agent_port )
    consul_client.agent.service.register( consul_service_name, service_id=str(uuid.uuid4()), address='0.0.0.0', port=8500 )
    app.run(host='0.0.0.0', port=80, debug=True)
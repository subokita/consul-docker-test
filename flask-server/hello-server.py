import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    consul_agent_address = os.environ.get( 'CONSUL_AGENT_ADDR', 'consul-bootstrap' )
    consul_agent_port    = int(os.environ.get( 'CONSUL_AGENT_PORT', 8500 ))
    
    # consul_agent_address = 'consul-8500.service.consul'
    # curl 192.168.99.100:8500/v1/catalog/servic
    url      = ('http://%s:%d/v1/catalog/services') % (consul_agent_address, consul_agent_port)
    response = requests.get(url, timeout=0.01).text

    return "Hello World\n" + response 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
import uuid
import consul
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == '__main__':
    consul_client = consul.Consul(host='consul-bootstrap', port=8500)
    consul_client.agent.service.register('flask-server', service_id=str(uuid.uuid4()), address='0.0.0.0', port=8500 )
    app.run(host='0.0.0.0', port=80, debug=True)
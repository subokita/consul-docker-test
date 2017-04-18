FROM        python:3.5.2

COPY        requirements.txt requirements.txt
RUN         pip install --no-cache-dir -r requirements.txt
ENV         PYTHONPATH=/usr/local/app

COPY        flask_server   /usr/local/app/consul-docker-test/flask_server

WORKDIR     /usr/local/app/consul-docker-test
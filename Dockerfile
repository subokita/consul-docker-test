FROM        python:3.5.2-slim

COPY        requirements.txt requirements.txt
RUN         apt-get update \
            &&  apt-get install -y \
                build-essential \

            &&  pip install --no-cache-dir -r requirements.txt \

            &&  rm -rf /var/lib/apt/lists/* \
            &&  apt-get purge -y \
                build-essential 

ENV         PYTHONPATH=/usr/local/app
COPY        flask-server   /usr/local/app/consul-docker-test/flask-server
WORKDIR     /usr/local/app/consul-docker-test
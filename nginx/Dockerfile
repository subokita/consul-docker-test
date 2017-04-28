FROM        nginx:latest
RUN         apt-get update \
            && apt-get install -y \
                unzip \
                watch

ADD         https://releases.hashicorp.com/consul-template/0.18.2/consul-template_0.18.2_linux_amd64.zip /usr/bin/
RUN         unzip /usr/bin/consul-template_0.18.2_linux_amd64.zip -d /usr/local/bin \
            && mkdir /etc/consul-templates \
            && mkdir /logs/ \
            && mkdir -p /usr/local/app/nginx-consul-template

WORKDIR     /usr/local/app/nginx-consul-template
CMD         "bash"
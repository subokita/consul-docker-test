#!/bin/bash
/usr/sbin/nginx -c /etc/nginx/nginx.conf && \
consul-template -consul-addr=${CONSUL_AGENT_ADDR}:${CONSUL_AGENT_PORT} \
                -template="./consul.ctmpl:/etc/nginx/conf.d/services.conf:/usr/sbin/nginx -s reload"

# consul-template -consul-addr=${CONSUL_AGENT_ADDR}:${CONSUL_AGENT_PORT} \
#                 -template="/etc/consul-templates/consul.ctmpl" -dry -once
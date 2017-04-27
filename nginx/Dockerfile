FROM        nginx
COPY        ./nginx.conf      /etc/nginx/nginx.conf
COPY        ./mime.types      /etc/nginx/mime.types
COPY        ./uwsgi_params    /etc/nginx/uwsgi_params
RUN         mkdir /logs/
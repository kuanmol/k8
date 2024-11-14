FROM alpine:latest

RUN apk update && apk add nginx

RUN mkdir -p /usr/share/nginx/html

RUN echo "<html><body><h1>basic web server on nginx using docker</h1></body></html>" > /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


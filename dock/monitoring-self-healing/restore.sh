#!/bin/bash

# Stop the current container
docker stop docker_app

# Remove the current container
docker rm docker_app

# Copy the old version (1.0) of the app into the container
cp -r version/1.0/* app/

# Rebuild the image
docker build -t my-flask-app .

# Restart the container
docker run --name docker_app --restart on-failure -p 5000:5000 my-flask-app

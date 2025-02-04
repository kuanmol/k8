#!/bin/bash

THRESHOLD_CPU=50  # CPU usage threshold in percentage
MAX_CONTAINERS=5  # Maximum number of backend containers
MIN_CONTAINERS=2  # Minimum number of backend containers

while true; do
    CONTAINER_COUNT=$(docker ps --filter "name=backend" --format "{{.ID}}" | wc -l)

    # Get average CPU usage (convert percentage to integer)
    AVG_CPU=$(docker stats --no-stream --format "{{.CPUPerc}}" | sed 's/%//' | awk '{sum+=$1} END {if (NR > 0) print int(sum/NR); else print 0}')

    echo "Current Average CPU: $AVG_CPU% | Containers Running: $CONTAINER_COUNT"

    if [ "$AVG_CPU" -gt "$THRESHOLD_CPU" ]; then
        if [ "$CONTAINER_COUNT" -lt "$MAX_CONTAINERS" ]; then
            echo "Scaling up..."
            docker-compose up --scale backend=$((CONTAINER_COUNT + 1)) -d
        fi
    elif [ "$CONTAINER_COUNT" -gt "$MIN_CONTAINERS" ]; then
        echo "Scaling down..."
        docker rm -f $(docker ps -q --filter "name=backend" | tail -n 1)
    fi

    sleep 30  # Check every 30 seconds
done

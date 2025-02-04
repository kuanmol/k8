#!/bin/bash

SCALE_THRESHOLD=5  # Number of tasks to trigger scaling
MAX_WORKERS=5
MIN_WORKERS=1

while true; do
  PENDING_TASKS=$(docker exec $(docker ps -qf "name=redis") redis-cli LLEN tasks)
  RUNNING_WORKERS=$(docker ps -q --filter "ancestor=worker" | wc -l)

  echo "Pending Tasks: $PENDING_TASKS | Running Workers: $RUNNING_WORKERS"

  if [ "$PENDING_TASKS" -gt "$SCALE_THRESHOLD" ] && [ "$RUNNING_WORKERS" -lt "$MAX_WORKERS" ]; then
    echo "Scaling up..."
    docker-compose up -d --scale worker=$((RUNNING_WORKERS + 1))
  elif [ "$PENDING_TASKS" -le "$SCALE_THRESHOLD" ] && [ "$RUNNING_WORKERS" -gt "$MIN_WORKERS" ]; then
    echo "Scaling down..."
    docker-compose up -d --scale worker=$((RUNNING_WORKERS - 1))
  fi

  # Self-Healing
  for container in $(docker ps -q); do
    if [ "$(docker inspect -f '{{.State.Running}}' $container)" != "true" ]; then
      echo "Restarting failed container: $container"
      docker restart $container
    fi
  done

  sleep 10
done

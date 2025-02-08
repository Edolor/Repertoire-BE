#!/bin/bash
set -e

echo "Stopping running containers..."
cd /home/ec2-user/app || exit 1
sudo docker-compose -f docker-compose.prod.yml down || true

echo "Removing unused Docker images..."
sudo docker image prune -af || true

echo "Existing containers stopped and removed."
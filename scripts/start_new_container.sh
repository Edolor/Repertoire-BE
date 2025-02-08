#!/bin/bash
set -e

echo "Starting new deployment..."
cd /home/ec2-user/app || exit 1

echo "Building and starting Docker containers..."
sudo docker-compose -f docker-compose.prod.yml up --build -d

echo "Waiting for database to be ready..."
sleep 10  # Ensure PostgreSQL starts before running migrations

echo "Running Django migrations..."
sudo docker-compose -f docker-compose.prod.yml exec -T backend python manage.py migrate

echo "Collecting static files..."
sudo docker-compose -f docker-compose.prod.yml exec -T backend python manage.py collectstatic --noinput

echo "Restarting containers..."
sudo docker-compose -f docker-compose.prod.yml restart

echo "Deployment successful!"

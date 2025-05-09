#!/bin/bash
set -e

echo "Starting new deployment..."

echo "Executing fetch_env..."

cd /home/ec2-user/app/scripts
echo "Changing permission for dump_to_s3.sh"
chmod +x dump_to_s3.sh
echo "Successfully changed! Continuing..."

chmod +x fetch_env.sh  # Make script executable
./fetch_env.sh         # Generate .env file

mv /home/ec2-user/app/scripts/.env /home/ec2-user/app

echo "Completed fetch_env()... Continuing"

cd /home/ec2-user/app || exit 1

echo "Building and starting Docker containers..."

sudo docker-compose -f docker-compose.prod.yml up --build -d

echo "Waiting for database to be ready..."
sleep 10  # Ensure PostgreSQL starts before running migrations

echo "Restarting containers..."
sudo docker-compose -f docker-compose.prod.yml restart

echo "Deployment successful!"

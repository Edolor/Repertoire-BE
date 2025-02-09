#!/bin/bash
set -e  # Exit on error

echo "Updating package list..."
sudo yum update -y  # For Amazon Linux

echo "Installing Docker..."
sudo yum install -y docker

echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker  # Ensure Docker starts on reboot

echo "Installing Docker Compose..."
DOCKER_COMPOSE_VERSION="1.29.2"
sudo curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Docker and Docker Compose installed successfully!"

# Installing docker dependency
echo "Installing libxcrypt compat"
# 
yum install -y libxcrypt-compat

echo "libxcrypt compat installation complete!"

# Installing extra NGINX

# Fetch cloudflare details
aws s3 cp s3://menaportfolio/cloudflare/cloudflare.crt /etc/ssl/cloudflare/cloudflare.crt
aws s3 cp s3://menaportfolio/cloudflare/cloudflare.key /etc/ssl/cloudflare/cloudflare.key
aws s3 cp s3://menaportfolio/cloudflare/nginx.conf /etc/ssl/cloudflare/nginx.conf

# Setup cron details
# Path to the script and log file
echo "Installing crontab!"

sudo yum install cronie -y
sudo systemctl start crond
sudo systemctl enable crond

echo "Installation complete, setting up job!"


BASE_PATH="/home/ec2-user/app"

sudo chmod +x /home/ec2-user/app/scripts/dump_to_s3.sh
sudo chmod +r /home/ec2-user/app/scripts/dump_to_s3.sh

ls -la /home/ec2-user/app/scripts/

SCRIPT_PATH="$BASE_PATH/scripts/dump_to_s3.sh"
LOG_FILE="$BASE_PATH/scripts/dump_to_s3.log"

# Define the cron job command
CRON_JOB="*/5 * * * * $SCRIPT_PATH >> $LOG_FILE 2>&1"

# Check if the cron job already exists
(crontab -l | grep -q "$SCRIPT_PATH") && echo "Cron job already exists." || (
    # Add the cron job if it doesn't exist
    echo "Setting up the cron job to run every 5 minutes..."
    (crontab -l ; echo "$CRON_JOB") | crontab -
    echo "Cron job has been added successfully!"
)
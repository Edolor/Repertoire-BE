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
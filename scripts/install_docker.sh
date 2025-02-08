#!/bin/bash
set -e  # Exit on any error

echo "Updating package list..."
sudo yum update -y  # For Amazon Linux

echo "Installing Docker..."
sudo yum install -y docker

echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker  # Ensure Docker starts on reboot

echo "Checking if Docker Compose is installed..."
if ! command -v docker-compose &> /dev/null
then
    echo "Installing Docker Compose..."
    sudo yum install -y docker-compose-plugin
else
    echo "Docker Compose is already installed."
fi

echo "Verifying Docker and Docker Compose installation..."
docker --version
docker compose version

echo "Docker and Docker Compose installed successfully!"

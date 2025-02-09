#!/bin/bash
set -e  # Exit if any command fails

echo "Fetching environment variables from AWS SSM..."

# Replace these with your Parameter Store paths
aws ssm get-parameter --name "Portfolio" --with-decryption --query "Parameter.Value" --output text > .env

# Fetch initial database backup
aws s3 cp s3://menaportfolio/database/backup.json ../backup.json

# Fetch cloudflare details
aws s3 cp s3://menaportfolio/cloudflare/cloudflare.crt /etc/ssl/cloudflare/cloudflare.crt
aws s3 cp s3://menaportfolio/cloudflare/cloudflare.key /etc/ssl/cloudflare/cloudflare.key
aws s3 cp s3://menaportfolio/cloudflare/nginx.conf /etc/ssl/cloudflare/nginx.conf

echo ".env file created successfully!"

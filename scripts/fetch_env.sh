#!/bin/bash
set -e  # Exit if any command fails

echo "Fetching environment variables from AWS SSM..."

# Replace these with your Parameter Store paths
aws ssm get-parameter --name "Portfolio" --with-decryption --query "Parameter.Value" --output text > .env

# Fetch initial database backup
aws s3 cp s3://menaportfolio/database/backup.json ../backup.json
aws s3 cp s3://menaportfolio/database/db_backup.json ../db_backup.json

echo ".env file created successfully!"

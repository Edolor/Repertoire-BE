#!/bin/bash
set -e  # Exit if any command fails

echo "Fetching environment variables from AWS SSM..."

# Replace these with your Parameter Store paths
aws ssm get-parameter --name "Portfolio" --with-decryption --query "Parameter.Value" --output text > .env

echo ".env file created successfully!"

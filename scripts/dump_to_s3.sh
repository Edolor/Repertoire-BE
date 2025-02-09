#!/bin/bash
set -e

# Set environment variables
BASE_PATH="/home/ec2-user/app"
BACKUP_FILE="$BASE_PATH/web/db_backup.json"
FILE_NAME="db_backup.json"

# Run the dumpdata command inside the Docker container
sudo docker exec -i app_backend_1 python manage.py dumpdata --exclude=auth.group --exclude=auth.permission --exclude=contenttypes --output=/home/app/web/db_backup.json

sudo docker cp app_backend_1:/home/app/web/$FILE_NAME $BASE_PATH/$FILE_NAME

# Check if dumpdata was successful
if [ $? -eq 0 ]; then
    echo "Database dump successful. Uploading to S3..."

    # Upload the file to S3
    aws s3 cp $BASE_PATH/$FILE_NAME s3://menaportfolio/database/$FILE_NAME

    # Check if upload was successful
    if [ $? -eq 0 ]; then
        echo "Backup uploaded to S3 successfully."
    else
        echo "Error uploading to S3."
    fi
else
    echo "Error creating database dump."
fi

#!/bin/bash

python manage.py migrate auth
python manage.py migrate admin
python manage.py migrate sessions

python manage.py migrate

python manage.py loaddata backup.json

exec "$@"

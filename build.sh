#!/usr/bin/env bash
set -o errexit  # Exit on error

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Start Gunicorn server
exec gunicorn base.wsgi:application --bind 0.0.0.0:8000
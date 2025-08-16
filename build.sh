#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Ensure superuser exists and has staff privileges
python manage.py shell 
#!/usr/bin/env bash
set -o errexit  # exit on error if any command fails

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

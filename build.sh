#!/usr/bin/env bash
set -o errexit  # exit on error if any command fails

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

echo "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='xo_aniket.888').exists():
    User.objects.create_superuser('xo_aniket.888', 'xoaniket@example.com', 'areustupid')
" | python manage.py shell

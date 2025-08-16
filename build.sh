#!/usr/bin/env bash
set -o errexit  # exit on error if any command fails

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Create or update superuser automatically
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
user, created = User.objects.get_or_create(
    username='xo_aniket.888',
    defaults={'email': 'xoaniket@example.com'}
)
user.is_staff = True
user.is_superuser = True
user.set_password('areustupid')
user.save()
if created:
    print(f"Superuser '{user.username}' created successfully.")
else:
    print(f"Superuser '{user.username}' updated successfully.")
END

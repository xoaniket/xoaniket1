#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Ensure superuser exists and is staff
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
u, created = User.objects.get_or_create(username='eren001', defaults={'email':'eren2004@gmail.com','is_staff':True,'is_superuser':True}); \
if not created: \
    u.is_staff = True; u.is_superuser = True; u.save()" | python manage.py shell

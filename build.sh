#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='eren001').exists() or \
User.objects.create_superuser('admin', 'eren2004@gmail.com', '1234567xo')" | python manage.py shell

# create_superuser.py
from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# Try to get the user, or create if it doesn't exist
user, created = User.objects.get_or_create(
    username='xo_aniket.888',
    defaults={'email': 'xoaniket@gmail.com'}
)

# Ensure the user has staff and superuser privileges
user.is_staff = True
user.is_superuser = True

# Set or reset the password
user.set_password('areustupid')

# Save changes to the database
user.save()

# Output status
if created:
    print(f"Superuser '{user.username}' created successfully.")
else:
    print(f"Superuser '{user.username}' updated successfully.")

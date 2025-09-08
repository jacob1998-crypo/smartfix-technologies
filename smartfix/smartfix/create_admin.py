# smartfix/create_admin.py
from django.contrib.auth import get_user_model
import os

def create_admin():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser {username}...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print(f"Superuser {username} already exists.")

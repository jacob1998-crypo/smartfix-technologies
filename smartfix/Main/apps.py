from django.apps import AppConfig
from django.db.models.signals import post_migrate

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main'

    def ready(self):
        # Import here so it runs after Django is ready
        from smartfix.create_admin import create_admin
        # Run create_admin after migrations
        post_migrate.connect(lambda **kwargs: create_admin(), sender=self)

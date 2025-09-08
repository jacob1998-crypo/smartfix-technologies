from django.apps import AppConfig
from django.db.models.signals import post_migrate

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main'

    def ready(self):
        # Import create_admin inside ready() so it runs after Django is ready
        from smartfix.create_admin import create_admin

        # Define a function to run after all migrations
        def run_create_admin(sender, **kwargs):
            print("Running create_admin after migrations...")
            create_admin()

        # Connect to post_migrate without specifying sender
        post_migrate.connect(run_create_admin)

from django.apps import AppConfig


class EventsConfig(AppConfig):
    # The default auto field to use for models that don't have a field specified.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the app
    name = 'events'

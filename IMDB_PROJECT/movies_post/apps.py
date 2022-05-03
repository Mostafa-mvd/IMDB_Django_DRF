from django.apps import AppConfig


class MoviesPostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies_post'

    def ready(self):
        import movies_post.signals

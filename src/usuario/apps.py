from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'

    def ready(self):
        # Import signals to ensure they're registered
        try:
            from . import signals  # noqa: F401
        except Exception:
            pass

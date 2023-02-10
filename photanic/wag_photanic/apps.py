from django.apps import AppConfig


class WagPhotanicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wag_photanic'
    def read(self):
        import wag_photanic.signals
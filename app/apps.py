from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import app.signals
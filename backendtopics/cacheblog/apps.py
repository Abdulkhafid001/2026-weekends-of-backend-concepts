from django.apps import AppConfig


class CacheblogConfig(AppConfig):
    name = 'cacheblog'

    def ready(self):
        import cacheblog.signals
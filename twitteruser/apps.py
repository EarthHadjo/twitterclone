from django.apps import AppConfig


class TwitteruserConfig(AppConfig):
    name = 'twitteruser'


def ready(self):
    import twitteruser.signals


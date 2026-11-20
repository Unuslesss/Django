from django.apps import AppConfig


class Lect1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # type: ignore
    name = 'lect1'
    verbose_name = 'Учебный портал РЭУ им. Г.В. Плеханова'

from django.apps import AppConfig


class CrmUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_user'

    def ready(self):
        import crm_user.signals.handlers
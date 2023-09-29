from django.apps import AppConfig


from django.apps import AppConfig


class CustomerAccountsConfig(AppConfig):
    """
    AppConfig for the CustomerAccounts app.

    Attributes:
        default_auto_field: The default auto field for models.
        name: The name of the app.

    Methods:
        ready: A method called when the app is ready to import signals.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "customer_accounts"

    def ready(self):
        """
        Method called when the app is ready to import signals.
        """
        import customer_accounts.signals

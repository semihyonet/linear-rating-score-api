import django
from django.conf import settings
from api import settings as api_settings

settings.configure(
    DATABASES=api_settings.DATABASES,
    INSTALLED_APPS=api_settings.INSTALLED_APPS
)

django.setup()

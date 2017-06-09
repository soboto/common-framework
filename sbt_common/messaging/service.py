
from ..utils import import_class
from ..settings import api_settings


class Service(object):
    service_name = None
    provider = None

    """docstring for Service"""
    def __init__(self, service_name, *args, **kwargs):
        self.service_name = service_name

        provider_class = import_class(api_settings.MESSAGE_SERVICE_PROVIDER)
        self.provider = provider_class(service=self)

    def get_info(self):
        if self.service_name not in api_settings.SERVICES:
            return {}

        return api_settings.SERVICES.get(self.service_name)

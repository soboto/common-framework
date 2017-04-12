from functools import partial


class BaseProvider(object):
    _service = None
    service_info = {}

    """docstring for BaseProvider"""
    def __init__(self, service, *args, **kwargs):
        self._service = service

        self.service_info = self._service.get_info()

    @property
    def service(self):
        return self._service

    def get_service_host(self):
        return self.service_info.get('host', None)

    def execute_message(self, *args, **attrs):
        raise NotImplementedError()

    def bind_service_events(self, events=[], **args):
        for event in events:
            setattr(self._service, event, partial(self.execute_message, event))

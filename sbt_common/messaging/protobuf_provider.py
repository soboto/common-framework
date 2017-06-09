import time
from grpc.beta import implementations

from .base_provider import BaseProvider
from ..utils import import_class
from ..settings import api_settings

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_PROTO_GENERATED_PATH = 'sbt_common.protobuf.generated'


class ProtobufProvider(BaseProvider):
    _protobuf_service = None
    _module = None
    _stub = None

    """docstring for ProtobufProvider"""
    def __init__(self, service, *args, **kwargs):
        super(ProtobufProvider, self).__init__(service, *args, **kwargs)

        self._module = self.service_info.get('module')
        self._stub = self.service_info.get('stub')

        channel = implementations.insecure_channel(self.get_service_host(), api_settings.DEFAULT_GRPC_PORT)
        stub_class = self.get_stub_class()

        self._protobuf_service = stub_class(channel)

        events = self._protobuf_service._cardinalities.keys()
        self.bind_service_events(events)

    def get_module(self):
        return '{0}.{1}'.format(_PROTO_GENERATED_PATH, str(self._module))

    def get_stub_class(self):
        return import_class('{0}.{1}'.format(self.get_module(), self._stub))

    def get_message_request_class(self, message):
        class_name = message + 'Request'
        tries = 0
        while (tries < 2):
            try:
                if tries == 0:
                    class_to_import = ''.join(s[0].upper() + s[1:] for s in class_name.split(' '))
                elif tries == 1:
                    class_to_import = ''.join(s[0].lower() + s[1:] for s in class_name.split(' '))

                return import_class('{0}.{1}'.format(self.get_module(), class_to_import))
            except Exception:
                pass
            tries = tries + 1

        return

    def execute_message(self, message, *args, **attrs):
        request = self.get_message_request_class(message)
        service_call = getattr(self._protobuf_service, message)

        params = {}
        if len(args) > 0:
            params = args[0]

        return service_call(request(**params), api_settings.DEFAULT_GRPC_TIMEOUT)


def create_protobuf_service(service_name, local_service_class):
    try:
        import django
        django.setup()
    except Exception as e:
        print e
        pass

    service_info = api_settings.SERVICES.get(service_name)

    protobuf_service_class = '{0}.{1}.{2}'.format(
        _PROTO_GENERATED_PATH, str(service_info.get('module')), str(service_info.get('pb_service')))

    protobuf_service = import_class(protobuf_service_class)
    local_service = import_class(local_service_class)
    service = protobuf_service(local_service())
    service.add_insecure_port('[::]:{}'.format(api_settings.DEFAULT_GRPC_PORT))
    service.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        service.stop(0)

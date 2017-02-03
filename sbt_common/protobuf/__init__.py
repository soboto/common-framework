"""The Python implementation of the GRPC server."""

import time
from sbt_common.utils import import_class
from sbt_common.settings import api_settings
from grpc.beta import implementations


_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_PROTO_GENERATED_PATH = 'sbt_common.protobuf.generated.'


def start_proto_server(proto_server_class, service_class):
    try:
        import django
        django.setup()
    except:
        pass

    service = import_class(service_class)

    server = proto_server_class(service())
    server.add_insecure_port('[::]:{}'.format(api_settings.DEFAULT_GRPC_PORT))
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


def _get_service(service_url, service_class):
    channel = implementations.insecure_channel(service_url, api_settings.DEFAULT_GRPC_PORT)

    stub = import_class(_PROTO_GENERATED_PATH + service_class)
    service = stub(channel)

    return service


class ProtoService(object):
    proto_service = None

    def __init__(self, service_url, service_class):
        self.proto_service = _get_service(service_url, service_class)

    def execute(self, method, request_class, message={}):

        request = import_class(_PROTO_GENERATED_PATH + request_class)
        service_call = getattr(self.proto_service, method)

        return service_call(request(**message), 60)

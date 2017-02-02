"""The Python implementation of the GRPC server."""

import time
from sbt_common.utils import import_class
from sbt_common.settings import api_settings

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


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

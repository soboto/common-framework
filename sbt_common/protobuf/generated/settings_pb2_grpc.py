import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import settings_pb2 as settings__pb2
import settings_pb2 as settings__pb2


class SettingsServiceStub(object):
  """=======================================
  The service definition.
  =======================================

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getSettings = channel.unary_unary(
        '/soboto.settings.SettingsService/getSettings',
        request_serializer=settings__pb2.SettingsInfoRequest.SerializeToString,
        response_deserializer=settings__pb2.SettingsInfoResponse.FromString,
        )


class SettingsServiceServicer(object):
  """=======================================
  The service definition.
  =======================================

  """

  def getSettings(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SettingsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getSettings': grpc.unary_unary_rpc_method_handler(
          servicer.getSettings,
          request_deserializer=settings__pb2.SettingsInfoRequest.FromString,
          response_serializer=settings__pb2.SettingsInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.settings.SettingsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

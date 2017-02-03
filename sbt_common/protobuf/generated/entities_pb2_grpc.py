import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import entities_pb2 as entities__pb2
import entities_pb2 as entities__pb2


class EntitiesServiceStub(object):
  """=======================================
  The service definition.
  =======================================

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getEntityInfo = channel.unary_unary(
        '/soboto.entities.EntitiesService/getEntityInfo',
        request_serializer=entities__pb2.EntityInfoRequest.SerializeToString,
        response_deserializer=entities__pb2.EntityInfoResponse.FromString,
        )


class EntitiesServiceServicer(object):
  """=======================================
  The service definition.
  =======================================

  """

  def getEntityInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EntitiesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getEntityInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getEntityInfo,
          request_deserializer=entities__pb2.EntityInfoRequest.FromString,
          response_serializer=entities__pb2.EntityInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.entities.EntitiesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

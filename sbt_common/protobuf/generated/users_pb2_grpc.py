import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import users_pb2 as users__pb2
import users_pb2 as users__pb2


class UsersServiceStub(object):
  """The service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ValidateAuthenticationToken = channel.unary_unary(
        '/soboto.users.UsersService/ValidateAuthenticationToken',
        request_serializer=users__pb2.ValidateAuthenticationTokenRequest.SerializeToString,
        response_deserializer=users__pb2.ValidateAuthenticationTokenResponse.FromString,
        )


class UsersServiceServicer(object):
  """The service definition.
  """

  def ValidateAuthenticationToken(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ValidateAuthenticationToken': grpc.unary_unary_rpc_method_handler(
          servicer.ValidateAuthenticationToken,
          request_deserializer=users__pb2.ValidateAuthenticationTokenRequest.FromString,
          response_serializer=users__pb2.ValidateAuthenticationTokenResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.users.UsersService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2
import users_pb2 as users__pb2


class UsersServiceStub(object):
  """=======================================
  The service definition.
  =======================================
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.validateAuthenticationToken = channel.unary_unary(
        '/soboto.users.UsersService/validateAuthenticationToken',
        request_serializer=users__pb2.ValidateAuthenticationTokenRequest.SerializeToString,
        response_deserializer=users__pb2.ValidateAuthenticationTokenResponse.FromString,
        )
    self.getUserPermissions = channel.unary_unary(
        '/soboto.users.UsersService/getUserPermissions',
        request_serializer=users__pb2.GetUserPermissionsRequest.SerializeToString,
        response_deserializer=users__pb2.GetUserPermissionsResponse.FromString,
        )
    self.getBOUserInfo = channel.unary_unary(
        '/soboto.users.UsersService/getBOUserInfo',
        request_serializer=users__pb2.GetBOUserInfoRequest.SerializeToString,
        response_deserializer=users__pb2.GetBOUserInfoResponse.FromString,
        )
    self.getCustomerInfo = channel.unary_unary(
        '/soboto.users.UsersService/getCustomerInfo',
        request_serializer=users__pb2.GetCustomerInfoRequest.SerializeToString,
        response_deserializer=users__pb2.GetCustomerInfoResponse.FromString,
        )


class UsersServiceServicer(object):
  """=======================================
  The service definition.
  =======================================
  """

  def validateAuthenticationToken(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUserPermissions(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getBOUserInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCustomerInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'validateAuthenticationToken': grpc.unary_unary_rpc_method_handler(
          servicer.validateAuthenticationToken,
          request_deserializer=users__pb2.ValidateAuthenticationTokenRequest.FromString,
          response_serializer=users__pb2.ValidateAuthenticationTokenResponse.SerializeToString,
      ),
      'getUserPermissions': grpc.unary_unary_rpc_method_handler(
          servicer.getUserPermissions,
          request_deserializer=users__pb2.GetUserPermissionsRequest.FromString,
          response_serializer=users__pb2.GetUserPermissionsResponse.SerializeToString,
      ),
      'getBOUserInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getBOUserInfo,
          request_deserializer=users__pb2.GetBOUserInfoRequest.FromString,
          response_serializer=users__pb2.GetBOUserInfoResponse.SerializeToString,
      ),
      'getCustomerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getCustomerInfo,
          request_deserializer=users__pb2.GetCustomerInfoRequest.FromString,
          response_serializer=users__pb2.GetCustomerInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.users.UsersService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

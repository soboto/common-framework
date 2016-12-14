import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import files_pb2 as files__pb2
import files_pb2 as files__pb2


class FilesServiceStub(object):
  """The service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FetchMedia = channel.unary_unary(
        '/soboto.files.FilesService/FetchMedia',
        request_serializer=files__pb2.FetchMediaRequest.SerializeToString,
        response_deserializer=files__pb2.FetchMediaResponse.FromString,
        )


class FilesServiceServicer(object):
  """The service definition
  """

  def FetchMedia(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FilesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FetchMedia': grpc.unary_unary_rpc_method_handler(
          servicer.FetchMedia,
          request_deserializer=files__pb2.FetchMediaRequest.FromString,
          response_serializer=files__pb2.FetchMediaResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.files.FilesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

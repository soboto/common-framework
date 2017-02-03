import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import bookings_pb2 as bookings__pb2
import bookings_pb2 as bookings__pb2


class BookingsServiceStub(object):
  """=======================================
  The service definition.
  =======================================

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getBookingInfo = channel.unary_unary(
        '/soboto.bookings.BookingsService/getBookingInfo',
        request_serializer=bookings__pb2.BookingInfoRequest.SerializeToString,
        response_deserializer=bookings__pb2.BookingInfoResponse.FromString,
        )


class BookingsServiceServicer(object):
  """=======================================
  The service definition.
  =======================================

  """

  def getBookingInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BookingsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getBookingInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getBookingInfo,
          request_deserializer=bookings__pb2.BookingInfoRequest.FromString,
          response_serializer=bookings__pb2.BookingInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.bookings.BookingsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

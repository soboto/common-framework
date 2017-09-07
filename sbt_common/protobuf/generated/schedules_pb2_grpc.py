import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import schedules_pb2 as schedules__pb2
import schedules_pb2 as schedules__pb2
import schedules_pb2 as schedules__pb2
import schedules_pb2 as schedules__pb2
import schedules_pb2 as schedules__pb2
import schedules_pb2 as schedules__pb2


class SchedulesServiceStub(object):
  """=======================================
  The service definition.
  =======================================

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.checkSlotAvailability = channel.unary_unary(
        '/soboto.schedules.SchedulesService/checkSlotAvailability',
        request_serializer=schedules__pb2.CheckSlotAvailabilityRequest.SerializeToString,
        response_deserializer=schedules__pb2.CheckSlotAvailabilityResponse.FromString,
        )
    self.incrementSlotAvailability = channel.unary_unary(
        '/soboto.schedules.SchedulesService/incrementSlotAvailability',
        request_serializer=schedules__pb2.IncrementSlotAvailabilityRequest.SerializeToString,
        response_deserializer=schedules__pb2.IncrementSlotAvailabilityResponse.FromString,
        )
    self.getSlotInfo = channel.unary_unary(
        '/soboto.schedules.SchedulesService/getSlotInfo',
        request_serializer=schedules__pb2.GetSlotInfoRequest.SerializeToString,
        response_deserializer=schedules__pb2.GetSlotInfoResponse.FromString,
        )


class SchedulesServiceServicer(object):
  """=======================================
  The service definition.
  =======================================

  """

  def checkSlotAvailability(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def incrementSlotAvailability(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getSlotInfo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SchedulesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'checkSlotAvailability': grpc.unary_unary_rpc_method_handler(
          servicer.checkSlotAvailability,
          request_deserializer=schedules__pb2.CheckSlotAvailabilityRequest.FromString,
          response_serializer=schedules__pb2.CheckSlotAvailabilityResponse.SerializeToString,
      ),
      'incrementSlotAvailability': grpc.unary_unary_rpc_method_handler(
          servicer.incrementSlotAvailability,
          request_deserializer=schedules__pb2.IncrementSlotAvailabilityRequest.FromString,
          response_serializer=schedules__pb2.IncrementSlotAvailabilityResponse.SerializeToString,
      ),
      'getSlotInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getSlotInfo,
          request_deserializer=schedules__pb2.GetSlotInfoRequest.FromString,
          response_serializer=schedules__pb2.GetSlotInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.schedules.SchedulesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

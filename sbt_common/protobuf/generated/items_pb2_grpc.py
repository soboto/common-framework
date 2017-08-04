import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2
import items_pb2 as items__pb2


class ItemsServiceStub(object):
  """=======================================
  The service definition.
  =======================================

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.checkEventAvailability = channel.unary_unary(
        '/soboto.items.ItemsService/checkEventAvailability',
        request_serializer=items__pb2.CheckEventAvailabilityRequest.SerializeToString,
        response_deserializer=items__pb2.CheckEventAvailabilityResponse.FromString,
        )
    self.duplicateItemEvent = channel.unary_unary(
        '/soboto.items.ItemsService/duplicateItemEvent',
        request_serializer=items__pb2.DuplicateItemEventRequest.SerializeToString,
        response_deserializer=items__pb2.DuplicateItemEventResponse.FromString,
        )
    self.getEntitiesItems = channel.unary_unary(
        '/soboto.items.ItemsService/getEntitiesItems',
        request_serializer=items__pb2.GetEntitiesItemsRequest.SerializeToString,
        response_deserializer=items__pb2.GetEntitiesItemsResponse.FromString,
        )
    self.updateItemsBilling = channel.unary_unary(
        '/soboto.items.ItemsService/updateItemsBilling',
        request_serializer=items__pb2.UpdateItemsBillingRequest.SerializeToString,
        response_deserializer=items__pb2.UpdateItemsBillingResponse.FromString,
        )


class ItemsServiceServicer(object):
  """=======================================
  The service definition.
  =======================================

  """

  def checkEventAvailability(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def duplicateItemEvent(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getEntitiesItems(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateItemsBilling(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ItemsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'checkEventAvailability': grpc.unary_unary_rpc_method_handler(
          servicer.checkEventAvailability,
          request_deserializer=items__pb2.CheckEventAvailabilityRequest.FromString,
          response_serializer=items__pb2.CheckEventAvailabilityResponse.SerializeToString,
      ),
      'duplicateItemEvent': grpc.unary_unary_rpc_method_handler(
          servicer.duplicateItemEvent,
          request_deserializer=items__pb2.DuplicateItemEventRequest.FromString,
          response_serializer=items__pb2.DuplicateItemEventResponse.SerializeToString,
      ),
      'getEntitiesItems': grpc.unary_unary_rpc_method_handler(
          servicer.getEntitiesItems,
          request_deserializer=items__pb2.GetEntitiesItemsRequest.FromString,
          response_serializer=items__pb2.GetEntitiesItemsResponse.SerializeToString,
      ),
      'updateItemsBilling': grpc.unary_unary_rpc_method_handler(
          servicer.updateItemsBilling,
          request_deserializer=items__pb2.UpdateItemsBillingRequest.FromString,
          response_serializer=items__pb2.UpdateItemsBillingResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'soboto.items.ItemsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

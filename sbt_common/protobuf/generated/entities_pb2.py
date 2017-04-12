# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entities.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='entities.proto',
  package='soboto.entities',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x65ntities.proto\x12\x0fsoboto.entities\"\x16\n\x05Phone\x12\r\n\x05value\x18\x01 \x01(\t\"\x16\n\x05\x45mail\x12\r\n\x05value\x18\x01 \x01(\t\"\xb7\x02\n\x06\x45ntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\x0c\n\x04\x63ity\x18\x06 \x01(\t\x12\x11\n\tpost_code\x18\x07 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x08 \x01(\t\x12\x10\n\x08timezone\x18\t \x01(\t\x12\r\n\x05phone\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x0f\n\x07website\x18\x0c \x01(\t\x12\x32\n\x12\x61lternative_phones\x18\r \x03(\x0b\x32\x16.soboto.entities.Phone\x12\x32\n\x12\x61lternative_emails\x18\x0e \x03(\x0b\x32\x16.soboto.entities.Email\"\"\n\x14GetEntityInfoRequest\x12\n\n\x02id\x18\x01 \x01(\t\"@\n\x15GetEntityInfoResponse\x12\'\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x17.soboto.entities.Entity2s\n\x0f\x45ntitiesService\x12`\n\rgetEntityInfo\x12%.soboto.entities.GetEntityInfoRequest\x1a&.soboto.entities.GetEntityInfoResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PHONE = _descriptor.Descriptor(
  name='Phone',
  full_name='soboto.entities.Phone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='soboto.entities.Phone.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=57,
)


_EMAIL = _descriptor.Descriptor(
  name='Email',
  full_name='soboto.entities.Email',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='soboto.entities.Email.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=81,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='soboto.entities.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.entities.Entity.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alias', full_name='soboto.entities.Entity.alias', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='soboto.entities.Entity.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='soboto.entities.Entity.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='soboto.entities.Entity.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='soboto.entities.Entity.city', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_code', full_name='soboto.entities.Entity.post_code', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='soboto.entities.Entity.country_code', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='soboto.entities.Entity.timezone', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='soboto.entities.Entity.phone', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='soboto.entities.Entity.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='website', full_name='soboto.entities.Entity.website', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternative_phones', full_name='soboto.entities.Entity.alternative_phones', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alternative_emails', full_name='soboto.entities.Entity.alternative_emails', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=395,
)


_GETENTITYINFOREQUEST = _descriptor.Descriptor(
  name='GetEntityInfoRequest',
  full_name='soboto.entities.GetEntityInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.entities.GetEntityInfoRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=431,
)


_GETENTITYINFORESPONSE = _descriptor.Descriptor(
  name='GetEntityInfoResponse',
  full_name='soboto.entities.GetEntityInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='soboto.entities.GetEntityInfoResponse.entity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=497,
)

_ENTITY.fields_by_name['alternative_phones'].message_type = _PHONE
_ENTITY.fields_by_name['alternative_emails'].message_type = _EMAIL
_GETENTITYINFORESPONSE.fields_by_name['entity'].message_type = _ENTITY
DESCRIPTOR.message_types_by_name['Phone'] = _PHONE
DESCRIPTOR.message_types_by_name['Email'] = _EMAIL
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['GetEntityInfoRequest'] = _GETENTITYINFOREQUEST
DESCRIPTOR.message_types_by_name['GetEntityInfoResponse'] = _GETENTITYINFORESPONSE

Phone = _reflection.GeneratedProtocolMessageType('Phone', (_message.Message,), dict(
  DESCRIPTOR = _PHONE,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:soboto.entities.Phone)
  ))
_sym_db.RegisterMessage(Phone)

Email = _reflection.GeneratedProtocolMessageType('Email', (_message.Message,), dict(
  DESCRIPTOR = _EMAIL,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:soboto.entities.Email)
  ))
_sym_db.RegisterMessage(Email)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), dict(
  DESCRIPTOR = _ENTITY,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:soboto.entities.Entity)
  ))
_sym_db.RegisterMessage(Entity)

GetEntityInfoRequest = _reflection.GeneratedProtocolMessageType('GetEntityInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETENTITYINFOREQUEST,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:soboto.entities.GetEntityInfoRequest)
  ))
_sym_db.RegisterMessage(GetEntityInfoRequest)

GetEntityInfoResponse = _reflection.GeneratedProtocolMessageType('GetEntityInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETENTITYINFORESPONSE,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:soboto.entities.GetEntityInfoResponse)
  ))
_sym_db.RegisterMessage(GetEntityInfoResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


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
          request_serializer=GetEntityInfoRequest.SerializeToString,
          response_deserializer=GetEntityInfoResponse.FromString,
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
            request_deserializer=GetEntityInfoRequest.FromString,
            response_serializer=GetEntityInfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'soboto.entities.EntitiesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaEntitiesServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """=======================================
    The service definition.
    =======================================

    """
    def getEntityInfo(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaEntitiesServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """=======================================
    The service definition.
    =======================================

    """
    def getEntityInfo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    getEntityInfo.future = None


  def beta_create_EntitiesService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('soboto.entities.EntitiesService', 'getEntityInfo'): GetEntityInfoRequest.FromString,
    }
    response_serializers = {
      ('soboto.entities.EntitiesService', 'getEntityInfo'): GetEntityInfoResponse.SerializeToString,
    }
    method_implementations = {
      ('soboto.entities.EntitiesService', 'getEntityInfo'): face_utilities.unary_unary_inline(servicer.getEntityInfo),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_EntitiesService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('soboto.entities.EntitiesService', 'getEntityInfo'): GetEntityInfoRequest.SerializeToString,
    }
    response_deserializers = {
      ('soboto.entities.EntitiesService', 'getEntityInfo'): GetEntityInfoResponse.FromString,
    }
    cardinalities = {
      'getEntityInfo': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'soboto.entities.EntitiesService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)

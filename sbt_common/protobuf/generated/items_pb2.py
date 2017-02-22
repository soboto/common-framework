# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: items.proto

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
  name='items.proto',
  package='soboto.items',
  syntax='proto3',
  serialized_pb=_b('\n\x0bitems.proto\x12\x0csoboto.items\":\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x05\x12\x12\n\nupdated_at\x18\x03 \x01(\x05\"\xf1\x01\n\tItemEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nstart_time\x18\x04 \x01(\x05\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x05\x12\x14\n\x0cmin_quantity\x18\x06 \x01(\x05\x12\x14\n\x0cmax_quantity\x18\x07 \x01(\x05\x12\x0f\n\x07\x61ll_day\x18\x08 \x01(\x08\x12 \n\x04item\x18\t \x01(\x0b\x32\x12.soboto.items.Item\x12\x30\n\rprice_options\x18\n \x03(\x0b\x32\x19.soboto.items.PriceOption\"\x81\x01\n\x0bPriceOption\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x10\n\x08required\x18\x03 \x01(\x08\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x37\n\x10participant_type\x18\x05 \x01(\x0b\x32\x1d.soboto.items.ParticipantType\",\n\x0fParticipantType\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"4\n\x14SlotEventParticipant\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"\x93\x01\n\tSlotEvent\x12\x0f\n\x07slot_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x03 \x01(\x05\x12\x17\n\x0f\x62ooked_quantity\x18\x04 \x01(\x05\x12\x38\n\x0cparticipants\x18\x05 \x03(\x0b\x32\".soboto.items.SlotEventParticipant\"J\n\x15SlotEventAvailability\x12\x0f\n\x07slot_id\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\t\"L\n\x1d\x43heckEventAvailabilityRequest\x12+\n\ntime_slots\x18\x01 \x03(\x0b\x32\x17.soboto.items.SlotEvent\"Y\n\x1e\x43heckEventAvailabilityResponse\x12\x37\n\ntime_slots\x18\x01 \x03(\x0b\x32#.soboto.items.SlotEventAvailability\"I\n\x19\x44uplicateItemEventRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\"I\n\x1a\x44uplicateItemEventResponse\x12+\n\nitem_event\x18\x01 \x01(\x0b\x32\x17.soboto.items.ItemEvent2\xf0\x01\n\x0cItemsService\x12u\n\x16\x63heckEventAvailability\x12+.soboto.items.CheckEventAvailabilityRequest\x1a,.soboto.items.CheckEventAvailabilityResponse\"\x00\x12i\n\x12\x64uplicateItemEvent\x12\'.soboto.items.DuplicateItemEventRequest\x1a(.soboto.items.DuplicateItemEventResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='soboto.items.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.items.Item.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='soboto.items.Item.created_at', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='soboto.items.Item.updated_at', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=29,
  serialized_end=87,
)


_ITEMEVENT = _descriptor.Descriptor(
  name='ItemEvent',
  full_name='soboto.items.ItemEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.items.ItemEvent.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='soboto.items.ItemEvent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='soboto.items.ItemEvent.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='soboto.items.ItemEvent.start_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='soboto.items.ItemEvent.end_time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_quantity', full_name='soboto.items.ItemEvent.min_quantity', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_quantity', full_name='soboto.items.ItemEvent.max_quantity', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_day', full_name='soboto.items.ItemEvent.all_day', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='soboto.items.ItemEvent.item', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_options', full_name='soboto.items.ItemEvent.price_options', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=90,
  serialized_end=331,
)


_PRICEOPTION = _descriptor.Descriptor(
  name='PriceOption',
  full_name='soboto.items.PriceOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.items.PriceOption.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='soboto.items.PriceOption.price', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required', full_name='soboto.items.PriceOption.required', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='soboto.items.PriceOption.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='participant_type', full_name='soboto.items.PriceOption.participant_type', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=334,
  serialized_end=463,
)


_PARTICIPANTTYPE = _descriptor.Descriptor(
  name='ParticipantType',
  full_name='soboto.items.ParticipantType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.items.ParticipantType.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='soboto.items.ParticipantType.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=465,
  serialized_end=509,
)


_SLOTEVENTPARTICIPANT = _descriptor.Descriptor(
  name='SlotEventParticipant',
  full_name='soboto.items.SlotEventParticipant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='soboto.items.SlotEventParticipant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='soboto.items.SlotEventParticipant.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=511,
  serialized_end=563,
)


_SLOTEVENT = _descriptor.Descriptor(
  name='SlotEvent',
  full_name='soboto.items.SlotEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='soboto.items.SlotEvent.slot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='soboto.items.SlotEvent.event_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='soboto.items.SlotEvent.datetime', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='booked_quantity', full_name='soboto.items.SlotEvent.booked_quantity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='participants', full_name='soboto.items.SlotEvent.participants', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=566,
  serialized_end=713,
)


_SLOTEVENTAVAILABILITY = _descriptor.Descriptor(
  name='SlotEventAvailability',
  full_name='soboto.items.SlotEventAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='soboto.items.SlotEventAvailability.slot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='soboto.items.SlotEventAvailability.datetime', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='soboto.items.SlotEventAvailability.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=715,
  serialized_end=789,
)


_CHECKEVENTAVAILABILITYREQUEST = _descriptor.Descriptor(
  name='CheckEventAvailabilityRequest',
  full_name='soboto.items.CheckEventAvailabilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_slots', full_name='soboto.items.CheckEventAvailabilityRequest.time_slots', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=791,
  serialized_end=867,
)


_CHECKEVENTAVAILABILITYRESPONSE = _descriptor.Descriptor(
  name='CheckEventAvailabilityResponse',
  full_name='soboto.items.CheckEventAvailabilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_slots', full_name='soboto.items.CheckEventAvailabilityResponse.time_slots', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=869,
  serialized_end=958,
)


_DUPLICATEITEMEVENTREQUEST = _descriptor.Descriptor(
  name='DuplicateItemEventRequest',
  full_name='soboto.items.DuplicateItemEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_id', full_name='soboto.items.DuplicateItemEventRequest.event_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='soboto.items.DuplicateItemEventRequest.start', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='soboto.items.DuplicateItemEventRequest.end', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=960,
  serialized_end=1033,
)


_DUPLICATEITEMEVENTRESPONSE = _descriptor.Descriptor(
  name='DuplicateItemEventResponse',
  full_name='soboto.items.DuplicateItemEventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_event', full_name='soboto.items.DuplicateItemEventResponse.item_event', index=0,
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
  serialized_start=1035,
  serialized_end=1108,
)

_ITEMEVENT.fields_by_name['item'].message_type = _ITEM
_ITEMEVENT.fields_by_name['price_options'].message_type = _PRICEOPTION
_PRICEOPTION.fields_by_name['participant_type'].message_type = _PARTICIPANTTYPE
_SLOTEVENT.fields_by_name['participants'].message_type = _SLOTEVENTPARTICIPANT
_CHECKEVENTAVAILABILITYREQUEST.fields_by_name['time_slots'].message_type = _SLOTEVENT
_CHECKEVENTAVAILABILITYRESPONSE.fields_by_name['time_slots'].message_type = _SLOTEVENTAVAILABILITY
_DUPLICATEITEMEVENTRESPONSE.fields_by_name['item_event'].message_type = _ITEMEVENT
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemEvent'] = _ITEMEVENT
DESCRIPTOR.message_types_by_name['PriceOption'] = _PRICEOPTION
DESCRIPTOR.message_types_by_name['ParticipantType'] = _PARTICIPANTTYPE
DESCRIPTOR.message_types_by_name['SlotEventParticipant'] = _SLOTEVENTPARTICIPANT
DESCRIPTOR.message_types_by_name['SlotEvent'] = _SLOTEVENT
DESCRIPTOR.message_types_by_name['SlotEventAvailability'] = _SLOTEVENTAVAILABILITY
DESCRIPTOR.message_types_by_name['CheckEventAvailabilityRequest'] = _CHECKEVENTAVAILABILITYREQUEST
DESCRIPTOR.message_types_by_name['CheckEventAvailabilityResponse'] = _CHECKEVENTAVAILABILITYRESPONSE
DESCRIPTOR.message_types_by_name['DuplicateItemEventRequest'] = _DUPLICATEITEMEVENTREQUEST
DESCRIPTOR.message_types_by_name['DuplicateItemEventResponse'] = _DUPLICATEITEMEVENTRESPONSE

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.Item)
  ))
_sym_db.RegisterMessage(Item)

ItemEvent = _reflection.GeneratedProtocolMessageType('ItemEvent', (_message.Message,), dict(
  DESCRIPTOR = _ITEMEVENT,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.ItemEvent)
  ))
_sym_db.RegisterMessage(ItemEvent)

PriceOption = _reflection.GeneratedProtocolMessageType('PriceOption', (_message.Message,), dict(
  DESCRIPTOR = _PRICEOPTION,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.PriceOption)
  ))
_sym_db.RegisterMessage(PriceOption)

ParticipantType = _reflection.GeneratedProtocolMessageType('ParticipantType', (_message.Message,), dict(
  DESCRIPTOR = _PARTICIPANTTYPE,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.ParticipantType)
  ))
_sym_db.RegisterMessage(ParticipantType)

SlotEventParticipant = _reflection.GeneratedProtocolMessageType('SlotEventParticipant', (_message.Message,), dict(
  DESCRIPTOR = _SLOTEVENTPARTICIPANT,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.SlotEventParticipant)
  ))
_sym_db.RegisterMessage(SlotEventParticipant)

SlotEvent = _reflection.GeneratedProtocolMessageType('SlotEvent', (_message.Message,), dict(
  DESCRIPTOR = _SLOTEVENT,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.SlotEvent)
  ))
_sym_db.RegisterMessage(SlotEvent)

SlotEventAvailability = _reflection.GeneratedProtocolMessageType('SlotEventAvailability', (_message.Message,), dict(
  DESCRIPTOR = _SLOTEVENTAVAILABILITY,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.SlotEventAvailability)
  ))
_sym_db.RegisterMessage(SlotEventAvailability)

CheckEventAvailabilityRequest = _reflection.GeneratedProtocolMessageType('CheckEventAvailabilityRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKEVENTAVAILABILITYREQUEST,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.CheckEventAvailabilityRequest)
  ))
_sym_db.RegisterMessage(CheckEventAvailabilityRequest)

CheckEventAvailabilityResponse = _reflection.GeneratedProtocolMessageType('CheckEventAvailabilityResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKEVENTAVAILABILITYRESPONSE,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.CheckEventAvailabilityResponse)
  ))
_sym_db.RegisterMessage(CheckEventAvailabilityResponse)

DuplicateItemEventRequest = _reflection.GeneratedProtocolMessageType('DuplicateItemEventRequest', (_message.Message,), dict(
  DESCRIPTOR = _DUPLICATEITEMEVENTREQUEST,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.DuplicateItemEventRequest)
  ))
_sym_db.RegisterMessage(DuplicateItemEventRequest)

DuplicateItemEventResponse = _reflection.GeneratedProtocolMessageType('DuplicateItemEventResponse', (_message.Message,), dict(
  DESCRIPTOR = _DUPLICATEITEMEVENTRESPONSE,
  __module__ = 'items_pb2'
  # @@protoc_insertion_point(class_scope:soboto.items.DuplicateItemEventResponse)
  ))
_sym_db.RegisterMessage(DuplicateItemEventResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


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
          request_serializer=CheckEventAvailabilityRequest.SerializeToString,
          response_deserializer=CheckEventAvailabilityResponse.FromString,
          )
      self.duplicateItemEvent = channel.unary_unary(
          '/soboto.items.ItemsService/duplicateItemEvent',
          request_serializer=DuplicateItemEventRequest.SerializeToString,
          response_deserializer=DuplicateItemEventResponse.FromString,
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


  def add_ItemsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'checkEventAvailability': grpc.unary_unary_rpc_method_handler(
            servicer.checkEventAvailability,
            request_deserializer=CheckEventAvailabilityRequest.FromString,
            response_serializer=CheckEventAvailabilityResponse.SerializeToString,
        ),
        'duplicateItemEvent': grpc.unary_unary_rpc_method_handler(
            servicer.duplicateItemEvent,
            request_deserializer=DuplicateItemEventRequest.FromString,
            response_serializer=DuplicateItemEventResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'soboto.items.ItemsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaItemsServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """=======================================
    The service definition.
    =======================================

    """
    def checkEventAvailability(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def duplicateItemEvent(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaItemsServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """=======================================
    The service definition.
    =======================================

    """
    def checkEventAvailability(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    checkEventAvailability.future = None
    def duplicateItemEvent(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    duplicateItemEvent.future = None


  def beta_create_ItemsService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('soboto.items.ItemsService', 'checkEventAvailability'): CheckEventAvailabilityRequest.FromString,
      ('soboto.items.ItemsService', 'duplicateItemEvent'): DuplicateItemEventRequest.FromString,
    }
    response_serializers = {
      ('soboto.items.ItemsService', 'checkEventAvailability'): CheckEventAvailabilityResponse.SerializeToString,
      ('soboto.items.ItemsService', 'duplicateItemEvent'): DuplicateItemEventResponse.SerializeToString,
    }
    method_implementations = {
      ('soboto.items.ItemsService', 'checkEventAvailability'): face_utilities.unary_unary_inline(servicer.checkEventAvailability),
      ('soboto.items.ItemsService', 'duplicateItemEvent'): face_utilities.unary_unary_inline(servicer.duplicateItemEvent),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_ItemsService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('soboto.items.ItemsService', 'checkEventAvailability'): CheckEventAvailabilityRequest.SerializeToString,
      ('soboto.items.ItemsService', 'duplicateItemEvent'): DuplicateItemEventRequest.SerializeToString,
    }
    response_deserializers = {
      ('soboto.items.ItemsService', 'checkEventAvailability'): CheckEventAvailabilityResponse.FromString,
      ('soboto.items.ItemsService', 'duplicateItemEvent'): DuplicateItemEventResponse.FromString,
    }
    cardinalities = {
      'checkEventAvailability': cardinality.Cardinality.UNARY_UNARY,
      'duplicateItemEvent': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'soboto.items.ItemsService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
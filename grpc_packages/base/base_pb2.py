# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base/base.proto',
  package='base',
  syntax='proto3',
  serialized_options=b'Z\030pyuser_center/proto/base',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x62\x61se/base.proto\x12\x04\x62\x61se\"Z\n\x04\x42\x61se\x12$\n\x05\x65xtra\x18\x01 \x03(\x0b\x32\x15.base.Base.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x88\x01\n\x08\x42\x61seResp\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12(\n\x05\x65xtra\x18\x03 \x03(\x0b\x32\x19.base.BaseResp.ExtraEntry\x1a,\n\nExtraEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x1aZ\x18pyuser_center/proto/baseb\x06proto3'
)




_BASE_EXTRAENTRY = _descriptor.Descriptor(
  name='ExtraEntry',
  full_name='base.Base.ExtraEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='base.Base.ExtraEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='base.Base.ExtraEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=115,
)

_BASE = _descriptor.Descriptor(
  name='Base',
  full_name='base.Base',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='extra', full_name='base.Base.extra', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BASE_EXTRAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=115,
)


_BASERESP_EXTRAENTRY = _descriptor.Descriptor(
  name='ExtraEntry',
  full_name='base.BaseResp.ExtraEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='base.BaseResp.ExtraEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='base.BaseResp.ExtraEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=115,
)

_BASERESP = _descriptor.Descriptor(
  name='BaseResp',
  full_name='base.BaseResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='base.BaseResp.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='base.BaseResp.status_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra', full_name='base.BaseResp.extra', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BASERESP_EXTRAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=254,
)

_BASE_EXTRAENTRY.containing_type = _BASE
_BASE.fields_by_name['extra'].message_type = _BASE_EXTRAENTRY
_BASERESP_EXTRAENTRY.containing_type = _BASERESP
_BASERESP.fields_by_name['extra'].message_type = _BASERESP_EXTRAENTRY
DESCRIPTOR.message_types_by_name['Base'] = _BASE
DESCRIPTOR.message_types_by_name['BaseResp'] = _BASERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Base = _reflection.GeneratedProtocolMessageType('Base', (_message.Message,), {

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _BASE_EXTRAENTRY,
    '__module__' : 'base.base_pb2'
    # @@protoc_insertion_point(class_scope:base.Base.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _BASE,
  '__module__' : 'base.base_pb2'
  # @@protoc_insertion_point(class_scope:base.Base)
  })
_sym_db.RegisterMessage(Base)
_sym_db.RegisterMessage(Base.ExtraEntry)

BaseResp = _reflection.GeneratedProtocolMessageType('BaseResp', (_message.Message,), {

  'ExtraEntry' : _reflection.GeneratedProtocolMessageType('ExtraEntry', (_message.Message,), {
    'DESCRIPTOR' : _BASERESP_EXTRAENTRY,
    '__module__' : 'base.base_pb2'
    # @@protoc_insertion_point(class_scope:base.BaseResp.ExtraEntry)
    })
  ,
  'DESCRIPTOR' : _BASERESP,
  '__module__' : 'base.base_pb2'
  # @@protoc_insertion_point(class_scope:base.BaseResp)
  })
_sym_db.RegisterMessage(BaseResp)
_sym_db.RegisterMessage(BaseResp.ExtraEntry)


DESCRIPTOR._options = None
_BASE_EXTRAENTRY._options = None
_BASERESP_EXTRAENTRY._options = None
# @@protoc_insertion_point(module_scope)
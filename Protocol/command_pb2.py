# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='command.proto',
  package='System',
  serialized_pb='\n\rcommand.proto\x12\x06System\"#\n\x07\x63ommand\x12\x0b\n\x03opt\x18\x01 \x02(\t\x12\x0b\n\x03\x61rg\x18\x02 \x01(\t')




_COMMAND = _descriptor.Descriptor(
  name='command',
  full_name='System.command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opt', full_name='System.command.opt', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg', full_name='System.command.arg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=25,
  serialized_end=60,
)

DESCRIPTOR.message_types_by_name['command'] = _COMMAND

class command(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMAND

  # @@protoc_insertion_point(class_scope:System.command)


# @@protoc_insertion_point(module_scope)

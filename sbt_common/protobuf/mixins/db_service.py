from decimal import Decimal
from datetime import datetime, date
from uuid import UUID
from rest_framework.settings import api_settings
from rest_framework import ISO_8601
from google.protobuf.descriptor import FieldDescriptor
from sbt_common.utils import datetime_to_epoch


class DJangoDBServiceMixin(object):

    def set_pb_model_attrs(self, db_model, pb_model):
        for attr in db_model.__dict__.keys():
            if getattr(db_model, attr, None) is None:
                continue

            if not hasattr(pb_model, attr):
                continue

            field = pb_model.DESCRIPTOR.fields_by_name[attr]
            if field.type == FieldDescriptor.TYPE_MESSAGE:
                continue

            value = getattr(db_model, attr)
            if type(value) == Decimal:
                value = float(value)
            elif type(value) == datetime:
                value = datetime_to_epoch(value)
            elif type(value) == date:
                output_format = getattr(self, 'format', api_settings.DATE_FORMAT)
                if output_format.lower() == ISO_8601:
                    value = value.isoformat()
                else:
                    value = value.strftime(output_format)
            elif type(value) == UUID:
                value = str(value)

            setattr(pb_model, attr, value)

        return pb_model

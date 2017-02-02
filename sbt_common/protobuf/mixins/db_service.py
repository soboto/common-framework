from sbt_common.helpers.fields import UnixEpochDateTimeField
from decimal import Decimal
from datetime import datetime
from uuid import UUID


class DJangoDBServiceMixin(object):

    def set_pb_model_attrs(self, db_model, pb_model):
        for attr in db_model.__dict__.keys():
            if getattr(db_model, attr, None) is None:
                continue

            if not hasattr(pb_model, attr):
                continue

            value = getattr(db_model, attr)
            if type(value) == Decimal:
                value = float(value)
            elif type(value) == datetime:
                value = UnixEpochDateTimeField.datetime_to_epoch(value)
            elif type(value) == UUID:
                value = str(value)

            setattr(pb_model, attr, value)

        return pb_model

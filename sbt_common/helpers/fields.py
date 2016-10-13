# -*- coding: utf-8 -*-
import calendar
import datetime

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.utils.timezone import utc
from rest_framework.fields import CharField, DateTimeField


class LanguageField(CharField):

    def to_internal_value(self, value):
        lang_code = cache.get('content_language')

        if self.parent.instance:
            current_value = getattr(self.parent.instance, self.source)

            if type(current_value) is dict:
                current_value[lang_code] = value
                return current_value

        return {
            lang_code: value
        }

    def to_representation(self, value):
        lang_code = cache.get('content_language')

        if lang_code in value:
            return value[lang_code]

        return ''


class UnixEpochDateTimeField(DateTimeField):

    def to_internal_value(self, value):
        return self.epoch_to_datetime(value)

    def to_representation(self, value):
        return self.datetime_to_epoch(value)

    @staticmethod
    def datetime_to_epoch(value):
        try:
            return int(calendar.timegm(value.utctimetuple()))
        except (AttributeError, TypeError):
            return None

    @staticmethod
    def epoch_to_datetime(value):
        try:
            return datetime.datetime.utcfromtimestamp(int(value)).replace(tzinfo=utc)
        except (ValueError, TypeError):
            raise ValidationError('%s is not a valid value' % value)

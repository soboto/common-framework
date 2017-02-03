# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from rest_framework.fields import CharField, DateTimeField
from sbt_common.utils import epoch_to_datetime, datetime_to_epoch


class LanguageField(CharField):

    def get_language_code(self):
        request = self.parent._context.get('request', None)
        assert request is not None, 'request have to be initializated on parent serializer ' \
                                    '(' + self.parent.__class__.__name__ + ') context'

        return getattr(request, 'content_language')

    def to_internal_value(self, value):
        lang_code = self.get_language_code()

        if self.parent.instance:
            current_value = getattr(self.parent.instance, self.source)

            if type(current_value) is dict:
                current_value[lang_code] = value
                return current_value

        return {
            lang_code: value
        }

    def to_representation(self, value):
        lang_code = self.get_language_code()

        if lang_code in value:
            return value[lang_code]

        return ''


class UnixEpochDateTimeField(DateTimeField):

    def to_internal_value(self, value):
        try:
            return epoch_to_datetime(value)
        except (ValueError, TypeError):
            raise ValidationError('%s is not a valid value' % value)

    def to_representation(self, value):
        return datetime_to_epoch(value)

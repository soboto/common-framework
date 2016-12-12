# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from rest_framework_gis.fields import GeometryField
from shapely.geometry import shape


class LocationField(GeometryField):
    """
    A field to handle GeoDjango Geometry fields
    """
    type_name = 'LocationField'

    def to_internal_value(self, value):

        try:
            return shape(value).wkt
        except (ValueError, TypeError):
            raise ValidationError(_('Invalid format: string or unicode input unrecognized GeoJSON.'))

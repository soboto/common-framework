# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'SOBOTO_COMMON', None)

DEFAULTS = {
    'REQUIRE_AUTH': True,
    'SERVICE_NAME': None,
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)

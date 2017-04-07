# -*- coding: utf-8 -*-
from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'SOBOTO_COMMON', None)

DEFAULTS = {
    'REQUIRE_AUTH': True,
    'SERVICE_NAME': None,
    'AUTH_MODEL_FACTORY': 'sbt_common.models.UserModelFactory',
    'DEFAULT_GRPC_PORT': 50050,
    'DEFAULT_GRPC_TIMEOUT': 60,

    'SERVICE_USERS_URL': 'sbtbackoffice_users-50050',

    'MESSAGE_SERVICE_PROVIDER': 'sbt_common.messaging.protobuf_provider.ProtobufProvider',
    'SERVICES': {
        'items': {
            'host': 'sbtbackoffice_items-50050',
            'module': 'items_pb2',
            'stub': 'beta_create_ItemsService_stub',
            'pb_service': 'beta_create_ItemsService_server'
        }
    }
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)

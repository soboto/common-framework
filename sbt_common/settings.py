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
        },
        'schedules': {
            'host': 'sbtbackoffice_schedules-50050',
            'module': 'schedules_pb2',
            'stub': 'beta_create_SchedulesService_stub',
            'pb_service': 'beta_create_SchedulesService_server'
        },
        'files': {
            'host': 'sbtbackoffice_files-50050',
            'module': 'files_pb2',
            'stub': 'beta_create_FilesService_stub',
            'pb_service': 'beta_create_FilesService_server'
        },
        'entities': {
            'host': 'sbtbackoffice_entities-50050',
            'module': 'entities_pb2',
            'stub': 'beta_create_EntitiesService_stub',
            'pb_service': 'beta_create_EntitiesService_server'
        },
        'settings': {
            'host': 'sbtbackoffice_settings-50050',
            'module': 'settings_pb2',
            'stub': 'beta_create_SettingsService_stub',
            'pb_service': 'beta_create_SettingsService_server'
        },
        'users': {
            'host': 'sbtbackoffice_users-50050',
            'module': 'users_pb2',
            'stub': 'beta_create_UsersService_stub',
            'pb_service': 'beta_create_UsersService_server'
        },
        'bookings': {
            'host': 'sbtbackoffice_bookings-50050',
            'module': 'bookings_pb2',
            'stub': 'beta_create_BookingsService_stub',
            'pb_service': 'beta_create_BookingsService_server'
        }
    }
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)

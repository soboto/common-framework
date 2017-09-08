# -*- coding: utf-8 -*-
from protobuf_to_dict import protobuf_to_dict
from django.contrib.auth.models import _user_has_perm, _user_get_all_permissions
from django.contrib.auth import get_user_model

from .constants import BO_USER_TYPE, CUSTOMER_USER_TYPE, ANONYMOUS_USER_TYPE
from .settings import api_settings


class AuthUser(object):
    id = None
    username = None
    name = None
    first_name = None
    last_name = None
    email = None
    type = None
    is_active = False
    is_superuser = False
    is_staff = False
    _perm_cache = set()

    def __init__(self, *args, **kwargs):
        for param in kwargs:
            setattr(self, param, kwargs.get(param))

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, name):
        return self

    def _get_groups(self):
        return self._groups
    groups = property(_get_groups)

    def _get_user_permissions(self):
        return self._user_permissions
    user_permissions = property(_get_user_permissions)

    def get_group_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return _user_get_all_permissions(self, obj=obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_perms(self, perm_list, obj=None):
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_username(self):
        return self.username


class BOUser(AuthUser):
    entity = None
    entity_type = None
    type = BO_USER_TYPE

    def __init__(self, *args, **kwargs):
        super(BOUser, self).__init__(*args, **kwargs)

        self.parse_entity()

    def parse_entity(self):
        entity_info = self.entity
        if isinstance(entity_info, dict):
            self.entity = entity_info['entity_id']
            self.entity_type = entity_info['entity_type']
        
    def get_entity(self):
        return self.entity


class Customer(AuthUser):
    type = CUSTOMER_USER_TYPE


class Anonymous(AuthUser):
    type = ANONYMOUS_USER_TYPE
    is_active = True

    def is_anonymous(self):
        return True


class UserModelFactory(object):
    _types = {
        BO_USER_TYPE: BOUser,
        CUSTOMER_USER_TYPE: Customer
    }
    user_info = None
    user_type = None

    def __init__(self, user_info, *args, **kwargs):
        super(UserModelFactory, self).__init__(*args, **kwargs)
        self.user_info = protobuf_to_dict(user_info)
        self.user_type = self.user_info.get('type')

    def get_user(self):
        if self.user_type not in self._types:
            raise Exception('Unrecognised user type')

        if api_settings.SERVICE_NAME == 'users' and 'id' in self.user_info:
            user_model = get_user_model()
            user = user_model.objects.get(pk=self.user_info['id'])
            return user

        user_model = self._types[self.user_type]
        return user_model(**self.user_info)


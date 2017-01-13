# -*- coding: utf-8 -*-
from protobuf_to_dict import protobuf_to_dict
from django.contrib.auth.models import _user_has_perm, _user_get_all_permissions


class DefaultAuthModelInterface(object):

    def get_model(self, user_info):
        user_info = protobuf_to_dict(user_info)
        user = AuthUser(**user_info)

        return user


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
    entity = []
    _perm_cache = set()

    def __init__(self, *args, **kwargs):
        for param in kwargs:
            setattr(self, param, kwargs.get(param))

        self.parse_entities()

    def parse_entities(self):
        self.entity = [e['id'] for e in self.entity]

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
